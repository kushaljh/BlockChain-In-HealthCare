import requests

url = "https://api.tierion.com/v1/datastores"
payload = {'X-Username': 'kushal.jhunjhunwalla@gmail.com', 'X-Api-Key' : 'QKGs+DurASnHUPuR21MyiONYYR3XAtOKtOf04xYzUIA=', 'Content-Type': 'application/json'}


response = requests.get(url, headers = payload)

print(response.status_code)
print(response.content)
