
"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом,
а не ручном режиме, с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя методы
encode, decode или функцию bytes) и определить тип, содержимое и длину соответствующих переменных.
"""


str_1 = ['class', 'function', 'method']

for i in str_1:
    s = eval(f"b'{i}'")
    print(s, type(s))
    print('length of world:', len(i))


