from mylib.extract import extract
from mylib.query import complex_query
from mylib.transform_load import load

print("Extracting data...")
extract(
    "https://raw.githubusercontent.com/fivethirtyeight/data/master/terrorism/eu_terrorism_fatalities_by_country.csv",
    "data/fatalities_by_country.csv",
)
extract(
    "https://raw.githubusercontent.com/fivethirtyeight/data/master/terrorism/eu_terrorism_fatalities_by_year.csv",
    "data/fatalities_by_year.csv",
)

print("Loading data...")
load()

print("Querying data...")
complex_query()
