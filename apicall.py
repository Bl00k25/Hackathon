import time

import requests
import json
import mysql.connector as msql
import random


def token():
    url = "https://openapiuat.airtel.africa/auth/oauth2/token"

    payload = json.dumps({
        "client_id": "2601f408-027d-4dc5-a538-f995bf4ee17d",
        "client_secret": "a353ed73-c3cf-4c97-8135-13f4a1976cc1",
        "grant_type": "client_credentials"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    jsonData = response.json()
    return jsonData


class BuyThing:
    def __init__(self, id):
        db = msql.connect(database="hackathon_db", user="root", passwd="", host="localhost")
        dbcur = db.cursor()
        query = "select name,price from game where id = %d"
        value = id
        dbcur.execute(query, value)
        res = dbcur.fetchone()
        name = res[0]
        price = res[1]
        id = random.randint(7895132132, 1378546512348465162455)
        access_token = token()['access_token']
        # Define the API endpoint and parameters
        url = "https://openapiuat.airtel.africa/merchant/v1/payments/"
        payload = json.dumps({
            "reference": "Achat de " + name,
            "transaction": {
                "amount": "" + price,
                "country": "MG",
                "currency": "MGA",
                "id": "" + id
            },
            "subscriber": {
                "country": "MG",
                "currency": "MGA",
                "msisdn": 333005842
            }
        })
        headers = {
            'X-Country': 'MG',
            'X-Currency': 'MGA',
            'Accept': '*/*',
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json'
        }

        # Send the API request
        response = requests.post(url, headers=headers, data=payload)

        # Parse the API response
        data = json.loads(response.text)
        print(data)

        time.sleep(20)

        url = "https://openapiuat.airtel.africa/standard/v1/payments/"+id+"/"

        payload = {}
        headers = {
            'X-Country': 'MG',
            'X-Currency': 'MGA',
            'Authorization': 'Bearer ' + access_token
        }
