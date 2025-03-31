# Base Class
class Animal:
    def move(self):
        pass

# Inherited Classes
class Fish(Animal):
    def move(self):
        print("Gliding through water 🐟")

class Bird(Animal):
    def move(self):
        print("Soaring through the air 🦅")

class Kangaroo(Animal):
    def move(self):
        print("Hopping across the land 🦘")

# Vehicle Base Class
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Cruising on the road 🚗")

class Helicopter(Vehicle):
    def move(self):
        print("Rotating blades take flight 🚁")

class Submarine(Vehicle):
    def move(self):
        print("Diving deep underwater 🛳️")

# Demonstration
def travel_system(entity):
    entity.move()

# Create instances
nemo = Fish()
eagle = Bird()
roo = Kangaroo()
sedan = Car()
chopper = Helicopter()
nautilus = Submarine()

# Test polymorphism
for traveler in [nemo, eagle, roo, sedan, chopper, nautilus]:
    travel_system(traveler)
