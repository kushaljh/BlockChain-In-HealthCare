import requests
import json

payload = {'X-Username': 'kushal.jhunjhunwalla@gmail.com', 'X-Api-Key' : 'QKGs+DurASnHUPuR21MyiONYYR3XAtOKtOf04xYzUIA=',
            'Content-Type': 'application/json'}

def newUser(name, email, number, drug, dose):
    data = {}
    data['datastoreId'] = 7132
    data['Full Name'] = name
    data['Email'] = email
    data['Phone Number'] = number
    data['Prescription'] = drug
    data['Dosage'] = dose
    data_json = json.dumps(data)
    add_url = "https://api.tierion.com/v1/records"
    requests.post(add_url, data = data_json, headers = payload)
