# #
# # class User:
# #     pass
# # peter = User()
# # peter.name = "Petja Robinsov"
# # peter.age = 36
# #
# # julia = User()
# # julia.name = "Julia Donaldos"
# # julia.age = 89
# # julia.height = 189
# #
# # print(peter.name, peter.age)
# # print(julia.name, julia.height)
# #
# # class Car:
# #     number_of_wheels = 4
# #     motor = True
# #     frame = True
# #     passengers = 5
# # vw_passat = Car()
# # print(vw_passat.motor, vw_passat.frame, vw_passat.passengers)
# # vw_golf = Car()
# # print(vw_golf.motor, vw_golf.number_of_wheels)
# #
# #
# # class Car:
# #     def __init__(self, number_of_wheels, motor, frame, passengers):
# #         self.rr = motor
# #         self.number_of_wheels = number_of_wheels
# #         self.frame = frame
# #         self.passengers = passengers
# #
# # vw_passat = Car(number_of_wheels=4, motor=True, frame=True, passengers=5)
# # print(vw_passat.number_of_wheels, vw_passat.passengers, vw_passat.rr)
#
# # class Product:
# #     def __init__(self, name, category, quantity, vol):
# #         self.name = name
# #         self.category = category
# #         self.quantity = quantity
# #         self.vol = vol
# #
# #     def is_available(self):
# #         return True if self.quantity > 4 else False
# #
# # double_bock = Product(name="Double bock", category="beer", quantity=5, vol="8%")
# # print(double_bock.quantity, double_bock.vol)
# # print(double_bock.is_available())
#
# # class Event:
# #     def __init__(self, timestamp=0, event_type="", session_id=""):
# #         self.timestamp = timestamp
# #         self.event_type = event_type
# #         self.session_id = session_id
# #
# # events = [
# #     {
# #      "timestamp": 1554583508000,
# #      "type": "itemViewEvent",
# #      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
# #     },
# #     {
# #      "timestamp": 1555296337000,
# #      "type": "itemViewEvent",
# #      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
# #     },
# #     {
# #      "timestamp": 1549461608000,
# #      "type": "itemBuyEvent",
# #      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
# #     },
# # ]
# #
# # for event in events:
# #     event_obj = Event(timestamp=event.get("timestamp"),
# #                       event_type=event.get("type"),
# #                       session_id=event.get("session_id"))
# #     print(event_obj.timestamp)
#
# # class Human:
# #     def __init__(self, age, height, legs):
# #         self.age = age
# #         self.height = height
# #         self.legs = legs
# # Vasja = Human(age=45, height=154, legs=3)
# # Petja = Human(age=25, height=198, legs=5)
# # print(Vasja.legs)
# # print(Petja.height)
#
# # class Human:
# #     age = None
# #     def __init__(self, age=4):
# #         self.age = age
# #     def get_age(self):
# #         return self.age
# #     def set_age(self, age):
# #         if age > 0 and isinstance(age, int):
# #             self.age = age
# # h = Human()
# # h.set_age(15)
# # print(h.get_age())
#
# # class Point:
# #     def __init__(self, x=0, y=0):
# #         self.__x = x
# #         self.__y = y
# #
# #     def setter(self, x, y):
# #         self.__x = x
# #         self.__y = y
# #
# #     def getter(self):
# #         return self.__x, self.__y
# #
# # pt = Point(1, 2)
# # pt.setter(5,4)
# # print(pt.getter())
#
#
# # print(pt.__x, pt.__y)
#
# # import datetime
# # class Product:
# #     max_quantity =1000
# #     def __init__(self, name, category, quantity):
# #         self.name = name
# #         self.category = category
# #         self.quantity = quantity
# #     def is_available(self):
# #         return True if self.quantity > 0 else False
# #     def in_gategory(self):
# #         return True if self.category == "food" else False
# # class Food(Product):
# #     is_critical = True
# #     needs_to_be_refreshed = True
# #     refresh_frequency = datetime.timedelta(days=1)
# # eggs = Food(name="eggs", category="food", quantity=5)
# # fish = Food(name="fish", category="food", quantity=24)
# # class Fruits(Product):
# #     is_tropical = True
# #     in_pcs = 10
# #     in_kgs = 1
# # bananas = Fruits(name="banana", category="food", quantity=1002)
# # cucumbers = Fruits(name="cucumbers", category="food", quantity=42)
# #
# # if __name__ == "__main__":
# #     print(bananas.quantity)
# #     print(fish.name)
# #     print(isinstance("foo", str))
# #     print(isinstance(bananas, Fruits))
# # class Point:
# #     def __init__(self, x=0, y=0):
# #         self.__x = x
# #         self.__y = y
# #
# #     def get_x(self):
# #         return self.__x
# #
# #     def get_y(self):
# #         return self.__y
# #
# # if __name__ == "__main__":
# #     # This code will only run if the script is executed directly, not if it's imported as a module
# #     pt = Point(1, 2)
# #     print(pt.get_x())  # Prints 1
# #     print(pt.get_y())  # Prints 2
#
# # class Rectangle:
# #     def __init__(self, length, width):
# #         self.length = length
# #         self.width = width
# #
# #     def calculate_area(self):
# #         return self.length * self.width
# #
# # if __name__ == "__main__":
# #     # This code will only run if the script is executed directly, not if it's imported as a module
# #     length = float(input("Enter the length of the rectangle: "))
# #     width = float(input("Enter the width of the rectangle: "))
# #
# #     rectangle = Rectangle(length, width)
# #     area = rectangle.calculate_area()
# #
# #     print(f"The area of the rectangle is: {area}")
#
# # class Room1:
# #     def get_room(self):
# #         print('room1')
# #
# #
# # class Room2:
# #     def get_room(self):
# #         print('room2')
# #
# #     def get_room2(self):
# #         print('room2 for flat')
# #
# #
# # class Kitchen:
#
#
# # class Room:
# #     def get_room(self):
# #         print('room')
# #
# #
# # class Room1(Room):
# #     def get_room(self):
# #         print('room1')
# #
# #
# # class Room2(Room):
# #     def get_room(self):
# #         print('room2')
# #
# #
# # class Flat(Room1, Room2):
# #     ...
# #
# #
# # print(Flat.mro())  # метод класса, который показывает порядок наследования
# #
# # f = Flat()
# # f.get_room()
#
# # class Rectangle:
# #     def __init__(self, width, height):
# #         self.width = width
# #         self.height = height
# #
# #     def get_width(self):
# #         return self.width
# #     def get_height(self):
# #         return self.height
# #     def get_area(self):
# #         return self.width * self.height
#
# # class Cat:
# #     def __init__(self, name, sex, age):
# #         self.name = name
# #         self.sex = sex
# #         self.age = age
# #     def get_name(self):
# #         return self.name
# #     def get_sex(self):
# #         return self.sex
# #     def get_age(self):
# #         return self.age
# # class Dot:
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y
# #     def __eq__(self, other):
# #         return self.x==other.x and self.y==other.y
# #     def __str__(self):
# #         return f"Dot: {self.x, self.y}"
# # p1 = Dot(1,2)
# # p2 = Dot(1,2)
# # print(p1 == p2)
# # print(str(p1))
# # print(p2)
# # /-------------------------------------------------
# # class Rectangle:
# #     def __init__(self, a, b):
# #         self.a = a
# #         self.b = b
# #     def __eq__(self, other):
# #         return self.a==other.a and self.b==other.b
# #     def get_area_rectangle(self):
# #         return self.a * self.b
# # class Square:
# #     def __init__(self,a):
# #         self.a = a
# #     def get_area_square(self):
# #         return self.a ** 2
# # class Circle:
# #     def __init__(self, r):
# #         self.r = r
# #     def get_area_circle(self):
# #         return (self.r ** 2) * 3.14
# #
#
# # class Rectangle:
# #     def __init__(self, x, y, width, height):
# #         self.x = x
# #         self.y = y
# #         self.width = width
# #         self.height = height
# #     def get_x_coord(self):
# #         return self.x
# #     def get_y_coord(self):
# #         return self.y
# #     def get_width(self):
# #         return self.width
# #     def get_height(self):
# #         return self.height
# #     def get_area(self):
# #         return self.height * self.width
# #     def __str__(self):
# #         return f"Rectangle: {self.x}, {self.y}, {self.width}, {self.height}"
# # rect = Rectangle(5, 10, 50, 100)
# #
# # print(rect)
# # print("Ploshad figuty: ", rect.get_area(), "cm2")
# # -------------------------------------------------------------------
# # class Customer:
# #     def __init__(self, name, surname, city, balance):
# #         self.name = name
# #         self.surname = surname
# #         self.city = city
# #         self.balance = balance
# #     def __str__(self):
# #         return f"{self.name} {self.surname}. {self.city}. Balance: {self.balance} USD"
# #     def customer_info(self):
# #         return f"{self.name} {self.surname}. {self.city}. Balance: {self.balance} USD"
# #     def get_guest(self):
# #         return f"{self.name} {self.surname}. {self.city}"
# # customer1 = Customer("Ivan", "Petrov", "Moscow", 50)
# # customer2 = Customer("Homus", "Teingo", "Boku", 684)
# # customer3 = Customer("Gofu", "Boli", "Uhogu", 985)
# # customer4 = Customer("Losi", "Colih", "Nofiid", 89)
# # customer5 = Customer("Seruy", "Wolgi", "Trovi", 45)
# #
# # print(customer1.get_guest())
# # print(customer3)
# # guest_list = [customer4, customer5, customer1]
# # for guest in guest_list:
# #     print(guest.get_guest())
# # ------------------------------------------------------------------------------
# # class StaticClass:
# #     @staticmethod
# #     def bar():
# #         print("bar")
# # StaticClass.bar()
# #
# # class SelfClass:
# #     def __init__(self, text):
# #         self.text = text
# #     def textprint(self):
# #         return self.text
# # textobject = SelfClass("bar")
# # print(textobject.textprint())
#
# # class MethodsComparison:
# #     def __init__(self, text):
# #         self.text = text
# #
# #     def instance_method(self):
# #         return f"Instance method: {self.text}"
# #
# #     @staticmethod
# #     def static_method(text):
# #         return f"Static method: {text}"
# #
# # # Creating an instance of MethodsComparison
# # obj = MethodsComparison("bar")
# #
# # # Using the instance method
# # result_instance = obj.instance_method()
# # print(result_instance)
# #
# # # Using the static method
# # result_static = MethodsComparison.static_method("foo")
# # print(result_static)
#
# # class SquareFactory:
# #     @staticmethod
# #     def square_side(a):
# #         print(a)
# # SquareFactory.square_side(5)
#
# # class Square:
# #     def __init__(self, side):
# #         self.side = side
# # class SquareFactory:
# #     @staticmethod
# #     def create_square(side):
# #         return Square(side)
# # sq1 = SquareFactory.create_square(1)
# # print(sq1.side)
#
# # class Dog:
# #     _happiness = 10
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #     @property
# #     def human_age(self):
# #         return self.age * 7.3
# #     @property
# #     def happiness(self):
# #         return self._happiness
# #     @happiness.setter
# #     def happiness(self, value):
# #         if value <= 100 and value >= 0:
# #             self._happiness = value
# #         else:
# #             raise ValueError("Happiness must be between 0 ... 100")
# # jane = Dog("Jane", 8)
# # jane.happiness = 100
# # print(jane.happiness)
#
# # class Sqare:
# #     def __init__(self, side):
# #         self._side = side
# #     @property
# #     def Square_area(self):
# #         return self._side ** 2
# #     @property
# #     def Side_value(self):
# #         return self._side
# #     @Side_value.setter
# #     def Side_value(self, value):
# #         if value > 0:
# #             self.side = value
# #         else:
# #             raise ValueError("The side length must be positive")
# #
# # sq1 = Sqare(5)
# # sq2 = Sqare(7)
# # print(sq1.Square_area)
# # print(sq1.Side_value)
# # print("Перед исключением")
# # c = 1 / 0  # Здесь что-то не так….
# # print("После исключения")
#
# # try:
# #     a = int(input("a: "))
# #     b = int(input("b: "))
# #     c = a / b
# #     print("poluchaetsja: ", c)
# #
# # except ZeroDivisionError as d:
# #     print(d)
# # else:
# #     print("vse nichtjak")
# # finally:
# #     print("togda poh")
#
# # try:
# #     age = int(input("skolko te let??? :"))
# #     if age > 100 or age < 0:
# #         raise ValueError("no goni")
# #     print(f"Tebe {age} let")
# # except ValueError:
# #     print("Nepravilnyj vozrast")
#
#
# # try:
# #     inp = int(input("Vvedite chislo: "))
# #     print(f"Вы ввели {inp}")
# # except ValueError:
# #     print("Вы ввели неправильное число")
# # finally:
# #     print("Выход из программы")
#
# # class TwoLevelList:
# #     def __init__(self, rows, cols):
# #         # Initialize the two-level list with zeros
# #         self.data = [[0] * cols for _ in range(rows)]
# #
# #     def set_value(self, row, col, value):
# #         # Set a value at a specific position
# #         self.data[row][col] = value
# #
# #     def get_value(self, row, col):
# #         # Get the value at a specific position
# #         return self.data[row][col]
# #
# #     def display(self):
# #         # Display the two-level list
# #         for row in self.data:
# #             for element in row:
# #                 print(element, end=' ')
# #             print()
# #
# # # Example usage:
# # two_level_list = TwoLevelList(rows=3, cols=4)
# #
# # # Set values
# # two_level_list.set_value(0, 0, 1)
# # two_level_list.set_value(1, 2, 5)
# # two_level_list.set_value(2, 3, 9)
# #
# # # Display the two-level list
# # two_level_list.display()
#
# # Get value
# # value = two_level_list.get_value(1, 2)
# # print(f"Value at position (1, 2): {value}")
#
# # try:
# #     raise ZeroDivisionError
# # except ArithmeticError:
# #     print("Hello from arithmetic error")
#
# # raise ZeroDivisionError
# # raise ArithmeticError
#
# # class Point:
# #     color = "red"
# #     circle = 2
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y
# #
# #     def set_coords(self, x, y):
# #         self.x = x
# #         self.y = y
# #     def get_coords(self):
# #         return (self.x, self.y)
# # pt = Point(1, 2)
# # pt2 = Point(4, 9)
# #
# # pt.set_coords(58,45)
# # print(str(pt.get_coords()))
# # print(", ".join(map(str, pt.get_coords())))
#
# # class Point:
# #     def __new__(cls, *args, **kwargs):
# #         print("vyzov __new dlja" + str(cls))
# #         return super().__new__(cls)
# #
# #     def __init__(self, x=0, y=0):
# #         print("vyzov __init dlja" + str(self))
# #         self.x = x
# #         self.y = y
# # pt = Point(1, 2)
#
# # class Vector:
# #     min_coord = 0
# #     max_coord = 100
# #
# #     @classmethod
# #     def validate(cls, arg):
# #         return cls.min_coord <= arg <= cls.max_coord
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y
# #
# #     def get_coord(self):
# #         return self.x, self.y
# #
# #     @staticmethod
# #     def norm2(x, y):
# #         return x*x + y*y
# #
# # v = Vector(5, 7)
# # print(v.get_coord())
# # print(v.norm2(20,30))
#
# # class Point:
# #     def __init__(self, x=0, y=0):
# #         self.__x = x
# #         self.__y = y
# #     @classmethod
# #     def __check_value(cls, x):
# #         return type(x) in (int, float)
# #     def set_coord(self, x, y):
# #         if self.__check_value(x) and self.__check_value(y):
# #             self.__x = x
# #             self.__y = y
# #         else:
# #             ValueError("Coords must be numbers")
# #
# #     def get_coord(self):
# #         return self.__x, self.__y
# #
# # pt = Point(5,7)
# # pt.set_coord(20,50)
# # print(pt.get_coord())
#
# # class Point:
# #     color = "red"
# #     circle = 2
# #     MAX_COORD = 104
# #     MIN_COORD = 0
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y
# #
# #     def set_coords(self, x, y):
# #         if self.MIN_COORD <= x <= self.MAX_COORD:
# #             self.x = x
# #             self.y = y
# #     def get_coords(self):
# #         return (self.x, self.y)
# #
# #
# # pt1 = Point(50, 2)
# # pt2 = Point(4, 9)
# #
# #
# # print(pt1.get_coords())
# # print(pt2.get_coords())
#
# class Person:
#     def __init__(self, name = "", old = 0):
#         self.__name = name
#         self.__old = old
#     def set_name(self, name):
#         self.__name = name
#     def set_old(self, old):
#         self.__old = old
#     def get_old(self):
#         return self.__old
#     def get_name(self):
#         return self.__name
#     old = property(get_old, set_old)
#     name = property(get_name, set_name)
# pr = Person("Vasja", 38)
# pr2 = Person("Goga", 45)
#
# pr.old = 98
# print(pr.old)
#

