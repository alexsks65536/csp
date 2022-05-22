import csv
import re

import chardet


def get_data():
    main_data = []

    with open(f'test_file.txt', 'rb') as file_main:
        data_bytes = file_main.read()
        result = chardet.detect(data_bytes)
        data = data_bytes.decode(result['encoding'])

    data_search = re.compile(r'Операционная система\s*\S*')
    main_data.append(data_search.findall(data))

    return main_data


def write_to_csv(out_file):
    main_data = get_data()
    with open(out_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in main_data:
            writer.writerow(row)


write_to_csv('test_file.csv')
