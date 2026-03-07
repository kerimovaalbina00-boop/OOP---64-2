
class Hero:

    # Конструктор класса
    def __init__(self, name, lvl, health, strength ):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.health = health
        self.strength = strength

    # Метод класса
    def greet(self):
        return f"Привет, я {self.name}, мой уровень {self.lvl}"

    def attack(self):
        self.strength -= 1
        return f"{self.name} наносит удар!"


    def rest(self):
        self.health += 1
        return f"{self.name} отдыхает"


class Warrior(Hero):
    def __init__(self, name, lvl, health, strength, stamina): #stamina - выносливость
        super().__init__(name, lvl,health, strength)
        self.stamina = stamina

    def attack(self):
        return f"{self.name} атакует мечом!"


class Mage(Hero):
    def __init__(self, name, lvl, health, strength, mana):
        super().__init__(name, lvl, health, strength)
        self.mana = mana

    def attack(self):
        return f"{self.name} кастует заклинание !"

class Assassin(Hero):
    def __init__(self, name, lvl, health, strength, stealth):  #stealth — скрытность
        super().__init__(name, lvl, health, strength)
        self.stealth = stealth

    def attack(self):
        return f"{self.name} атакует из-под тишка !"

warrior = Warrior("Mikasa", 8, 100, 20, 50)
mage = Mage("Eren", 5, 80, 15, 100)
assassin = Assassin("Armin", 6, 70, 25, 90)

warrior.greet()
warrior.attack()

mage.greet()
mage.attack()

assassin.greet()
assassin.attack()

print(warrior.rest())
print(mage.rest())
print(assassin.rest())
print(warrior.attack())
print(mage.rest())
print(assassin.attack())

import random
heroes = [warrior, mage, assassin]
choices = {
    'Warrior': 'Камень',
    'Mage': 'Бумага',
    'Assassin': 'Ножницы'
}
player = random.choice(heroes)
bot = random.choice(heroes)

print("Ты выбрал:", player.__class__.__name__, choices[player.__class__.__name__])
print("Бот выбрал:", bot.__class__.__name__, choices[bot.__class__.__name__])

if player.__class__ == bot.__class__:
    print("Ничья!")
elif (
    (choices[player.__class__.__name__] == "Камень" and choices[bot.__class__.__name__] == "Ножницы") or
    (choices[player.__class__.__name__] == "Ножницы" and choices[bot.__class__.__name__] == "Бумага") or
    (choices[player.__class__.__name__] == "Бумага" and choices[bot.__class__.__name__] == "Камень")
):
    print("Ты победил!")
else:
    print("Бот победил!")