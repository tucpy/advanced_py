import abc
class Animal:
    #
    __metaclass__ = abc.ABCMeta
    @classmethod
    @abc.abstractclassmethod
    
    def Shout(self):
        return ""

class Cat(Animal):
    def Shout(self):
        return "Meow meow ..."
class Dog(Animal):
    def Shout(self):
        return "Bow wow ..."
class Elephant(Animal):
    def Shout(self):
        return "Aum aum ..."

a_cat = Cat()
a_dog = Dog()
an_elephant = Elephant()
zoo = [a_cat, a_dog, an_elephant]
for animal in zoo:
    print(animal.Shout())