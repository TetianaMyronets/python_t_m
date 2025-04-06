# if 1 > 0:
#     print('Hello')
#
# if True:
#     print('Hello world!')
#
# def my_func():
#     return False
#
# if my_func():
#     print('Hello my friend!')
#     value = 1

# value = 1 < 0
# if value:
#     print('Hello')
# else:
#     print('Bay')

# x = 1
# while x != 10:
#     print('Hello!')
#     if x == 5:
#         break
#     x += 1


# for integer in range(1, 10):
#     print(integer)
#     if integer == 2:
#         break

# Home Work
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)
#
# for i in range(5):
#     print(i)
#     if i == 2:
#         continue

# numbers = [-5, 3, -1, 7, -2, 10]
# for i in numbers:
#     if i >= 0:
#         print(i)

# numbers = [3, 10, 7, 8, 15, 22, 31]
# for i in numbers:
#     if i % 2 == 0:
#         print(i,'- парне число')
#     else:
#         print(i,'- непарне число')

# n = int(input("Введіть число від 0 до 250: "))
# m = n // 60
# f = n % 60
# print('Число', n,'- це', m, 'хвилин', f, 'секунд')

# text = ['Python is Awesome']
# vowel = ['a', 'e', 'i', 'o', 'u']
# x = 0
# for i in list(text[0]):
#    if i.lower() in vowel:
#        x = x + 1
# print(x)

# def printing_number():
#     number = input("Enter number please: ")
#     print(number)
#
# printing_number()

# def fullname(name ='Serhii'):
#     full_name = name + 'Mykolayovich'
#     return fullname
#
# print(fullname('Serhii'))

# def arguments(**kwargs):
#     print(kwargs)
#     print(type)
#
# arguments(name = 'arg1', surname = 'arg2', age = 21)

# def multiple(*args):
#     for argument in args:
#         print(argument**2)
#
# multiple(12, 34, 54)

# def dictionary(**kwards):
#     print(type(kwards))
# dictionary(name = 'Alex')

# class Student:
#     high = 25
#
#     def full_name_creation(self, name, fullname = 'Mykolayovich'):
#         print(type(name))
#         new_name = name + fullname
#         return new_name
#
#     def adding_age(self, fullname, age):
#         return fullname, age

# my_parametr = 'My string y: 21'
# second_parametr = 'is'

# print(len(my_parametr))
# print(my_parametr[3:9])
# print(my_parametr[0:13:2]) #2 - step
# print(my_parametr[::-1])
# print(my_parametr[13:4:-3])
# print(my_parametr.split('string'))
# print(my_parametr.split('y'))

# second = my_parametr.join(second_parametr)
# print(second)

# my_parametr = '21'
# second_parametr = ['Alex', 'Olga', 'Igor']
# second = my_parametr.join(second_parametr)
# print(second)

# def shorten_next(text, n):
#     if len(text) > n:
#         return "ERROR"
#     return text[:n] + '...' if len(text) > n else text
#
# shorten_next("The table is broken", 20)

# my_string = "my age is 21"
# some = 'Hello'
# print(my_string.join(some))

# my_string = "My age is 21"
# some = ['Hello', 'Hi', 'By']
# print(' ', my_string.join(some))
#
# my_string = "My age is 21"
# some = '43'
# print('my age is 55'.replace('55','23'))

# my_string = "my age is 21"
# some = '43'
# print(my_string.upper().replace('21', some))

# my_string = "my age is 21"
# some = '43'
# print(f"There is an example: {my_string}")
#
# my_string = "my age is 21"
# some = [43, 32, 'Hello']
# print(f"There is an example: {some}")

# my_string = "my %s age %s 21"
# some = 43
# one = 'ages'
# print(my_string % (one,some))

# my_string = "my {} is {}"
# some = 43
# one = 'age'
# print(my_string.format(one, some))

# def test_function ("I'm from main")

# import math
# print(math.sqrt(64))
#
# import random
# print(random.choice(['Alex', 'Mykola']))

# some = [1, 2, 'letter']
# # some = list()
# print(type(some))
# print(some)

# some = (1, 2, 'letter')
# # some = tuple()
# print(type(some))
# print(some)

# some = {1, 2, 'letter'}
# # some = set()
# print(type(some))
# print(some)
#
# some = {} #dict
# print(type(some))
# print(some)

# s = 'helicopter'
# my_list = list(s)
# my_list[2] = 34
# print(my_list)

# my_list = ['Hello', [1, 4.6, 'hi'], 5, {'i'}]
# my_list.append(['o', 'p', 23.0, 'r'])
#
# print(my_list)

