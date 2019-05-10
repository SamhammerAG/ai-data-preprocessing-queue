from .base_replacer import BaseReplacer
from typing import Pattern

class IbanReplacer(BaseReplacer):
    def regex(self: 'DateReplacer') -> Pattern:
        return r"\bDE\d{2}\s*\d{4}\s*\d{4}\s*\d{4}\s*\d{4}\s*\d{2}\b"

    def order(self: 'ShortDateReplacer') -> int:
        return 1

    def token(self: 'ShortDateReplacer') -> str: 
        return "replacediban"