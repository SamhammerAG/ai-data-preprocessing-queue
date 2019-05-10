from .base_replacer import BaseReplacer
from typing import Pattern, List

class DateReplacer(BaseReplacer):
    def regex(self: 'DateReplacer') -> List[Pattern]:
        return [r"\b(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[1-9])\.([1-9]|0[1-9]|1[0-2])\.((19|20)\d{2})\b"]

    def order(self: 'DateReplacer') -> int:
        return 1

    def token(self: 'DateReplacer') -> str:
        return "replaceddate"