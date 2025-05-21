import requests

url = "http://localhost:5001/products"
data = {
    "name": "Apple",
    "price": 1.99
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
