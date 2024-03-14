"""
Get DnD Race Information
"""

import requests
import pandas as pd
from sqlalchemy import create_engine, update
from sqlalchemy import MetaData, Table, Column, String
from sqlalchemy.exc import SQLAlchemyError


# EXTRACT
def extract(api_urls: list) -> list:
    extracted_data = []
    for url in api_urls:
        try:
            data = requests.get(url).json()
            if data:
                extracted_data.append(data)
        except requests.exceptions.RequestException as e:
            print(f"Error extracting data from {url}: {e}")
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


# EDIT PLAYER NAMES
def edit_player_name(engine, table_name, index, new_player_name):
    try:
        with engine.connect() as connection:
            metadata = MetaData()
            table = Table(table_name, metadata, autoload_with=engine)
            player_name = Column("player_name", String)
            if "player_name" not in table.columns:
                player_name_column = Column("player_name", String)
                table.append_column(player_name_column)
                metadata.create_all(engine)
            update_stmt = (
                update(table)
                .where(table.c.index == index)
                .values(player_name=new_player_name)
            )
            result = connection.execute(update_stmt)
            if result.rowcount:
                print(f"Player name for id {index} updated successfully.")
            else:
                print(f"No rows matched the update condition for id {index}.")
    except Exception as e:
        print(f"An error occurred while updating player name for id: {e}")


# LOAD
def load(df: pd.DataFrame, table_name: str) -> None:
    if not df.empty:
        try:
            df["player_name"] = "default_name"
            disk_engine = create_engine(f"sqlite:///my_lite_store.db")
            df.to_sql(table_name, disk_engine, if_exists="replace", index=True)
            print(f"Data loaded into {table_name} table successfully.")
        except SQLAlchemyError as e:
            print(f"Error loading data into {table_name} table: {e}")
    else:
        print("Error: DataFrame is empty. No data to load.")


# EXECUTE
try:
    engine = create_engine("sqlite:///my_lite_store.db")
    metadata = MetaData()
    existing_table = Table("dnd_races", metadata, autoload_with=engine)
    player_name = Column("player_name", String, default="default_name")
    existing_table.append_column(player_name, replace_existing=True)
    metadata.create_all(engine)
    print(
        "Table 'dnd_races' altered successfully to include the new column with default value."
    )

    api_urls = [
        "https://www.dnd5eapi.co/api/races/gnome",
        "https://www.dnd5eapi.co/api/races/elf",
        "https://www.dnd5eapi.co/api/races/half-orc",
    ]
    data_list = extract(api_urls)
    df = transform(data_list)

    if not df.empty:
        load(df, "dnd_races")
        edit_player_name(engine, "dnd_races", 1, "Megan")
    else:
        print("Error: No data to load.")

except SQLAlchemyError as e:
    print(f"An error occurred with SQLAlchemy: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
