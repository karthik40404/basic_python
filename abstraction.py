from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Bird(Animal):
    def fly(self):
        print('fly')

    def make_sound(self):
        print('bird sound')

class Cat(Animal):
    def run(self):
        print('run')

    def make_sound(self):
        print('cat sound')

b1 = Bird()
b1.fly()
b1.make_sound()

print('cat')
c = Cat()
c.run()
c.make_sound()
