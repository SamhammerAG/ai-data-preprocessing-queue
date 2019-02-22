import importlib


class StepProcessor:
    def __init__(self, name):
        self.name = name

        package_name = __package__ + '.Steps'
        module_name = '.' + self.name
        self.module = importlib.import_module(module_name, package_name)

        assert self.module.step is not None

    def run(self, item, itemState, globalState=None):
        return self.module.step(item, itemState, globalState)
