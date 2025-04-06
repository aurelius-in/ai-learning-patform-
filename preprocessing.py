import pandas as pd
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess_dataframe(df, text_column):
    df[text_column] = df[text_column].astype(str).apply(clean_text)
    return df