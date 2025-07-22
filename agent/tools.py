# agent/tools.py: أدوات للقراءة من Excel أو API
import os
import pandas as pd
import requests

def get_products():
    source = os.environ.get("DATA_SOURCE", "excel")  # excel أو api
    if source == "excel":
        df = pd.read_excel("data.xlsx")
        return df.to_dict(orient="records")
    elif source == "api":
        url = os.environ.get("API_URL")
        response = requests.get(url)
        return response.json()
    else:
        raise ValueError("Unknown data source") 