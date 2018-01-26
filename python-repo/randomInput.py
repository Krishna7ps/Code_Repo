import random

rng=random.Random()
guess=''
while True:
    number=rng.randrange(1,10)
    guess=int(input("Guess A number :"))
    if guess==number:
        print("Hurrey")
    else:
        print("number is ",number)
