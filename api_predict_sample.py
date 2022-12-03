import requests

data_json = {"pts_5": 16.5, "stl_5": 0.3, "ft_pct_5": 87.2, "min_5": 41.7}

host = "http://127.0.0.1:8000"
url_string = host + "/predict"

"""

r = requests.get(url_string, json=data_json)

print(f"here is our output: {r}")
"""


X = [16.5, 0.3, 87.2, 41.7]
features = ["pts_5", "stl_5", "ft_pct_5", "min_5"]

url_string = (
    host
    + f"/predict?{features[0]}={X[0]}&{features[1]}={X[1]}&{features[2]}={X[2]}&{features[3]}={X[3]}"
)
r = requests.get(url_string, timeout=20)
print(r.json())
