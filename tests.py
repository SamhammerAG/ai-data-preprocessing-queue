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

    def test_multiple_steps(self):
        pipeline = Pipeline(['text_only', 'to_lower'])
        value = pipeline.consume('123 CamelCase')
        self.assertEqual(value, '    camelcase')

if __name__ == '__main__':
    unittest.main()
