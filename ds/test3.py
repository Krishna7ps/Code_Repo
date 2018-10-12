class C1:
    def display(self):
        print("From C1 class: ",self.name)

class C2(C1):
    def shout():
        # self.name=input("Enter name for C2: ")
        print("it's c2")

class C3(C1):
    def shout():
        # self.name=input("Enter name for C3: ")
        print("it's c3")

C3.shout()
C2.shout()

