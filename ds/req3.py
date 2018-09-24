import requests
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/w/index.php'+'?title=List_of_Game_of_Thrones_episodes&oldid=802553687'

r=requests.get(url)
html=r.text
ht=BeautifulSoup(html)
eptab=ht.findAll('table',class_='wikiepisodetable')

for t in eptab:
    header=[]
    values=[]
    rows=t.find_all('tr')
    for i in rows[0].find_all(['th']):
        header.append(i.text)
    print(len(rows))
    for h in rows[1:]:
        values=[]
        for i in h.find_all(['th','td']):
            values.append(i.text)
        if values:
            epi_dict={header[i]:values[i] for i in range(len(values))}
            print(epi_dict['No.overall'],'---->',epi_dict['Title']) 
    print()
         