"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать
скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""


import json


def write_order_to_json(item: str, quantity: str, price: str, buyer: str, date: str) -> None:

    with open('orders_1.json', 'r', encoding='utf-8') as file_out:
        data = json.load(file_out)

    with open('orders_1.json', 'w', encoding='utf-8') as file_in:
        input_list = data['orders']
        input_info = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        input_list.append(input_info)
        json.dump(data, file_in, indent=4)

write_order_to_json('mfu', '6', '18500', 'Semenov A.C.', '19.12.2021')
write_order_to_json('videodeck', '2', '1500', 'Warshavsky D.O.', '19.11.2021')
write_order_to_json('computer', '3', '28500', 'Turovsky A.L.', '18.12.2021')
