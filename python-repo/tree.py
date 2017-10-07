level=int(input("enter level of tree: "))
l=0
while l<level:
    print(' '*(level//2)+'*'+'*'*(l+1)+' '*(level//2))
    l+=1
