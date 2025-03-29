import requests

class RequestsDriver():
    @staticmethod
    def get(url: str, headers: str) -> requests.Response:
        return requests.get(url, headers=headers)
    
    @staticmethod
    def validate_response(response: requests.Response) -> None:
        response.raise_for_status()
