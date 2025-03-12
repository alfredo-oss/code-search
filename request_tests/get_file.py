import requests
project_name = "code_search"
url = f"http://127.0.0.1:8004/api/v1/code/{project_name}"

response = requests.get(url)

print(response.json())
