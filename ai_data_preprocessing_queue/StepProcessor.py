import importlib
from .Steps import language_detect


class StepProcessor:
    def __init__(self, name, stepData):
        self.name = name
        self.stepData = stepData

        package_name = __package__ + '.Steps'
        module_name = '.' + self.name
        self.module = importlib.import_module(module_name, package_name)

        assert self.module.step is not None

    def run(self, item, itemState, globalState=None):
        return self.module.step(item, itemState, globalState, self.stepData or "")
