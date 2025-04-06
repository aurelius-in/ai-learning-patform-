import pandas as pd
from src.data.preprocessing import clean_text, preprocess_dataframe

def test_clean_text():
    text = "Hello, World! 123"
    assert clean_text(text) == "hello world 123"

def test_preprocess_dataframe():
    df = pd.DataFrame({"text": ["Hello, TEST!"]})
    processed_df = preprocess_dataframe(df, "text")
    assert processed_df.loc[0, "text"] == "hello test"
