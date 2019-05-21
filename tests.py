import unittest

from ai_data_preprocessing_queue.Pipeline import Pipeline


class PipelineTest(unittest.TestCase):

    def test_text_only(self):
        pipeline = Pipeline({'text_only': None})
        value = pipeline.consume('123 text - "more" text , and .')
        self.assertEqual('    text    more  text   and  ', value)

    def test_text_to_lower(self):
        pipeline = Pipeline({'to_lower': None})
        value = pipeline.consume('This is a Test text with CamelCase')
        self.assertEqual('this is a test text with camelcase', value)

    def test_snowball_stemmer_english(self):
        pipeline = Pipeline({'language_detect': None, 'snowball_stemmer': None})
        value = pipeline.consume('how can i trouble troubling troubled')
        self.assertEqual('how can i troubl troubl troubl', value)

    def test_snowball_stemmer_german(self):
        pipeline = Pipeline({'language_detect': None, 'snowball_stemmer': None})
        value = pipeline.consume('Wie kann ich kategorie kategorien kategorischen kategorisch')
        self.assertEqual('wie kann ich kategori kategori kategor kategor', value)

    def test_multiple_steps(self):
        pipeline = Pipeline({'text_only': None, 'to_lower': None})
        value = pipeline.consume('123 CamelCase')
        self.assertEqual('    camelcase', value)

    def test_number_interpretation_do_not_crash_for_no_data(self):
        pipeline = Pipeline({"number_interpretation": None})
        value = pipeline.consume("test text")
        self.assertEqual("test text", value)

    def test_number_interpretation(self):
        handler = open("./number_interpretation_testdata.csv", "r")
        pipeline = Pipeline({"number_interpretation": handler.read()})
        handler.close()
        # date
        value = pipeline.consume("test 1.1.2019 20.2.2003 1.1.20 01.01.20 1.1.1900 1.1. 01.01. test")
        self.assertEqual('test  replaceddate   replaceddate   replaceddate  replaceddate replaceddate   replaceddate  replaceddate test', value)
        # iban
        value = pipeline.consume("test DE12500101170648489890")
        self.assertEqual('test  replacediban ', value)
        # postcode
        value = pipeline.consume("test 92637 92709 test")
        self.assertEqual('test  replacedpostcode   replacedpostcode  test', value)
        # german phone
        value = pipeline.consume("test 0961123456 test")
        self.assertEqual('test  replacedgermanphonenumber  test', value)
        value = pipeline.consume("test (0961)123456 test")
        self.assertEqual('test  replacedgermanphonenumber  test', value)
        value = pipeline.consume("test +49(0)121-79536-77 test")
        self.assertEqual('test  replacedgermanphonenumber  test', value)
        # german handy
        value = pipeline.consume("test 015125391111 test")
        self.assertEqual('test  replacedgermanphonenumber  test', value)

    def test_token_replacement_do_not_crash_for_no_data(self):
        pipeline = Pipeline({"token_replacement": None})
        value = pipeline.consume("test text")
        self.assertEqual("test text", value)

    def test_token_replacement(self):
        handler = open("./token_replacement_testdata.csv", "r")
        pipeline = Pipeline({"token_replacement": handler.read()})
        handler.close()
        value = pipeline.consume("test asd bla 1212")
        self.assertEqual('test www blub 1212', value)

    def test_token_replacement_do_not_replace_parts_of_word(self):
        handler = open("./token_replacement_testdata.csv", "r")
        pipeline = Pipeline({"token_replacement": handler.read()})
        handler.close()
        value = pipeline.consume("test abg. abgabgeschlossen 1212")
        self.assertEqual('test abgeschlossen abgabgeschlossen 1212', value)

    def test_token_replacement_also_replace_dots_at_end_of_phrase(self):
        handler = open("./token_replacement_testdata.csv", "r")
        pipeline = Pipeline({"token_replacement": handler.read()})
        handler.close()
        value = pipeline.consume("abg. 1212")
        self.assertEqual('abgeschlossen 1212', value)

    def test_spellcheck_do_not_crash_for_no_data(self):
        pipeline = Pipeline({"spellcheck": "kopie\r\nartikel\r\n"})
        value = pipeline.consume("kopie koipe artikel artikle artilek artleki")
        self.assertEqual('kopie kopie artikel artikel artikel artleki', value)

    def test_spellcheck(self):
        pipeline = Pipeline({"spellcheck": None})
        value = pipeline.consume("kopie koipe artikel artikle artilek artleki")
        self.assertEqual('kopie koipe artikel artikle artilek artleki', value)

    def test_spellcheck_should_not_throw_exception_for_short_values(self):
        pipeline = Pipeline({"spellcheck": "kopie\r\nartikel\r\n"})
        value = pipeline.consume("k koipe artikel")
        self.assertEqual('k kopie artikel', value)


if __name__ == '__main__':
    unittest.main()
