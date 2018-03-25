import requests
import json

payload = {'X-Username': 'kushal.jhunjhunwalla@gmail.com', 'X-Api-Key' : 'QKGs+DurASnHUPuR21MyiONYYR3XAtOKtOf04xYzUIA=',
            'Content-Type': 'application/json'}

def getRecord(id):
        url = "https://api.tierion.com/v1/records/" + str(id)
        response = requests.get(url, headers = payload)

        dict2 = json.loads(json.loads(response.content)['json'])
        #print(dict2)
        return dict2

#getRecord("x6Iru4hRsU6C3Xgmb_2oow");