# urllib ver of exercise 12.2
import urllib.request

url = 'http://data.pr4e.org/romeo.txt'
data = urllib.request.urlopen(url).read().decode().strip()

print(data[:3000])
print(len(data))
