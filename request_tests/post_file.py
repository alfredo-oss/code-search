import requests
import json
url = "http://127.0.0.1:8005/api/v1/code/track"
data = {
    "user": "alfred",
    "project": "dofus_clone",
    "filename": "alfred.py",
    "time": "",
    "content": "print(\"Hello World\")",
}

# Convert Dictionary to JSON
json_data = json.dumps(data)
# ✅ Send `data` directly (not inside `{"data": data}`)
response = requests.post(url, data=json_data)

print(response.json())
