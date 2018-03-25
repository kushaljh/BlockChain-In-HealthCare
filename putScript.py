import requests
import json

url = "https://api.tierion.com/v1/datastores"
payload = {'X-Username': 'kushal.jhunjhunwalla@gmail.com', 'X-Api-Key' : 'QKGs+DurASnHUPuR21MyiONYYR3XAtOKtOf04xYzUIA=', 
            'Content-Type': 'application/x-www-form-urlencoded'}

def newUser():
    data = {}
    data['datastoreId'] = 7132;
    data['name'] = input("Enter name : ");
    data['groupName'] = input("Enter groupName : ");
    #redirectEnabled = input("Enter redirectEnabled : ")
    #redirectUrl = input("Enter redirectUrl : ")
    #emailNotificationEnabled = input("Enter emailNotificationEnabled : ")
    #emailNotificationAddress = input("Enter emailNotificationAddress : ")
    #postDataEnabled = input("Enter postDataEnabled : ")
    #postDataUrl = input("Enter postDataUrl : ")
    #postReceiptEnabled = input("Enter postReceiptEnabled : ")
    #postReceiptUrl = input("Enter postReceiptUrl : ")
    data_json = json.dumps(data)
    print(data_json)
    return data_json

add_url = "https://api.tierion.com/v1/records"

response = requests.post(add_url, json = newUser(), headers = payload, params = {'datastoreId' : 7132});

print(response.status_code)
print(response.json())
