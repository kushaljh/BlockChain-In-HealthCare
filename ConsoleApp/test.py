import requests
import json

url = "https://api.tierion.com/v1/datastores"
payload = {'X-Username': 'kushal.jhunjhunwalla@gmail.com',
            'X-Api-Key' : 'QKGs+DurASnHUPuR21MyiONYYR3XAtOKtOf04xYzUIA=',
            'Content-Type': 'application/json'}


response = requests.get(url, headers = payload)

print(response.status_code)
print(response.content)

record_url = "https://api.tierion.com/v1/records?datastoreId=7132"
response = requests.get(record_url, headers = payload)
data = response.content #
#data1 = json.loads(response.content, indent=4,separators=(',', ':'))


print("get : ", response.status_code)
print("get : ", data)
