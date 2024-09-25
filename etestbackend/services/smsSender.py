import requests
from datetime import datetime
import time
import json


class SMSSender:
    headers = {
        "Authorization": "Basic RG5rVmpaYkdWeXJwamZjVEhjd0RUR1VOZnM2YUZDQW06YlBaWTNaWVRhN08xQWpjag==",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }

    url = "https://api.orange.com/oauth/v3/token"

    access_token = None
    data = {"grant_type": "client_credentials"}
    expire_in = None
    expiration_time = None

    def __init__(self) -> None:
        try:
            self.access_token = self.get_access_token()
            if self.access_token is None:
                raise Exception("Request for access token failed")

        except Exception as e:
            print(e)

        else:
            self.expiration_time = time.time() + self.expire_in

    def get_access_token(self):
        try:
            r = requests.post(self.url, data=self.data, headers=self.headers)
            r.raise_for_status()

        except Exception as e:
            print(e)

        else:
            access_token = r.json()["access_token"]
            self.expire_in = r.json()["expires_in"]

        return access_token
