import json
import time

jfile=open("data-text.json",'r').readlines()

for i in jfile:
    print(json.load(i))
# print(jfile)
# data=json.loads(jfile)

# for d in data:
    # print(d)
    # time.sleep(10)
