import random

number=random.randint(1,21)
count=1
guessed=False

while not guessed:
    print("Please enter your guess between 1 to 20")
    print()
    guess=int(input())
    if guess==number:
        print("well done, you guessed it in ",count,"counts",sep=' ')
        print()
        guessed=True
    elif guess<number:
        count+=1
        print("Guess is low")
        continue
    elif guess>number:
        count+=1
        print("Guess is high")

    
    