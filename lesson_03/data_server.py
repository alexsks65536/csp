"""
1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
клиент отправляет запрос серверу;
сервер отвечает соответствующим кодом результата. Клиент и сервер должны быть реализованы в виде отдельных скриптов,
содержащих соответствующие функции. Функции клиента: сформировать presence-сообщение; отправить сообщение серверу;
получить ответ сервера; разобрать сообщение сервера; параметры командной строки скрипта client.py <addr> [<port>]:
addr — ip-адрес сервера; port — tcp-порт на сервере, по умолчанию 7777.
Функции сервера: принимает сообщение клиента; формирует ответ клиенту; отправляет ответ клиенту;
имеет параметры командной строки: -p <port> — TCP-порт для работы (по умолчанию использует 7777);
-a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
"""

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

SERV_SOCK = socket(AF_INET, SOCK_STREAM)
SERV_SOCK.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
SERV_SOCK.bind(('', 7777))
SERV_SOCK.listen(1)

try:
    while True:
        CLIENT_SOCK, ADDR = SERV_SOCK.accept()
        DATA = CLIENT_SOCK.recv(4096)
        print(f"Сообщение: {DATA.decode('utf-8')} было отправлено клиентом: {ADDR}")
        MSG = 'Привет, клиент'
        CLIENT_SOCK.send(MSG.encode('utf-8'))
        CLIENT_SOCK.close()
finally:
    SERV_SOCK.close()