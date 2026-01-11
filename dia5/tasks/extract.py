from prefect import task
import requests

@task
def extract():
    """
    extraer data de randomuser
    """
    URL = "https://randomuser.me/api/?results=10"
    response = requests.get(URL)
    
    extract_data = []
    if response.status_code == 200:
        extract_data = response.json()['results']
    return extract_data