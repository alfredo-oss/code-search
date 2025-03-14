import requests
file_name = "xloc.py"
url = f"http://127.0.0.1:8003/api/v1/code/track/{file_name}"

response = requests.get(url)

print(response.json())