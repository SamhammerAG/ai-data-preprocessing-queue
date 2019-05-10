from .base_replacer import BaseReplacer
from typing import Pattern, List

class GermanPhonenumberReplacer(BaseReplacer):
    def regex(self: 'GermanPhonenumberReplacer') -> List[Pattern]:
        return [r"(\(?([\d\-\)\–\+\/\(]+){6,}\)?([ .-–\/]?)([\d]+))"]

    def order(self: 'GermanPhonenumberReplacer') -> int:
        return 10

    def token(self: 'GermanPhonenumberReplacer') -> str:
        return "replacedgermanphonenumber"