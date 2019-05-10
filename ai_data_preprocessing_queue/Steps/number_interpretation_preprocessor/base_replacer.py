from abc import ABC, abstractmethod
from typing import Pattern
import re

class BaseReplacer(ABC):
    @abstractmethod
    def regex(self: 'BaseReplacer') -> Pattern:
        pass

    @abstractmethod
    def token(self: 'BaseReplacer') -> str:
        pass

    @abstractmethod
    def order(self: 'BaseReplacer') -> int:
        pass

    def replace(self: 'BaseReplacer', text: str) -> str:
        pattern = re.compile(self.regex())
        return pattern.sub(self.token(), text)
