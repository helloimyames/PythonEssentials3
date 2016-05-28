class AnimalActions:
    def quack(self): return self.strings['quack']
    def feathers(self): return self.strings['feathers']
    def bark(self): return self.strings['bark']
    def fur(self): return self.strings['fur']

class Duck(AnimalActions):
    strings = dict(
            quack = "quackkk!",
            feathers = "the duck has grey and white feathers",
            bark = "the duck cannot bark",
            fur = "the duck has no fur"
            )

class Person(AnimalActions):
    strings = dict(
            quack = " the person imitates a quackkk!",
            feathers = "the person takes a feather from the ground",
            bark = "the person barks",
            fur = "the person has no fur"
            )

def in_the_forest(duck):
    print(duck.quack)
    print(duck.feathers)

def main():
    donald = Duck()
    john = Person()
    john.quack()

    print("in the forest")
    for o in (donald, john):
        in_the_forest(o)
        print("in for loop")

if __name__ == "__main__": main()

