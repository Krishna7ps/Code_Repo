till=int(input("enter size of table(min 1): "))

for i in range(1,till+1):
    if i==1:
        while i<=till:
            print(i,end='    ')
            i+=1
        print("+"+('---'*till*2))
    print("{0:2}{1}".format(i,"|"),end=' ')
    for j in range(1,till+1):
        print("{0:4}".format(i*j),end=' ')
    print()
    

