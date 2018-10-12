from collections import defaultdict, namedtuple
from pprint import pprint

def letter_freequncies(sentence):
    freequencies=defaultdict(list)
    for letter in sentence:
        freequencies[letter]+=[1]
    return freequencies

Stock=namedtuple("stock","a b c d")
stock=Stock("fb",1,2,3)
pprint(stock)
if __name__=="__main__":
    pprint(letter_freequncies('This is the sentence Im passing to the function'))