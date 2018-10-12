from collections import Counter

response=[
    'vanilla',
    'vanilla',
    'vanilla',
    'vanilla',
    'chacolate',
    'chacolate',
    'chacolate',
    'chacolate',
    'chacolate',
    'chacolate',
    'chacolate',
    'biscuit',
    'biscuit',
    'biscuit',
    'biscuit',
    'chatni'
]

# print([i[0] for i in Counter(response).most_common(3)])

class SillyInt(int):
    def __add__(self,num):
        return 0

a=SillyInt(1)
b=SillyInt(2)
print(a+b)
print(dir(int))