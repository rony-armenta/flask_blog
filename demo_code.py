from abc import ABC, abstractmethod

# 1. ABSTRACTION: We use an "Abstract Base Class" (ABC).
# It acts as a strict template. You can't create a generic "Animal" object;
# you must create a specific type like Dog or Cat.


class Animal(ABC):
    def __init__(self, name):
        self.name = name          # Public Variable
        self.__hunger = 50        # 2. ENCAPSULATION: Double underscore makes it "Private"

    @abstractmethod
    def make_sound(self):
        # This is a method that HAS to be implemented by child classes
        pass

    def feed(self, food_amount):
        self.__hunger -= food_amount
        print(f"{self.name} was fed. Hunger level is now hidden and protected.")

# 3. INHERITANCE: Dog "is-an" Animal. It gets 'name' and 'feed' for free.


class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"      # 4. POLYMORPHISM: Dog's version of the sound

# 3. INHERITANCE: Cat "is-an" Animal.


class Cat(Animal):
    def make_sound(self):
        return "Meow..."          # 4. POLYMORPHISM: Cat's version of the sound


# --- EXECUTION ---
my_zoo = [Dog("Buddy"), Cat("Luna")]

for animal in my_zoo:
    # This is Polymorphism in action:
    # One command (make_sound), two different results.
    print(f"{animal.name} says: {animal.make_sound()}")
