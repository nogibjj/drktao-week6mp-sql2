"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

"""
import requests

def extract(url, file_path):
    """"Extract a url to a file path"""
    with requests.get(url,timeout=10) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path

