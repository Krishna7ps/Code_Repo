import random

num=int(input("enter a number"))
done=False
while not done:
    if num%2==0:
        num=num//2
        print(num)
        if num==1:
            done=True 
    elif num%2==1:
        num=3*num+1
        print(num)
        if num==1:
            done=True
