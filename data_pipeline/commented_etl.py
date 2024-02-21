"""
Python Extract Transform Load Example
"""

# Import the right libraries
import requests
import pandas as pd
from sqlalchemy import create_engine


# EXTRACT
def extract() -> dict:
    API_URL = "http://universities.hipolabs.com/search?country=United+States"
    data = requests.get(API_URL).json()
    return data


# TRANSFORM
def transform(data: dict) -> pd.DataFrame:
    df = pd.DataFrame(data)
    print(f"Total Number of universities from API {len(data)}")
    # Filter by name column containing "California"
    df = df[df["name"].str.contains("California")]  # DF is like a csv with a memory
    print(f"Number of universities in California: {len(df)}")
    # Convert the data to be in the right format: From list of domains to string
    # separated comma
    df["domains"] = [",".join(map(str, l)) for l in df["domains"]]
    df["web_pages"] = [",".join(map(str, l)) for l in df["web_pages"]]
    # Drop the index because we're just doing a filter
    df = df.reset_index(drop=True)
    # Only returning the desired columns we want to store
    return df[["domains", "country", "web_pages", "name"]]


# LOAD
# Create a SQLite database which exists in a database, and saving the
# dataframe into a table.
def load(df: pd.DataFrame) -> None:
    # Load data into a SQLite database
    disk_engine = create_engine("sqlite:///my_lite_store.db")
    # Put into the table cal_uni and replace data if it already exists
    df.to_sql("cal_uni", disk_engine, if_exists="replace")


# EXECUTE
# Get the data out of extract, get it in a json format
data = extract()
# Pass in the data to turn into json
df = transform(data)
# Load it into the sql db
load(df)
