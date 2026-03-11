import re
from typing import Any


def remove_newline(text: str) -> str:
    """Remove excessive newlines or spaces from the text."""
    pattern = re.compile(r"\s{2,}|[\n\r]{3,}")
    result = pattern.sub(" ", text)
    return re.sub(r"\s+", " ", result).strip()


GreetingExpressions = [
    "sincerely",
    "best regards",
    "happy holidays",
    "kind regards",
    "warm regards",
    "cheers",
    "regards",
    "mit freundlichen grüßen",
    "freundliche grüße",
    "beste grüße",
    "viele grüße",
    "herzliche grüße",
    "liebe grüße",
    "mit freundlichen grüssen",
    "freundliche grüsse",
    "beste grüsse",
    "viele grüsse",
    "herzliche grüsse",
    "liebe grüsse",
]
greetings_regex = r"(" + "|".join(GreetingExpressions) + r")\s*,?\s*"


def remove_greetings_and_following_text(text: str) -> str:
    pattern = greetings_regex + ".*"
    return re.sub(pattern, "", text, flags=re.IGNORECASE | re.UNICODE | re.DOTALL).strip()


# thank you expressions should be removed after greetings and following signature text,
# as they often appear at the beginning of a message
THANK_EXPRESSIONS = [
    r"thank you(?: very much)?",  # thank you, thank you very much
    r"thankyou(?: very much)?",  # thankyou, thankyou very much
    r"thanks(?: a lot| again)?",  # thanks, thanks a lot, thanks again
    r"many thanks",  # many thanks
    r"a thousand thanks",  # a thousand thanks
    r"danke(?: schön)?",  # danke, danke schön, danke und
    r"vielen dank",  # vielen dank
    r"dankeschön",  # dankeschön
    r"besten dank",  # besten dank
]

# Suffixes which could follow thank you expressions
THANK_SUFFIXES = [
    r"(?:in advance(?: for (?:your|the) (?:help|support|understanding|assistance))?)",
    r"(?:for (?:your|the) (?:help|support|understanding|assistance))",
    r"(?:schon mal\s+)?(?:im voraus\s+)?für\s+(?:ihre|ihr|eure|die|den)\s+(?:hilfe|support|verständnis)",
    r"vorab",
    r"kindly?",
]

# Combine them into a final regex pattern and compile
thank_expressions = r"|".join(THANK_EXPRESSIONS)
suffixes = r"(?:\s+(?:" + r"|".join(THANK_SUFFIXES) + r"))?"
final_pattern = r"\b(?:" + thank_expressions + r")" + suffixes + r"\s*(?:,|\.|!|;)?\s*"
thanking_regex = re.compile(final_pattern, flags=re.IGNORECASE | re.UNICODE)


def remove_thanking_expressions(text: str) -> str:
    return thanking_regex.sub("", text)


# In the end, single greetings are removed again, which could not
# be reliably removed by the preceding expressions
single_greeting_words = ["liebe grüße", "liebe grüsse", "grüße", "grüsse", "gruß", "gruss"]
single_greetings_pattern = r"\b(?:{})\b".format("|".join(single_greeting_words))


def remove_single_greeting_words(text: str, pattern: str) -> str:
    return re.sub(pattern, " ", text, flags=re.IGNORECASE | re.UNICODE)


def step(item: Any, item_state: dict[str, Any], global_state: dict[str, Any] | None, preprocessor_data: str) -> Any:
    if not item:
        return item
    try:
        text_greetings_removed = remove_greetings_and_following_text(item)
        thankyou_removed = remove_thanking_expressions(text_greetings_removed)
        single_greetings_removed = remove_single_greeting_words(thankyou_removed, single_greetings_pattern)

        return remove_newline(single_greetings_removed)
    except Exception as e:
        raise ValueError(f"An error occurred while removing signature: {e}") from e
