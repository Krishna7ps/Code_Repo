import random

nick_name=['bujji', 'bangaru', 'chinnari', 'Renu', 'bujjikonda', 'bangarukonda', 'kanna']
apology=['sorry', 'manninchu', 'thappaindi', 'Badha pettanu, baaga chusukunta']

fd=open(r"apology.txt",'w')
for i in range(1001):
    name=random.choice(nick_name)
    apo=random.choice(apology)
    msg=random.choice([[i+1,name,apo]])
    for j in range(len(msg)):
        fd.write(str(msg[j])+' ')
    fd.write('\n')
    print()
fd.close()


