import requests
import json

payload = {'X-Username': 'kushal.jhunjhunwalla@gmail.com', 'X-Api-Key' : 'QKGs+DurASnHUPuR21MyiONYYR3XAtOKtOf04xYzUIA=',
            'Content-Type': 'application/json'}

def newUser():
    data = {}
    data['datastoreId'] = 7132;
    data['Full Name'] = input("Enter name: ");
    data['Email'] = input("Enter email: ");
    data['Phone Number'] = input("Enter phone number: ");
    data['Prescription'] = input("Enter drug name: ");
    data['Dosage'] = input("Enter dosage: ");
    data_json = json.dumps(data)
    return data_json

add_url = "https://api.tierion.com/v1/records"

dataItem = newUser()

response = requests.post(add_url, data = dataItem, headers = payload);
