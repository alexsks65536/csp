"""
5. Написать код, который выполняет пинг веб-ресурсов yandex.ru, youtube.com и преобразовывает результат из
байтовового типа данных в строковый без ошибок для любой кодировки операционной системы.
"""


import subprocess

import chardet

sites = ['youtube.com', 'yandex.ru']

for site in sites:
    site_ping = subprocess.Popen(('ping', site), stdout=subprocess.PIPE)
    
    for foo, bar in enumerate(site_ping.stdout):
        request = chardet.detect(bar)
        bar = bar.decode(request['encoding']).encode('utf-8')
        if foo < 5:
            print(bar.decode('utf-8'))
        else:
            site_ping.kill()

