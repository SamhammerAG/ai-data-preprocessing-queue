import re
from typing import Any


def step(item: Any, item_state: dict[str, Any], global_state: dict[str, Any] | None, preprocessor_data: str) -> Any:
    return re.sub(r"[^\w\s]", " ", item)
