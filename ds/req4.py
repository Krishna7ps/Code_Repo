import requests
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/w/index.php'+'?title=List_of_Game_of_Thrones_episodes&oldid=802553687'
r=BeautifulSoup(requests.get(url).text)
#print(r)

links=r.find_all('a',children='href')
for i in links:
    print()
    print()