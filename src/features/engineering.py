import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

def encode_categorical(df, column):
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column].astype(str))
    return df, le

def scale_numerical(df, columns):
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df, scaler

def add_text_length_feature(df, text_column):
    df['text_length'] = df[text_column].astype(str).apply(len)
    return df
