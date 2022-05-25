from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


def get_server():

    SERV_SOCK = socket(AF_INET, SOCK_STREAM)
    SERV_SOCK.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    SERV_SOCK.bind(('', 7777))
    SERV_SOCK.listen(1)

    try:
        while True:
            CLIENT_SOCK, ADDR = SERV_SOCK.accept()
            DATA = CLIENT_SOCK.recv(4096)
            if isinstance(DATA, bytes):
                print(f"Сообщение: {DATA.decode('utf-8')} было отправлено клиентом: {ADDR}")
            MSG = 'Привет, клиент'
            CLIENT_SOCK.send(MSG.encode('utf-8'))
            CLIENT_SOCK.close()
    finally:
        SERV_SOCK.close()


def get_client():

    CLIENT_SOCK = socket(AF_INET, SOCK_STREAM)
    CLIENT_SOCK.connect(('localhost', 7777))
    MSG = 'Привет, сервер'
    CLIENT_SOCK.send(MSG.encode('utf-8'))
    DATA = CLIENT_SOCK.recv(4096)
    if isinstance(DATA, bytes):
        print(f"Сообщение от сервера: {DATA.decode('utf-8')} длиной {len(DATA)} байт")
    CLIENT_SOCK.close()