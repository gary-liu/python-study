import urllib
from urllib.request import urlopen

data1 = urllib.request.urlopen("http://www.baidu.com").read()
print(data1)

data2 = urlopen("http://www.baidu.com").read()
print(len(data2))


