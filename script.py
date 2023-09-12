import requests



def get_delivery_cost(order_json) -> float:
    """Подсчитывает и возвращает стоимость доставки"""

    total_weight = 0
    total_volume = 0

    order_items = order_json['rows']
    for item in order_items:
        item_url = item['assortment']['meta']['href']
        product =  requests.get(url=item_url, headers=headers).json()

        type = item['assortment']['meta']['type']
        if type == 'product':
            product_weight = product['weight']
            product_volume = product['volume']
            product_quantity = item['quantity']

            total_weight += product_quantity * product_weight
            total_volume += product_quantity * product_volume

    delivery_cost = total_weight / total_volume * 500
    return round(delivery_cost)


def add_delivery_in_order(url: str, cost: float) -> None:
    """Принимает url заказа и цену доставки. Добавляет услугу доставки в заказ"""

    service_url = 'https://online.moysklad.ru/api/remap/1.2/entity/service'
    services = requests.get(url=service_url, headers=headers).json()

    services_items = services['rows']
    for service in services_items:
        if service['name'] == 'Доставка':
            data = {'assortment': {'meta':service['meta']}, 
                    'quantity': 1,
                    'price': cost
            }
            r = requests.post(url, headers=headers, json=data)



token = f'fa134e381e8bcc9f9eb9a9375a974f7540b2986b'
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

order_id = 'd4062914-5070-11ee-0a80-0c76002c9d9c'
order_url = f'https://online.moysklad.ru/api/remap/1.2/entity/customerorder/{order_id}/positions'
order = requests.get(url=order_url, headers=headers).json()

delivery_cost = get_delivery_cost(order)
add_delivery_in_order(order_url, delivery_cost)
