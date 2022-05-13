progr_1 = 'Программирование'
print(progr_1)

print(type(progr_1))

progr_2 = 'Programování'
print(progr_2)

unic_s_1 = "\N{LATIN SMALL LETTER C WITH DOT ABOVE}"
print(unic_s_1)

unic_s_2 = "\u010B"
print(unic_s_2)

progr_3 = 'Программа'
progr_4 = '\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'
print(progr_4)
print(progr_3 == progr_4)
print(len(progr_4))

print(ord('ã'))
print(chr(227))

bytes_s_1 = b'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'
bytes_s_2 = b"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430"
bytes_s_3 = b'''\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'''
print(type(bytes_s_1))
bytes_s_4 = b'Program'
print(bytes_s_4)
print(len(bytes_s_4))

# bytes_s_5 = b'Программа'
# print(bytes_s_5)

"""Конвертация байтов и строк"""

enc_str = 'Кодировка'
enc_str_bytes = enc_str.encode('utf-8')
print(enc_str_bytes)

dec_str_bytes = b'\xd0\x9a\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb0'
dec_str = dec_str_bytes.decode('utf-8')
print(dec_str)

"""также для класса str"""

str_1 = 'Программа'
str_1_enc = str.encode(str_1, encoding='utf-8')
print(str_1_enc)

bytes_1 = b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb0'
bytes_1_enc = bytes.decode(bytes_1, encoding='utf-8')
print(bytes_1_enc)

"""Примеры конвертации байтов и строк
        Модуль subprocess"""

import chardet  # необходимо инсталлировать pip install chardet
import subprocess
import platform

param = '-n' if platform.system().lower() == 'windows' else '-c'
args = ['ping', param, '3', 'google.com']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    result = chardet.detect(line)
    print('result = ', result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
