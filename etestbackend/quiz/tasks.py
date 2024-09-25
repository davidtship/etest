from services.smsSender import SMSSender
from celery import shared_task
import time

import requests
import json


@shared_task
def sendSMS(address, message, senderAdress="+243816524437"):
    print("Entering")
    api = SMSSender()

    headers = {
        "Content-type": "application/json",
    }

    if time.time() > api.expiration_time:
        headers["Authorization"] = f"Bearer {api.get_access_token()}"
    else:
        headers["Authorization"] = f"Bearer {api.access_token}"

    data = {
        "outboundSMSMessageRequest": {
            "address": "tel:" + address,
            "senderAddress": "tel:" + senderAdress,
            "outboundSMSTextMessage": {"message": message},
        }
    }

    url = "https://api.orange.com/smsmessaging/v1/outbound/tel%3A%2B243816524437/requests?"

    r = requests.post(url, data=json.dumps(data), headers=headers)

    print(r.json())
    return r.json()
