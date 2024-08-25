import requests

def fetch_figma_data(figma_token, figma_file_id):
  url = f"https://api.figma.com/v1/files/{figma_file_id}"
  headers = {"X-Figma-Token": figma_token}

  response = requests.get(url, headers=headers)
  return response.json()
