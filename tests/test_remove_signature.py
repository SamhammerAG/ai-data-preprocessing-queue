import unittest
from unittest.mock import MagicMock, patch

from parameterized import parameterized

from ai_data_preprocessing_queue.Pipeline import Pipeline
from ai_data_preprocessing_queue.Steps.remove_signature import remove_greetings_and_following_text, remove_newline, step


class TestRemoveSignature(unittest.TestCase):
    @parameterized.expand(
        [  # type: ignore[untyped-decorator]
            (
                "multiple_newlines",
                "Could you please review the attached document?\n\n\nI need your feedback by Friday.",
                "Could you please review the attached document? I need your feedback by Friday.",
            ),
            (
                "multiple_spaces",
                "The meeting    is scheduled    for 3PM    tomorrow.",
                "The meeting is scheduled for 3PM tomorrow.",
            ),
            (
                "mixed_whitespace",
                "Please find the report attached.  \n\n  The numbers look good   \r\n\r\n   for Q3!",
                "Please find the report attached. The numbers look good for Q3!",
            ),
            ("empty_string", "", ""),
            (
                "trailing_whitespace",
                "I'll send the updated version tomorrow.   \n\n  ",
                "I'll send the updated version tomorrow.",
            ),
        ]
    )
    def test_remove_newline(self, name: str, input_text: str, expected: str) -> None:
        self.assertEqual(remove_newline(input_text), expected)

    @parameterized.expand(
        [  # type: ignore[untyped-decorator]
            (
                "english_signature_basic",
                "Here's the project update. Sincerely, John Smith\nProject Manager",
                "Here's the project update.",
            ),
            (
                "english_signature_with_content",
                "Please review the attached documents. Best regards, Jane Doe\nSenior Developer\nTech Department",
                "Please review the attached documents.",
            ),
            (
                "english_signature_with_content_and_several_newlines",
                "Please review the attached documents. Best regards,\nJane Doe\n\nSenior Developer\n\nTech Department",
                "Please review the attached documents.",
            ),
            (
                "german_signature",
                "Die Unterlagen wurden aktualisiert. Mit freundlichen Grüßen, Hans Schmidt\nPhone: +49 123 456789",
                "Die Unterlagen wurden aktualisiert.",
            ),
            (
                "greeting_with_comma",
                "Meeting is scheduled for tomorrow. Kind regards, Sarah",
                "Meeting is scheduled for tomorrow.",
            ),
            ("mixed_case_greeting", "Report is ready. BEST REGARDS, Tom Wilson", "Report is ready."),
            (
                "multiple_greetings",
                "Hello team, here's the update. Best regards, Jim\nRegards, HR Team",
                "Hello team, here's the update.",
            ),
            ("empty_string", "", ""),
            (
                "no_greetings",
                "This is a plain text without any greetings or signatures.",
                "This is a plain text without any greetings or signatures.",
            ),
        ]
    )
    def test_remove_greetings_and_following_text(self, name: str, input_text: str, expected: str) -> None:
        self.assertEqual(remove_greetings_and_following_text(input_text), expected)

    @parameterized.expand(
        [  # type: ignore[untyped-decorator]
            (
                "remove_signature_basic",
                "We're sending the final draft for review. Best regards, Alice Johnson\nProject Lead",
                "We're sending the final draft for review.",
            ),
            (
                "remove_signature_extended",
                "Order Mice/keyboard\nGoodmorning, Can you please order the following: 10 x Dell Laser Mouse IL3220 "
                "10 x Dell Business Keyboard AB322 (UK layout) Thx Best regards Jimmy B. "
                "| C Facilities & Reception Klaus+Andreas Nederland | Anonymstraat 47 | 1234 AJ Amsterdam | "
                "Netherlands "
                "Phone: +01 23 695 4567 | Mobile: +97 65 445 1234 | Fax: +31 35 695 8825 jim.anonymus@company.com "
                "| www.nl.somecompany.com",
                "Order Mice/keyboard Goodmorning, Can you please order the following: 10 x Dell Laser Mouse IL3220 "
                "10 x Dell Business Keyboard AB322 (UK layout) Thx",
            ),
            (
                "thanking_at_start",
                "Thank you very much for your support. "
                "I will prepare the contract and send it tomorrow.\n\nBest regards, Bob Brown",
                "I will prepare the contract and send it tomorrow.",
            ),
            (
                "thanking_in_middle",
                "Thank you very much for your support. "
                "I appreciate your support on this migration. Thanks a lot, I will share the logs shortly.",
                "I appreciate your support on this migration. I will share the logs shortly.",
            ),
            (
                "single_greeting_word_german",
                "The deliverables are ready. Grüße",
                "The deliverables are ready.",
            ),
            (
                "german_empty_result",
                "Vielen Dank für Ihre Hilfe. Mit freundlichen Grüßen, Lena Meyer Und hier kommt noch mehr Text.",
                "",
            ),
            (
                "no_change",
                "Please schedule the kickoff meeting for next Tuesday morning at 10:00.",
                "Please schedule the kickoff meeting for next Tuesday morning at 10:00.",
            ),
        ]
    )
    def test_remove_signature(self, name: str, input_text: str, expected: str) -> None:
        pipeline = Pipeline({"remove_signature": None})
        value = pipeline.consume(input_text)
        self.assertEqual(expected, value)

    def test_remove_signature_step_empty_item(self) -> None:
        result = step("", {}, None, "")
        self.assertEqual(result, "")

    @patch(
        "ai_data_preprocessing_queue.Steps.remove_signature.remove_greetings_and_following_text",
        side_effect=Exception("Test error"),
    )
    def test_remove_signature_step_error(self, _: MagicMock) -> None:
        with self.assertRaises(Exception):
            step("Please schedule the kickoff meeting for next Tuesday morning at 10:00.", {}, None, "")


if __name__ == "__main__":
    unittest.main()
    unittest.main()
