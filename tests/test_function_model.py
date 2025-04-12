import pandas as pd
from function_model import IdealFunction

def test_get_summary():
    x = pd.Series([1, 2, 3])
    y = pd.Series([2, 4, 6])
    f = IdealFunction("test", x, y)
    summary = f.get_summary()
    assert round(summary["mean"], 2) == 4.0
    assert summary["min"] == 2
    assert summary["max"] == 6
