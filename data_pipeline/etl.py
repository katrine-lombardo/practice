"""
Python Extract Transform Load Example
"""

import requests
import pandas as pd
from sqlalchemy import create_engine
import os


# EXTRACT
def extract() -> dict:
    API_URL = "http://universities.hipolabs.com/search?country=United+States"
    data = requests.get(API_URL).json()
    return data


# TRANSFORM
def transform(data: dict) -> pd.DataFrame:
    df = pd.DataFrame(data)
    print(f"Total Number of universities from API {len(data)}")
    df = df[df["name"].str.contains("California")]
    print(f"Number of universities in California: {len(df)}")
    df["domains"] = [",".join(map(str, l)) for l in df["domains"]]
    df["web_pages"] = [",".join(map(str, l)) for l in df["web_pages"]]
    df = df.reset_index(drop=True)
    return df[["domains", "country", "web_pages", "name"]]


# LOAD
def load(df: pd.DataFrame) -> None:
    disk_engine = create_engine(f"sqlite:///my_lite_store.db")
    df.to_sql("cal_uni", disk_engine, if_exists="replace")


# EXECUTE
data = extract()
df = transform(data)
load(df)
