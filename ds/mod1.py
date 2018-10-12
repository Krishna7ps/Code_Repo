class Welcome:
    def welcome(self):
        print("welcome")

# print("This is in the mod1 module")

def main():
    print("Will this be in run first?")
    w=Welcome()
    print(w.welcome())

if __name__=="__main__":
    main()


