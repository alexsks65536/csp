"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
 Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед нами файл в неизвестной
 кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.
"""


from chardet import detect

str_1 = ['сетевое программирование', 'сокет', 'декоратор']

with open('../test_file.txt', 'w') as file:
    for foo in str_1:
        file.write(f'{foo}\n')
file.close()

with open('../test_file.txt', 'rb') as file:
    bar = file.read()
bar_code = detect(bar)['encoding']
print(bar_code)

with open('../test_file.txt', 'r', encoding=bar_code) as file:
    bar = file.read()
print(bar)
