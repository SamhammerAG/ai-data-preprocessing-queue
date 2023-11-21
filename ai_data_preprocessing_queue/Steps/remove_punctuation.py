import re
from typing import Any, Dict, Optional


def step(item: Any, item_state: Dict[str, Any], global_state: Optional[Dict[str, Any]], preprocessor_data: str) -> Any:
    item = re.sub(r"[^\w\s]", " ", item)
    return item
