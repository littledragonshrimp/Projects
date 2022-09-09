# read web page

import socket
import re

<<<<<<< Updated upstream
inp = input('Enter URL: ')
host = re.findall('.+//(.+)/.+', inp)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((host[0], 80))
    get = f'GET {inp} HTTP/1.0\r\n\r\n'.encode()
    sock.send(get)
except IndexError:
    print('Please enter valid URL.')
    quit()

while True:
    data = sock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

sock.close()
=======
inp = input('Input URL: ')
try:
    host = inp.split('/')
    ghost = host[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((ghost, 80))
    cmd = 'GET inp HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')

except TypeError:
    print('Please enter valid URL.')
mysock.close()
>>>>>>> Stashed changes
