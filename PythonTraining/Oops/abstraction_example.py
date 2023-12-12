from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        return f"{self.name} says speak!"
        pass

    @abstractmethod
    def normal(self):
        return f"{self.name} says normal!"
        pass


class Dog(Animal, ABC):
    def speak(self):
        return f"{self.name} says woof!"

    def normal(self):
        pass


class Cat(Animal, ABC):
    def speak(self):
        return f"{self.name} says Meow!"

    def normal(self):
        pass


if __name__ == "__main__":
    dog = Dog('Jimmy')
    cat = Cat('Ruby')
    # animal = Animal("Bob")

    print(dog.speak())
    print(cat.speak())
    # print(animal.speak())
