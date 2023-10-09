"""
Transforms and Loads data into Databricks
"""
import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv

def load(ds1="data/eu_terrorism_fatalities_by_country.csv", ds2="data/eu_terrorism_fatalities_by_year.csv"):
    df1 = pd.read_csv(ds1, delimiter=",")
    df2 = pd.read_csv(ds2, delimiter=",")
    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS CountryFatalitiesDB (
                iyear int,
                Belgium int,
                Denmark int,
                France int,
                Germany int,
                Greece int,
                Ireland int,
                Italy int,
                Luxembourg int,
                Netherlands int,
                Portugal int,
                Spain int,
                UK int
            )
        """
        )
        for _, row in df1.iterrows():
            convert = (_,) + tuple(row)
            c.execute(f"INSERT INTO CountryFatalitiesDB VALUES {convert}")

        c.execute(
            """
            CREATE TABLE IF NOT EXISTS YearFatalitiesDB (
                iyear int,
                fatalities int
            )
            """
        )
        for _, row in df2.iterrows():
            convert = (_,) + tuple(row)
            c.execute(f"INSERT INTO YearFatalitiesDB VALUES {convert}")
    c.close()
    return "Success"
