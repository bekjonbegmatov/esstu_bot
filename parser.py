import requests
from bs4 import BeautifulSoup

url = 'https://portal.esstu.ru/bakalavriat/45.htm'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml' )

arr = []
for text in soup.find_all('tr'):
    temp_arr = []
    for rez in text.find_all('td'):
        rez = rez.get_text()
        rez = rez.encode("latin-1").decode('cp1251')
        temp_arr.append(rez)
    arr.append(temp_arr)

print(arr)

