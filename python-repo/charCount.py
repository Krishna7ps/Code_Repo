import pprint

message="This is krishna, deciple of Sri krishna"
count={}

for ch in message:
    count.setdefault(ch,0)
    count[ch]+=1
print(pprint.pformat(count))

    