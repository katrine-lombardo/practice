"""
Get Gnome Information
"""

import requests
import pandas as pd
from sqlalchemy import create_engine


# EXTRACT
def extract() -> dict:
    API_URL = "https://www.dnd5eapi.co/api/races/gnome"
    data = requests.get(API_URL).json()
    return data


# TRANSFORM
def transform(data: dict) -> pd.DataFrame:
    gnome_data = {
        "name": data.get("name"),
        "speed": data.get("speed"),
        "alignment": data.get("alignment"),
        "languages": ",".join([lang["name"] for lang in data.get("languages", [])]),
        "traits": ",".join([trait["name"] for trait in data.get("traits", [])]),
    }
    df = pd.DataFrame([gnome_data])
    df.dropna(inplace=True)
    return df


# LOAD
def load(df: pd.DataFrame) -> None:
    disk_engine = create_engine(f"sqlite:///my_lite_store.db")
    df.to_sql("gnome_info", disk_engine, if_exists="replace")


# EXECUTE
data = extract()
if data:
    df = transform(data)
    load(df)
else:
    print("Error: Failed to retrieve data from the API.")
