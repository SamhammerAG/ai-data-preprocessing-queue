from .StepProcessor import StepProcessor
from typing import Dict, Optional


class Pipeline:

    def __init__(self, step_dict: Dict[str, Optional[str]]):
        self.step_processors = []
        for step_name in list(filter(None, step_dict.keys())):
            processor = StepProcessor(step_name, step_dict.get(step_name))
            self.step_processors.append(processor)

    def consume(self, text, globalState=None):
        retVal = text

        itemState = {}
        for processor in self.step_processors:
            retVal = processor.run(retVal, itemState, globalState)

        return retVal
