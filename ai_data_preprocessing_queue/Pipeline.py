from .StepProcessor import StepProcessor


class Pipeline():

    def __init__(self, step_names):
        self.step_processors = []
        for step_name in step_names:
            processor = StepProcessor(step_name)
            self.step_processors.append(processor)

    def consume(self, text, globalState=None):
        retVal = text

        for processor in self.step_processors:
            retVal = processor.run(retVal, globalState)

        return retVal
