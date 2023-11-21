import importlib
from typing import Any, Dict, Optional

# required import because of logic in init
from . import Steps  # noqa: F401


class StepProcessor:
    def __init__(self, name: str, step_data: Optional[str]) -> None:
        self.name: str = name
        self.step_data: Optional[str] = step_data

        package_name = f"{__package__}.Steps"
        module_name = f".{self.name}"
        self.module = importlib.import_module(module_name, package_name)

        assert self.module.step is not None

    def run(self, item: Any, item_state: Dict[str, Any], global_state: Optional[Dict[str, Any]] = None) -> Any:
        return self.module.step(item, item_state, global_state, self.step_data or "")
