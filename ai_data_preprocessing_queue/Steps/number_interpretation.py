import re
import glob
from pathlib import Path
from .number_interpretation_preprocessor import BaseReplacer
from os.path import dirname
from typing import List

def step(item, itemState, globalState):
    """replace numbers with tokens"""

    # read all classes of type BaseReplacer
    replacerNames: List[str] = [Path(f).parts[-1].replace(".py", "") 
        for f in glob.glob(dirname(__file__)+"/number_interpretation_preprocessor/*.py")
        if f.find("__init__") == -1 and f.find("base_replacer") == -1]
    
    fn = lambda n: __import__('ai_data_preprocessing_queue.Steps.number_interpretation_preprocessor', fromlist=[n])
    sort = lambda o: o.order()
    
    instances: List[BaseReplacer] = [getattr(fn(f), f.title().replace("_", ""))() for f in replacerNames]
    instances.sort(key = sort)

    for i in instances:
        item = i.replace(item)

    return item