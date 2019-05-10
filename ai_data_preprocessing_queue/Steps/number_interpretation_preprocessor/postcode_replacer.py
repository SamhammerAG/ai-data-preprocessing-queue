from .base_replacer import BaseReplacer
from typing import Pattern, List

class PostcodeReplacer(BaseReplacer):
    def token(self: 'PostcodeReplacer') -> str:
        return "replacedpostcode"
    
    def regex(self: 'PostCodeReplacer') -> List[Pattern]:
        return [r"\b([0]{1}[1-9]{1}|[1-9]{1}[0-9]{1})[0-9]{3}\b"]

    def order(self: 'PostCodeReplacer') -> int:
        return 20