"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
 и выполнить обратное преобразование (используя методы encode и decode).
"""


str_1 = ['разработка', 'администрирование', 'protocol', 'standard']
str_3 = []

for i in str_1:
    str_2 = i.encode('utf-8')
    print(f"result of encode: {str_2}")
    str_3.append(str_2)

print('#' * 60)

for i in str_3:
    str_4 = i.decode('utf-8')
    print(f"result of decode: {str_4}")