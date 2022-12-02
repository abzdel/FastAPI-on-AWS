import json
import requests

data_json = {
    "PTS_5": 16.5,
    "stl_5": 0.3,
    "ft_pct_5": 87.2,
    "min_5": 41.7
}

host = "http://127.0.0.1:8000"
url_string = host + '/predict'

"""

r = requests.get(url_string, json=data_json)

print(f"here is our output: {r}")
"""


X = [16.5, 0.3, 87.2, 41.7]

url_string = host + f'/predict?f0={X[0]}&f1={X[1]}&f2={X[2]}&f3={X[3]}'
r = requests.get(url_string)
print(r.json())