# try:
#     print("yeheee iskljuchenie1")
#     print("yeheee iskljuchenie2")
#     print("yeheee iskljuchenie3")
#     print(a)
#     print("yeheee iskljuchenie4")
#     print("yeheee iskljuchenie5")
#     print("yeheee iskljuchenie6")
#     print("yeheee iskljuchenie7")
# except:
#     print("...nevernaja komanda...")
#
# try:
#     y = int(input())
#     print(y)
# except ValueError:
#     print("neee")

# try:
#     y, x, d = map(int,input().split())
#     print(y, x, d)
#     res = x / d
# except ValueError as h:
#     print(h)
# except ArithmeticError as h:
#     print(h)
# else:
#     print("no errors sir")
# finally:
#     print("game over")

# class MyException(Exception):
#     pass
# try:
#     y, x, d = map(int, input().split())
#     print(y, x, d)
#     res = x / d
#     raise MyException("Message")
# except MyException as e:
#     print(e)

# class MyException(Exception):  # создаём пустой класс – исключения
#     pass
# try:
#     b=7
#     c=9
#     a = b + c
#     print(a)
#     raise MyException("message")  # поднимаем наше исключение
# except MyException as e:  # ловим его за хвост как шкодливого котёнка
#     print(e)  # выводим информацию об исключении

# class NonePositiveDigitException(ValueError):
#     pass
# class Sqaure():
#     def __init__(self, a=0, b=0):
#         self.a = a
#         self.b = b
#     def square_area(self, a, b):
#         if a <= 0 or b <= 0:
#             raise NonePositiveDigitException("Nepravilnaja storona kvadrata")
#         return a * b
# sq = Sqaure()
# print(sq.square_area(8, 5))
# import math
# print(math.trunc(math.fmod(math.fabs(-10000000), 55)+0.3))
import time
print(help(time))