
import requests

class APIClient:
    def __init__(self):
        self.base_url = "https://reqres.in"

    def post_data(self, endpoint: str, payload: dict):
        """Sends a POST request."""
        url = f"{self.base_url}/{endpoint}"
        print(f'url---- {url}')
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, json=payload)
        return response

    def get_data(self, endpoint: str, params: dict = None):
        """Sends a GET request."""
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        return response
