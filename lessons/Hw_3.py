from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name, lvl, health, strength):
        self.name = name
        self.lvl = lvl
        self.__health = health
        self.strength = strength

    def greet(self):
        return f"Привет, я {self.name}, мой уровень {self.lvl}"

    def rest(self):
        self.__health += 1
        return f"{self.name} отдыхает"

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):
    def attack(self):
        return "Воин атакует мечом"


class Mage(Hero):
    def attack(self):
        return "Маг использует магию"


class Assassin(Hero):
    def attack(self):
        return "Ассасин атакует из-под тишка"


warrior = Warrior("Mikasa", 24, 6, 5)
mage = Mage("Eren", 56, 6, 3)
assassin = Assassin("Armin", 90, 12, 34)


warrior.greet()
warrior.attack()
warrior.rest()
mage.greet()
mage.attack()
mage.rest()
assassin.greet()
assassin.attack()
assassin.rest()