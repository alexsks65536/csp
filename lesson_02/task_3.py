"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке
ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с
помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import yaml


str_input = {
    'items': ['printer', 'computer', 'monitor'],
    'items_quantity': 10,
    'items_cost': {
        'printer': '10000€',
        'computer': '15000€',
        'monitor': '12000€'
                  }
           }

with open('file_1.yaml', 'w', encoding='utf-8') as file_1:
    yaml.dump(str_input, file_1, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open("file_1.yaml", 'r', encoding='utf-8') as file_2:
    str_output = yaml.load(file_2, Loader=yaml.SafeLoader)

print(str_input == str_output)
