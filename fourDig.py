num=eval(input("Please enter a number"))
if num<0:
    print(0000)
if num>9999:
    print(9999)
if 10000>num>999:
    print(num)
if 1000>num>99:
    print('[',0,sep='',end='')
    print(num,end='] \n')
if -1<num<100:
    print('[',0,0,num,sep='',end='] \n')