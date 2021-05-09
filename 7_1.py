class Cat:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Bark")

my_cat = Cat("Murzik")
my_dog = Dog("Barsik")

animals = [my_cat, my_dog]

for animal in animals:
    animal.make_sound()  #в зависимости от класс animal будет вызываться нужный make_sound
    