import requests
import json

payload = {'X-Username': 'kushal.jhunjhunwalla@gmail.com', 'X-Api-Key' : 'QKGs+DurASnHUPuR21MyiONYYR3XAtOKtOf04xYzUIA=',
            'Content-Type': 'application/json'}

#print(response.status_code)
#print(response.json())

def deleteRecord(id):
        url = "https://api.tierion.com/v1/records/" + str(id)
        print(url)
        response = requests.delete(url, headers = payload)
        #print(response.status_code)
        #print(response.content)

delItem = input("Enter Prescription ID: ")

deleteRecord(delItem)
