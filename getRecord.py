import requests
import json

payload = {'X-Username': 'kushal.jhunjhunwalla@gmail.com', 'X-Api-Key' : 'QKGs+DurASnHUPuR21MyiONYYR3XAtOKtOf04xYzUIA=',
            'Content-Type': 'application/json'}

#print(response.status_code)
#print(response.json())

def getRecord(id):
        url = "https://api.tierion.com/v1/records/" + str(id)
        print(url)
        response = requests.get(url, headers = payload)
        print(response.status_code)
        print(response.content)

getItem = input("Enter Prescription ID: ")

getRecord(getItem)
