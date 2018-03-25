import requests
import json

url = "https://api.tierion.com/v1/datastores"
payload = {'X-Username': 'kushal.jhunjhunwalla@gmail.com', 'X-Api-Key' : 'QKGs+DurASnHUPuR21MyiONYYR3XAtOKtOf04xYzUIA=',
            'Content-Type': 'application/json'}

def newUser():
    data = {}
    data['datastoreId'] = 7132;
    data['name'] = input("Enter name : ");
    data['groupName'] = input("Enter groupName : ");
    data_json = json.dumps(data)
    #print(data_json)
    return data_json

add_url = "https://api.tierion.com/v1/records"

dataItem = newUser()

#print("test", dataItem)

response = requests.post(add_url, data = dataItem, headers = payload);

#print(response.status_code)
#print(response.json())
