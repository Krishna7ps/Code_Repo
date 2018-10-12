from csv import reader
import pprint

data=reader(open('mn.csv','r'))
header=reader(open('mn_headers.csv','r'))

# print(data)

data_row=[d for d in data]
header_row=[r for r in header]
print(type(data_row),type(header_row))
pprint.pprint(len(data_row))
pprint.pprint(len(header_row))

x=[9,1,2,3,4,5,5,6,6,7,0]
y=[12,12,11212,21,12,12121,121,121,2,1,2]

for i in zip(x,y):
    print(i)
for i in enumerate(x):
    print(i)