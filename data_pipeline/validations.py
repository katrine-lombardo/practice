"""
Stages of Validation in ETL

1) EXTRACTION: Validate source data (completeness, accuracy, initial QC)
2) TRANSFORMATION: Validate transformation rules (validate rules, consistency
after transformation, null check)
3) LOAD: Validate target data (completeness, integrity like FKs, reconciliation)

Techniques for Data Validation in ETL: Data type, range, constraint,
consistency, uniqueness, referential integrity
"""

import requests
import json
import pandas as pd
import sqlite3
from sqlalchemy import create_engine


# EXTRACT MONSTERS
def extract() -> dict:
    API_URL = "https://api.open5e.com/monsters/?format=json"

    try:
        response = requests.get(API_URL)

        if response.status_code != 200:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return {}

        data = response.json()
        monsters = data.get("results", [])

        # VALIDATE COMPLETENESS
        def validate_completeness(monsters: dict) -> bool:
            required_fields = [
                "slug",
                "name",
                "size",
                "type",
                "armor_class",
                "hit_points",
            ]
            for monster in monsters:
                for field in required_fields:
                    if field not in monster or not monster[field]:
                        print(
                            f"Missing or empty field {field} in monster {monster.get('name', 'Unknown')}"
                        )
                        return False
            return True

        # VALIDATE ACCURACY
        def validate_accuracy(monsters: dict) -> bool:
            for monster in monsters:
                if not isinstance(monster.get("name"), str):
                    print(f"Invalid data type for name in monster {monster}")
                    return False
                if not isinstance(monster.get("armor_class"), int):
                    print(f"Invalid data type for armor_class in monster {monster}")
                    return False
                # Add more type checks and range checks as necessary
            return True

        # INITIAL QUALITY CONTROL (QC)
        def initial_quality_control(monsters: dict) -> bool:
            monster_slugs = [monster.get("slug") for monster in monsters]
            if len(monster_slugs) != len(set(monster_slugs)):
                print("Duplicate monster slugs found")
                return False
            # Add more QC checks as necessary
            return True

        # Perform validation
        if not validate_completeness(monsters):
            raise ValueError("Data failed completeness validation")
        if not validate_accuracy(monsters):
            raise ValueError("Data failed accuracy validation")
        if not initial_quality_control(monsters):
            raise ValueError("Data failed initial quality control")

        print("Data extraction and validation successful.")
        return monsters

    except requests.RequestException as e:
        print(f"An error occurred during the request: {e}")
        return {}

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return {}


# TRANSFORM MONSTER DATA
def transform(monsters: dict) -> pd.DataFrame:
    df = pd.DataFrame(monsters)
    print(f"Total Number of monsters from API {len(monsters)}")


# LOAD MONSTER DATA
def load(df: pd.DataFrame) -> None:
    disk_engine = create_engine(f"sqlite:///my_lite_store.db")
    df.to_sql("dnd_monsters", disk_engine, if_exists="replace")
    print("Data loaded to database successfully.")


# EXECUTE
data = extract()
if data:
    df = transform(data)
    load(df)
else:
    print("Data extraction failed. ETL process aborted.")
