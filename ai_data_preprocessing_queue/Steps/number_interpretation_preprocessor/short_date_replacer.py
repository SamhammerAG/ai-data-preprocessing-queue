from .date_replacer import DateReplacer
from typing import Pattern, List

class ShortDateReplacer(DateReplacer):
    def regex(self: 'DateReplacer') -> List[Pattern]:
        return [
                r"\b(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[1-9])\.([1-9]|0[1-9]|1[0-2])\.((19|20)\d{2})\b",
                r"\b(\d{2})\.(\d{2})\.(\d{4})\b",
                r"\b(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[1-9])\.([1-9]|0[1-9]|1[0-2])\.(\d{2})(\s+)\b",
                r"\b(\d{2})\.(\d{2})\.(\d{2})\b",
                r"\b(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[1-9])\.([1-9]|0[1-9]|1[0-2])(\.)?\s+\b"
            ]