class AnimalActions:
    def quack(self): return self._doAction('quack')
    def feathers(self): return self._doAction('feathers')
    def bark(self): return self._doAction('bark')
    def fur(self): return self._doAction('fur')

    def _doAction(self, action):
        if action in self.strings:
            return self.strings[action]
        else:
            return 'The {} has no {}'.format(self.animalName(), action)
    def animalName(self):
        return self.__class__.__name__.lower()

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

