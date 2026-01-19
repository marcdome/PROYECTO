import requests
import pandas as pd
import json

url  = "https://api.adzuna.com/v1/api/jobs/es/search/1"
APP_ID = "99936c6b"
API_KEY = "5b5d7a3ac709455f1022920b276dccf7"
params = {
    "app_id": APP_ID,
    "app_key": API_KEY,
    "what": "python",
    "content-type": "application/json"
}
response = requests.get(url, params=params)
print(response.status_code)
print(json.dumps(response.json()))

