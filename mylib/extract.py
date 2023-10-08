"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""
import requests

def extract(url, file_path):
    """"Extract a url to a file path"""
    with requests.get(url,timeout=10) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path

extract('https://raw.githubusercontent.com/fivethirtyeight/data/master/terrorism/eu_terrorism_fatalities_by_country.csv',
        'data/fatalities_by_country.csv')
extract('https://raw.githubusercontent.com/fivethirtyeight/data/master/terrorism/eu_terrorism_fatalities_by_year.csv',
        'data/fatalities_by_year.csv')