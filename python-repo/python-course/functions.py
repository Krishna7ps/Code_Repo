def f():
    def g():
        print("This is function g..", __name__)
        print()
    print("This is function ", __name__)
    g()


def h(x):
    print("This is function parameter")
    print("parameter is ",x.__name__)
    x()

h(f)