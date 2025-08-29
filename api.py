import requests

base_url = "https://digi-api.com/api/v1/digimon/"

def get_digimon_info(name):
    url = base_url + name
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error in retrieving data {response.status_code}")
        return None
