from abc import ABC, abstractmethod
from typing import Pattern, List
import re

class BaseReplacer(ABC):
    @abstractmethod
    def regex(self: 'BaseReplacer') -> List[Pattern]:
        pass

    @abstractmethod
    def token(self: 'BaseReplacer') -> str:
        pass

    @abstractmethod
    def order(self: 'BaseReplacer') -> int:
        pass

    def replace(self: 'BaseReplacer', text: str) -> str:
        for p in self.regex():
            pattern = re.compile(p)
            text = pattern.sub(self.token(), text)
        return text
