"""
Get Gnome Information
"""

import requests
import pandas as pd
from sqlalchemy import create_engine


# EXTRACT
def extract(api_urls: list) -> list:
    extracted_data = []
    for url in api_urls:
        data = requests.get(url).json()
        if data:
            extracted_data.append(data)
    return extracted_data


# TRANSFORM
def transform(data_list: list) -> pd.DataFrame:
    dfs = []
    for data in data_list:
        race_data = {
            "name": data.get("name"),
            "speed": data.get("speed"),
            "alignment": data.get("alignment"),
            "languages": ",".join([lang["name"] for lang in data.get("languages", [])]),
            "traits": ",".join([trait["name"] for trait in data.get("traits", [])]),
        }
        print(f"Race data: {race_data}")
        df = pd.DataFrame([race_data])
        dfs.append(df)
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        return pd.DataFrame()


# LOAD
def load(df: pd.DataFrame, table_name: str) -> None:
    if not df.empty:
        disk_engine = create_engine(f"sqlite:///my_lite_store.db")
        df.to_sql(table_name, disk_engine, if_exists="replace", index=False)
        print(f"Data loaded into {table_name} table successfully.")
    else:
        print("Error: DataFrame is empty. No data to load.")


# EXECUTE
api_urls = [
    "https://www.dnd5eapi.co/api/races/gnome",
    "https://www.dnd5eapi.co/api/races/elf",
    "https://www.dnd5eapi.co/api/races/half-orc",
]
data_list = extract(api_urls)
df = transform(data_list)

if not df.empty:
    load(df, "dnd_races")
else:
    print("Error: No data to load.")
