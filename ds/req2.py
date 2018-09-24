import requests

def calc(a,b,op):
    url='http://www.webscrapingfordatascience.com/calchttp/'
    params={'a':a,'b':b,'op':op}
    r=requests.get(url,params=params)
    return r.text

print(calc(6,5,'*'))
print(calc(4,2,'+'))

import requests
url = 'https://en.wikipedia.org/w/index.php' + '?title=List_of_Game_of_Thrones_episodes&oldid=802553687'
r = requests.get(url) 
print(r.text)
body