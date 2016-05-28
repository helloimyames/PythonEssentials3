class Egg:
    def __init__(self,kind = "fried"):
        self.kind = kind

    def whatKind(self):
        return self.kind


def main():
    print("This is the syntax_self.py file")
     fried = Egg()
     scrambled = Egg('scrambled')


if __name__=="__main__": main ()
