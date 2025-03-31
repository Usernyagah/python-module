# Base Class
class Superhero:
    def __init__(self, name, alias, power_level):
        self.name = name
        self._alias = alias  # Encapsulated attribute
        self.power_level = power_level

    def introduce(self):
        print(f"I'm {self.name} ({self._alias}), Power Level: {self.power_level}")

    def use_power(self):
        print(f"{self.name} uses a generic superpower!")

    # Encapsulation example
    def get_secret_identity(self):
        return self._alias

    def set_secret_identity(self, new_alias):
        print("Secret identity updated!")
        self._alias = new_alias

# Inherited Class
class TechHero(Superhero):
    def __init__(self, name, alias, power_level, gadget):
        super().__init__(name, alias, power_level)
        self.gadget = gadget

    # Polymorphism - overriding method
    def use_power(self):
        print(f"{self.name} deploys {self.gadget}!")
        self.power_level -= 5

# Inherited Class
class Mutant(Superhero):
    def __init__(self, name, alias, power_level, mutation):
        super().__init__(name, alias, power_level)
        self.mutation = mutation

    # Polymorphism - different implementation
    def use_power(self):
        print(f"{self.name} activates {self.mutation} ability!")
        self.power_level += 2  # Mutants recover energy

# Usage Example
iron_man = TechHero("Tony Stark", "Iron Man", 95, "Repulsor Rays")
wolverine = Mutant("Logan", "Wolverine", 85, "Healing Factor")

heroes = [iron_man, wolverine]
for hero in heroes:
    hero.introduce()
    hero.use_power()
    print(f"Current power: {hero.power_level}\n")



