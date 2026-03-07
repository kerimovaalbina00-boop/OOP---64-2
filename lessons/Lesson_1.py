# MageHero
# mage_hero

# Родительский\Супер класс
# class Hero:
#
#     # Конструктор класса
#     def __init__(self, name, lvl=1, hp=100):
#         # Атрибуты класса
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp
#
#     # Метод класса
#     def action(self):
#         print(f"{self.name} base action!!")
#
#     # Принт
#     def __str__(self):
#         return self.name
#
# # Экземпляр\Объектом на основе класса
# kirito = Hero("Kirito")
# asuna = Hero("Asuna")
# kirito.action()
#
#
# # Дочерний класс
# class MageHero(Hero):
#
#     def cast_spell(self):
#         print(f"{self.name} cass fire!!")
#
# gendalf = MageHero("Gendalf")


# gendalf.cast_spell()
# asuna.action()


#ДЗ№1

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
        return f"{self.name} наносит удар!"
        self.strength -= 1

    def rest(self):
        return f"{self.name} отдыхает"
        self.health += 1

# Экземпляр\Объектом на основе класса
Mikasa= Hero("Mikasa", 5, 100, 5)
Eren = Hero("Eren", 6,90,4)
print(Mikasa.rest())
print(Eren.rest())


