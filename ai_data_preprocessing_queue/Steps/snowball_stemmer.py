import warnings
from typing import Any, Dict, Optional

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    from nltk.stem.snowball import SnowballStemmer


langMapping = {"de": SnowballStemmer("german"), "en": SnowballStemmer("english")}


def step(item: Any, itemState: Dict[str, Any], globalState: Optional[Dict[str, Any]], preprocessorData: str) -> Any:
    stemmer = langMapping.get(itemState["language"], langMapping["en"])

    stemmed_words = [stemmer.stem(word) for word in item.split()]

    return " ".join(stemmed_words)
