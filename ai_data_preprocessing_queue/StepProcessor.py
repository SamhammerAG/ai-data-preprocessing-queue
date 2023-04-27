import importlib
from typing import Any, Dict, Optional

# required import because of logic in init
from . import Steps  # noqa: F401


class StepProcessor:
    def __init__(self, name: str, stepData: Optional[str]) -> None:
        self.name: str = name
        self.stepData: Optional[str] = stepData

        package_name = f"{__package__}.Steps"
        module_name = f".{self.name}"
        self.module = importlib.import_module(module_name, package_name)

        assert self.module.step is not None

    def run(self, item: Any, itemState: Dict[str, Any], globalState: Optional[Dict[str, Any]] = None) -> Any:
        return self.module.step(item, itemState, globalState, self.stepData or "")
