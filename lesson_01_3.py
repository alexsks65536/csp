"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
"""


str_1 = ['attribute', 'класс', 'функция', 'type']

for i in str_1:
    try:
        str_2 = f"b'{i}'"
        eval(str_2)
    except SyntaxError:
        print(f'The word "{i}" cannot be represented as a byte string')
