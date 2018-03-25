import requests
import json

payload = {'X-Username': 'kushal.jhunjhunwalla@gmail.com', 'X-Api-Key' : 'QKGs+DurASnHUPuR21MyiONYYR3XAtOKtOf04xYzUIA=',
            'Content-Type': 'application/json'}

def getRecord(id):
        url = "https://api.tierion.com/v1/records/x6Iru4hRsU6C3Xgmb_2oow"# + str(id)
        response = requests.get(url, headers = payload)
        print(response.content.json)
        return response.content

getRecord(11);