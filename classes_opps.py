# Define a class
class Person:
    # Constructor (runs when a new object is created)
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute

    # Method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Base class
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

# Derived class
class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")  # call parent constructor
        self.name = name

    def make_sound(self):  # overriding method
        print(f"{self.name} says Woof!")


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())

dog1 = Dog("Buddy")
dog1.make_sound()


# Create objects (instances of the class)
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Access methods
person1.greet()
person2.greet()