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
        value = pipeline.consume("1.1.2019 20.2.2003 1.1.20 01.01.20 1.1.1900")
        self.assertEqual(value, 'replaceddate replaceddate replaceddate replaceddate replaceddate')

if __name__ == '__main__':
    unittest.main()
