# client.py

import requests

# r = requests.get("http://127.0.0.1:5000/info")
r = requests.get("http://127.0.0.1:5000/add/2/3")
print(r.status_code)
print(r.text)