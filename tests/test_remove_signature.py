import unittest

from parameterized import parameterized

from ai_data_preprocessing_queue.Steps.remove_signature import (
    remove_greetings_and_following_text, remove_newline)


class TestRemoveSignature(unittest.TestCase):
    @parameterized.expand([  # type: ignore[misc]
        ("multiple_newlines",
            "Could you please review the attached document?\n\n\nI need your feedback by Friday.",
            "Could you please review the attached document? I need your feedback by Friday."
        ),
        (
            "multiple_spaces",
            "The meeting    is scheduled    for 3PM    tomorrow.",
            "The meeting is scheduled for 3PM tomorrow."
        ),
        (
            "mixed_whitespace",
            "Please find the report attached.  \n\n  The numbers look good   \r\n\r\n   for Q3!",
            "Please find the report attached. The numbers look good for Q3!"
        ),
        (
            "empty_string",
            "",
            ""
        ),
        (
            "trailing_whitespace",
            "I'll send the updated version tomorrow.   \n\n  ",
            "I'll send the updated version tomorrow."
        ),
    ])
    def test_remove_newline(self, name: str, input_text: str, expected: str) -> None:
        self.assertEqual(remove_newline(input_text), expected)

    @parameterized.expand([  # type: ignore[misc]
        (
            "english_signature_basic",
            "Here's the project update. Sincerely, John Smith\nProject Manager",
            "Here's the project update."
        ),
        (
            "english_signature_with_content",
            "Please review the attached documents. Best regards, Jane Doe\nSenior Developer\nTech Department",
            "Please review the attached documents."
        ),
        (
            "english_signature_with_content_and_several_newlines",
            "Please review the attached documents. Best regards,\nJane Doe\n\nSenior Developer\n\nTech Department",
            "Please review the attached documents."
        ),
        (
            "german_signature",
            "Die Unterlagen wurden aktualisiert. Mit freundlichen Grüßen, Hans Schmidt\nPhone: +49 123 456789",
            "Die Unterlagen wurden aktualisiert."
        ),
        (
            "greeting_with_comma",
            "Meeting is scheduled for tomorrow. Kind regards, Sarah",
            "Meeting is scheduled for tomorrow."
        ),
        (
            "mixed_case_greeting",
            "Report is ready. BEST REGARDS, Tom Wilson",
            "Report is ready."
        ),
        (
            "multiple_greetings",
            "Hello team, here's the update. Best regards, Jim\nRegards, HR Team",
            "Hello team, here's the update."
        ),
        (
            "empty_string",
            "",
            ""
        ),
        (
            "no_greetings",
            "This is a plain text without any greetings or signatures.",
            "This is a plain text without any greetings or signatures."
        )
    ])
    def test_remove_greetings_and_following_text(self, name: str, input_text: str, expected: str) -> None:
        self.assertEqual(remove_greetings_and_following_text(input_text), expected)


if __name__ == '__main__':
    unittest.main()
    unittest.main()
