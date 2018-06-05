def nameis(namesend):
    name= namesend
name="sabaris"
def welcome():
    print("welcome to python functions",name)

def outer():
    #test=0
    def inner():
        #test=1
        print("inner: ",test)
    
    inner()
    print("outer: ",test)

test=2
outer()
print("global: ",test)