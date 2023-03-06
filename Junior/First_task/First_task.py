import requests

response = requests.get("https://reqres.in/api/users?page=2")

for i in range(0, response.json()['per_page']):
    if response.json()['data'][i]['id'] == 10:
        print(f"{response.json()['data'][i]['first_name']},{response.json()['data'][i]['last_name']}")

