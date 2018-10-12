def no_return():
    print("This is first line in no_return")
    raise Exception("This is always raised")
    print("never ever")

def call_return():
    print("Call return started here")
    no_return()
    print("end")

call_return()