# my_list = ['Hello', [1, 4.6, 'hi'], 5, {'i'}]
# my_list.insert(1, 'n')
#
# print(my_list)

# my_list = ['Hello', 'n', [1, 4.6, 'hi'], 5, {'i'}]
# my_list.pop(1)
#
# print(my_list)

# def sorting_for_my_lis():
#     for i in my_list:
#         return i if i == 'r' else []
#
# my_list = ['Hello', 'r', [1, 4.6, 'hi'], 5, {'i'}]
# sorted_list = my_list.sort(sorting_for_my_list)
#
# print()

# dict_1 = {
#     3456: 1,
#     False: 'some'
# }
#
# dict_2 = {
#     34: 1,
#     True: 'some'
# }

# def sorting_for_my_list(element):
#     return len(element)
# some = lambda x: x * 2
# print(some(5))

# def sorting_for_my_list(element):
#     return len(element)
# some = lambda: 25 * 25
# print(some())

# def decorator_example(func):
#     def inner_function():
#         print("Code before function")
#         some = func()
#         print(f"code after {some}")
#     return inner_function
#
#
# @decorator_example
# def my_function():
#     print('Hello')
#     return 2**2
#
#
# my_function()

# class Auto:
#     wheels = 4
#     true_color = 'green'
#
#     def __init__(self, brand, color, wheel_radius):
#         self.brand = brand
#         self.color = color
#         self.wheel_radius = wheel_radius
#
#     def run(self):
#         print(f"I'm running {self.brand}")
#
#     @staticmethod
#     def drift():
#         print('Whoohooo!')
#
#     @classmethod
#     def painting(cls, color):
#         cls.true_color = color
#         print("My color is", cls.true_color)
#
#
# my_car = Auto(brand = 'ford', color = 'red', wheel_radius = 25)
# my_car.run()
#
# print(type(my_car))
# print(my_car.wheels)
# print(my_car.run())
# my_car.drift()
# Auto.painting('yellow')
# my_car.painting('blue')
# print(Auto.true_color)


# class Auto:
#     wheels = 4
#     true_color = 'green'
#
# class Vehicle:
#     engine = True
#
# class Bike(Vehicle, Auto):
#
#     def wear_helmet(self):
#         pass
#
# rover = Bike()
# my_car = Vehicle()
#
# print(my_car.engine)
# print(rover.wheels)
#
# print(Bike.mro())

# class Motobike:
#     _engine = True
#
# new_moto = Motobike
# print(new_moto._engine)
#
# class Car:
#     def __init__(self, model):
#         self.model = model
#
#     @property
#     def model(self):
#         return  self.__model
#
#     @model.setter
#     def model(self, model):
#         self.__model = model
#
#     @model.getter
#     def model(self):
#         return self.__model
#
# my_car = Car('BMW')
# my_car.model = 'Ford'
# print(my_car.model)

# def start_car(self):
#     print((f'start {self.model}'))
#
# class BMW(Car):
#     def start_car(self):
#         new_model = 3 ** 2
#         print(new_model)
#
# new3_object = Car('x6')

# # PAYMENT METHOD
#
# from abc import ABC, abstractmethod
#
#
# class PaymentSystem(ABC):
#
#
#     @abstractmethod
#     def pay(self, amount):
#         pass
#
# class PayPal(PaymentSystem):
#
#     def pay(self, amount):
#         print(f"I paid with PayPal this amount {amount}")
#
# class GooglePay(PaymentSystem):
#
#     def pay(self, amount):
#         print(f"I paid with GooglePay this amount {amount}")
#
# def payment(payment_system, amount):
#         payment_system.pay(amount)
#
# payment(GooglePay(),1000)
# payment(PayPal(), 2000)

# Exeptions

# my_list = [1, 2, 0, 6]
# for i in my_list:
#     try:
#         result = 12 / i
#         print(result)
#     except ZeroDivisionError:
#         print("Don't do that. i = 0!!!")
#     except TypeError:
#         print('FFFF')
#     else:
#         print("Yohooo!")
#     finally:
#         print("I will be forever")


# my_list = [1, 2, 0, 6]
# for i in my_list:
#     try:
#         result = 12 / i
#         print(i)
#     except ZeroDivisionError:
#         print("Don't do that. i = 0!!!")
#         raise ZeroDivisionError
#
# class TooYoungError(Exception):
#     pass
#01
# age = 20
#
# if age < 21:
#     f = 21 - age
#     raise TooYoungError("Too young. Wait {f} more years")

my_list = [1, 2, 0, 6]
try:
    result = my_list[4]
    print(result)
except IndexError:
    print("Don't do this")