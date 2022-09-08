# show first 3000 characters
# http://data.pr4e.org/romeo.txt
import socket
import re

inp = input('Enter URL: ')
host = re.findall('.+?//(.+)/.+?', inp)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((host[0], 80))
    get = f'GET {inp} HTTP/1.0\r\n\r\n'.encode()
    sock.send(get)
except IndexError:
    print('Please enter a valid URL.')
    quit()

count = 0
string = None
while True:
    data = sock.recv(512)
    if len(data) < 1:
        break
    count += len(data)
    print(data.decode(), end='')
print(count)

sock.close()
