import urllib3
import builtwith
from bs4 import BeautifulSoup
http=urllib3.PoolManager()
r=http.request('GET','https://authoraditiagarwal.com/')
data1=BeautifulSoup(r.data,'lxml')
print(data1.title)
print(data1.title.text)

Tech=builtwith.parse('https://www.tutorialspoint.com/')
print(Tech)