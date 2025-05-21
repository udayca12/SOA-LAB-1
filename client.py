import requests
import json

BASE_URL = 'http://localhost:5001'

def get_products():
    response = requests.get(f'{BASE_URL}/products')
    print(f"GET /products: {response.status_code}")
    print(response.json())

def add_product(name, price):
    data = {'name': name, 'price': price}
    response = requests.post(
        f'{BASE_URL}/products',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(data)
    )
    print(f"POST /products: {response.status_code}")
    print(response.json())

def delete_product(product_id):
    response = requests.delete(f'{BASE_URL}/products/{product_id}')
    print(f"DELETE /products/{product_id}: {response.status_code}")
    print(response.json())

# Template for PUT (update) if you add it in your Flask app
def update_product(product_id, name=None, price=None):
    data = {}
    if name:
        data['name'] = name
    if price:
        data['price'] = price
    response = requests.put(
        f'{BASE_URL}/products/{product_id}',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(data)
    )
    print(f"PUT /products/{product_id}: {response.status_code}")
    print(response.json())

if __name__ == '__main__':
    print("Testing Product Service Client")
    print("==============================")

    # 1. Get all products
    get_products()

    # 2. Add a new product
    add_product('Sample Product', 19.99)

    # 3. Get all products again to see the new product
    get_products()

    # 4. Delete the product with ID 1 (change as needed)
    delete_product(1)

    # 5. Get all products again to confirm deletion
    get_products()

    # 6. (Optional) Update a product if you implement PUT in Flask
    # update_product(2, name='Updated Name', price=29.99)
