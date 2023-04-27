from typing import Any, Dict, List, Optional

from .StepProcessor import StepProcessor


class Pipeline:
    def __init__(self, step_dict: Dict[str, Optional[str]]) -> None:
        self.step_processors: List[StepProcessor] = []
        for step_name in list(filter(None, step_dict.keys())):
            processor = StepProcessor(step_name, step_dict.get(step_name))
            self.step_processors.append(processor)

    def consume(self, item: Any, globalState: Optional[Dict[str, Any]] = None) -> Any:
        retVal = item

        itemState: Dict[str, Any] = {}
        for processor in self.step_processors:
            retVal = processor.run(retVal, itemState, globalState)

        return retVal
