# # Статический метод (@staticmethod)
# Используется, когда методу не нужны ни self, ни cls.
 # Обычная функция, но логически относящаяся к классу.

class Math:
    @staticmethod
     def add():
     return 12 + 12
obj_1 = Math()
print(Math.add(12, 12))

# 2. Метод класса (@classmethod)

# Получает доступ к самому классу через cls.
# Используется для альтернативных конструкторов или работы с классом.

class Bank:
     # Атрибута класса
     bank_name = "Mbank"

     def __init__(self, sum, user):
         # Атрибута экземпляра\объекта класса
         self.__sum = sum
         self.user = user

     def get_sum(self):
        return self.__sum

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

ardager = Bank(123456, "ardager")
arzy = Bank(123, "arzy")

print(arzy.get_sum())
print(ardager.get_sum())


# 3. Декоратор @property
# Описание:
# Декоратор @property используется для того, чтобы метод стал доступным как атрибут, но при этом оставался методом.
# Это позволяет скрывать логику вычислений или проверки, делая код более чистым. Обычно используется
# для создания геттеров и сеттеров.


class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            return print("Не может быть меньше нуля!!")
        self.__price = value
        return print("OK!!")

first_product = Product(100)

print(first_product.price)
first_product.price = 11
print(first_product.price)

class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 100
        self.bonus = 100

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"



ardager1 = User("Ardadger", "Kartanbekov")

ardager1.full_name

# 1. Что такое декоратор?
# Декоратор — это функция, которая принимает другую функцию как аргумент и
# возвращает новую функцию, обычно обернутую в дополнительную функциональность.
# может добавить логику до выполнения принятой функции и полсле выполнения
def simple_decorator(func):
    def wrapper():
        print("До выполнения!!")
        func()
        print("После выполнения!!")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello")

say_hello()


def greeting_decorator(func):
    def wrapper(name):
        print(f"Привет {name} !!")
        func(name)
    return wrapper

@greeting_decorator
def greeting(name):
   print(f'Как дела {name}?')

greeting("Ardager")


def repeat_decorator(count):
    def decorator(func):
        def wrapper(name):
            for i in range(count):
                print(f"{i+1} раз!!! \n")
                print(f"Привет {name}!!")
                func(name)
        return wrapper
    return decorator

@repeat_decorator(5)
def greeting(name):
    print(f'Как дела {name}?')

greeting("Ardager")


# Разница между декоратором с параметрами и без в их вложености
# декоратор с параметрами имеет двойную влоденность
# а без параметра одну


def class_decorator(cls):
    class NewClass(cls):
        def method(self):
            print("New method!!")
    return NewClass

@class_decorator
class OldClass:
    def method(self):
        print("Old method!!")


obj_1 = OldClass()

print(type(obj_1))


def is_admin(func):
    def wrapper(user):
        if user.role == "admin":
            func()
        return print("Вы не админ")
    return wrapper

@is_admin
def send_msg(user):
    print(f'{user.name} msg!!')

def retry(func):
    def wrapper():
        data = func()
        if data.status == "OK":
            return print('OK!!')
        else:
            func()
    return wrapper


test = 123
