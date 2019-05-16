import unittest

from ai_data_preprocessing_queue.Pipeline import Pipeline


class PipelineTest(unittest.TestCase):

    def test_text_only(self):
        pipeline = Pipeline(['text_only'])
        value = pipeline.consume('123 text - "more" text , and .')
        self.assertEqual(value, '    text    more  text   and  ')

    def test_text_to_lower(self):
        pipeline = Pipeline(['to_lower'])
        value = pipeline.consume('This is a Test text with CamelCase')
        self.assertEqual(value, 'this is a test text with camelcase')

    def test_snowball_stemmer_english(self):
        pipeline = Pipeline(['language_detect', 'snowball_stemmer'])
        value = pipeline.consume('how can i trouble troubling troubled')
        self.assertEqual(value, 'how can i troubl troubl troubl')

    def test_snowball_stemmer_german(self):
        pipeline = Pipeline(['language_detect', 'snowball_stemmer'])
        value = pipeline.consume('Wie kann ich kategorie kategorien kategorischen kategorisch')
        self.assertEqual(value, 'wie kann ich kategori kategori kategor kategor')

    def test_multiple_steps(self):
        pipeline = Pipeline(['text_only', 'to_lower'])
        value = pipeline.consume('123 CamelCase')
        self.assertEqual(value, '    camelcase')

    def test_number_interpretation(self):
        pipeline = Pipeline(["number_interpretation"])
        # date
        value = pipeline.consume("test 1.1.2019 20.2.2003 1.1.20 01.01.20 1.1.1900 1.1. 01.01. test")
        self.assertEqual(value, 'test  replaceddate   replaceddate   replaceddate  replaceddate replaceddate   replaceddate  replaceddate test')
        # iban
        value = pipeline.consume("test DE12500101170648489890")
        self.assertEqual(value, 'test  replacediban ')
        # postcode
        value = pipeline.consume("test 92637 92709 test")
        self.assertEqual(value, 'test  replacedpostcode   replacedpostcode  test')
        # german phone
        value = pipeline.consume("test 0961123456 test")
        self.assertEqual(value, 'test  replacedgermanphonenumber  test')
        value = pipeline.consume("test (0961)123456 test")
        self.assertEqual(value, 'test  replacedgermanphonenumber  test')
        value = pipeline.consume("test +49(0)121-79536-77 test")
        self.assertEqual(value, 'test  replacedgermanphonenumber  test')
        # german handy
        value = pipeline.consume("test 015125391111 test")
        self.assertEqual(value, 'test  replacedgermanphonenumber  test')

    def test_number_interpretation_with_preprocessor_data(self):
        handler = open("./number_interpretation_testdata.csv", "r")
        pipeline = Pipeline(["number_interpretation"], {"number_interpretation": handler.read()})
        # should not replace dates with custom data
        value = pipeline.consume("test 1.1.2019 20.2.2003 1.1.20 01.01.20 1.1.1900 1.1. 01.01. test")
        self.assertEqual(value, 'test 1.1.2019 20.2.2003 1.1.20 01.01.20 1.1.1900 1.1. 01.01. test')
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
        self.assertEqual(value, 'test  replacedgermanphonenumber  test')

    def test_token_replacement(self):
        handler = open("./token_replacement.csv", "r")
        pipeline = Pipeline(["token_replacement"], {"token_replacement": handler.read()})
        value = pipeline.consume("test aufgeregt")
        self.assertEqual(value, 'test angryword')

    def test_spellcheck(self):
        pipeline = Pipeline(["spellcheck"], { "spellcheck": "kopie\r\nartikel\r\n"})
        value = pipeline.consume("kopie koipe artikel artikle artilek artleki")
        self.assertEqual(value, 'kopie kopie artikel artikel artikel artleki')

        pipeline = Pipeline(["spellcheck"])
        value = pipeline.consume("kopie koipe artikel artikle artilek artleki")
        self.assertEqual(value, 'kopie koipe artikel artikle artilek artleki')


if __name__ == '__main__':
    unittest.main()
