import re
from typing import Any, Dict, Optional


def step(item: Any, itemState: Dict[str, Any], globalState: Optional[Dict[str, Any]], preprocessorData: str) -> Any:
    item = re.sub(r"[^\w\s]", " ", item)
    return item
