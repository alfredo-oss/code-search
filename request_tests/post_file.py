import requests

url = "http://127.0.0.1:8004/api/v1/code/track"
data = {
    "user": "alfred",
    "project": "code_search"
}
files = {"file": ("courseSchedule.py", open("/Users/aderodt/workspace/interview-qa/Graphs/courseSchedule.py", "rb"))}

# ✅ Send `data` directly (not inside `{"data": data}`)
response = requests.post(url, files=files, data=data)

print(response.json())
