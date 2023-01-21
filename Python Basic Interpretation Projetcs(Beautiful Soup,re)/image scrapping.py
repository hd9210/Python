import requests,re
import bs4
url='https://app.cpcbccr.com/AQI_India/'
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text,'lxml')
lst2=[]
lst = soup.select('img')
for i in lst:
    lst2.append(i['src'])

for i in lst2:
    res= requests.get(f'{url}'+i)
    f = open('myjpg.png','wb')
    f.write(res.content)
    f.close()