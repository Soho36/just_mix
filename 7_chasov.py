# import os
# site = input()
# if "https://" in site:
#     os.system("start " + site)
#     print("if")
#
# elif "www." in site:
#     site = "https://" + site
#     os.system("start " + site)
#     print("elif")
#
# else:
#     site = "https://www." + site
#     os.system("start " + site)
#     print("else")

# while True:
#     x = int(input("vvedite chislo: "))
#     print(list(range(1, x + 1)))
#     count = 0
#     y = 1
#     while count < x:
#         count += 1
#         print("Current count: ", count)
#         y = y * count
#         print("Current Y: ", y)
#     print(y)

# x = ""
# while len(x) < 5:
#     y = input("Vvod dannyh: ")
#     if y == "o":
#         continue
#     if y == "stop":
#         break
#     x += y
# else:
#     print(x)
# print("Stopped")

# m = "stroka tekst"
# for i in m:
#     if i == "k":
#         continue
#     print(i)
# else:
#     print("sykl zavershen")

# x = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
# x2 = x.replace(", ", "").lower()
# print(x2)
# y = input("Vvedite stroku: ")
# for i in x2:
#     count = 0
#     for r in y:
#         if i == r:
#             count += 1
#     if count > 0:
#         print(i, count)

# for i in alfavit2:

# x = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
# xreplaced = x.replace(", ", "").lower()
# listx = list(xreplaced)
# print(listx)
# listx.append("hui")
# print(listx)
# listx[10] = ["ja", "molodec", "kanechka"]
# print(listx)
# listx[10].append("thoh")
# print(listx)
# listx[0], listx[1] = listx[1], listx[0]
# print(listx)


# n = list(range(1, 11))
# print(n)
#
# n.insert(2, 6)
# n.insert(3, 36)
# print("vsego:", n.count("hui"))
# n.sort()
# n.reverse()
# print(n)
# y = n.pop(1)
# print(y)
# print(n)

# n = list(range(1, 21))
# m = []
# l = []
# print(n)
# for i in n:
#     if i % 2 == 0:
#         m.append(i)
#     elif i % 2 != 0:
#         l.append(i)
# print("chetnye chisla: ", m)
# print("nechetnye chisla: ", l)
# b = l[::-1]
# print(b)

# x = list(range(1, 15))
# x = tuple(x)
# print(x)
# v = x[2:5]
# print(v)

# x = list(range(1, 15))
# print(x)

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# l = len(x)
# print(l)
# for i in range(l):
#     x[i] += 3
# print(x)

# x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
# print(x)
# y = list(x)
# print(y)
# y.append(25)
# print(y)
# x = tuple(y)
# print(x)
# if x == x:
#     print(True)
# print(type(x))
# ('E:\\YandexDisk\\Desktop_Zal\\1', ['papka 1 pustaja', 'papka 2 pustaja', 'tut marian'], ['43f.jpg', '45rf.jpg', '533s.jpg'])

# spisok = []
# import os
# import time
# for adresses, dirs, files in os.walk("E:\\YandexDisk\\Desktop_Zal\\1"):
#     for file in files:
#         full = os.path.join(adresses + file)
#         if time.time() - os.path.getctime(full) < 86400:
#             spisok.append(full)
#
# print(spisok)



# def show():
#     print("funkcija")
# show()
# z = 5
# def show2():
#     x = 7
#     return x + z
#
# print(show2())
#
# z = 8
# print(show2())

# h = ["a", "a", "h"]
# k = [9, 8, 7 ,5 ,7 ,5]
# j = [9, 8, 7, 6]
# def counts(par, count = 0, par2 = False):
#     if par2 == True:
#         typ = type(par[0])
#         for i in par:
#             count += 1
#         return count, typ
#
#     else:
#         for i in par:
#             count += 1
#         return count
# print(counts(h, 0, True))
# print(counts(k, 0, True))
# print(counts(j, 0, True))

# def name(h, f, l, *args, key):
#     print(args)
#     print(h)
#     print(f)
#     print(l)
#     print(key)
# name(7, 9, 5 ,5, key = 10)

# def exclusive_item (*args, key = False):
#     new_list = []
#     for i in args:
#         for y in i:
#             if y not in new_list:
#                 new_list.append(y)
#     if key == True:
#         new_list.sort()
#     return new_list
#
#
# z = [9, 8, 7]
# x = [8, 8, 9, 7, 6, 5]
# c = [1, 2, 3, 4, 5, 6, 7, 7]
#
# t = exclusive_item(z, x, c, key=True)
# print(exclusive_item(t))

# x = 5
# def name():
#     global x
#     x = 100
#     print(x)
#
# name()
# print(x)
#
# def name2(par):
#     print(par)
# name2()

# x = 5
# def name():
#     x = 10
#     def name2():
#         nonlocal x
#         x = 100
#         print(x)
#
#     name2()
#     print(x)
# name()
# print(x)
# import math
# PI = math.pi
#
# def radius():
#     n = float(input("diametr cilindra v cm: "))
#     n /= 2
#     return n
#
# def height():
#     m = float(input("Vysota cilindra v cm: "))
#     return m
#
# def volume():
#     r = radius()
#     h = height()
#     s = PI*r**2
#     v = s*h
#     return v
# # print("Objem cilindra: ",volume(), "cm3")
# def massa(g):
#     n = float(input("Udelnyj ves g/cm3: "))
#     return g*n/1000
# print("Ves cilindra v kg: ", massa(volume()))

# d1 = {"a": 7}
# d2 = dict(a=7)
# d3 = dict.fromkeys([1, 2, 3, 4, 5])

# price = {"meat": 3, "bread": 1.5, "potato": 6.6, "water": 25}

# price = {"meat": 3, "bread": 1.5, "potato": 6.6, "water": 25}
# def buy():
#     pay = 0
#     while True:
#         enter = input("Chto pokupaem???\n")
#         if enter == "end":
#             break
#         if enter in price:
#             pay += price[enter]
#         else:
#             print("no such stuff")
#     return pay
# print("Vsego k oplate: ", buy())

# users = {
#     "Alex7": {"password": 9856214, "id": 1957},
#     "Jimmy99": {"password": 1236487, "id": 9654},
#     "Bob": {"password": 9546752, "id": 6453}
# }
#
# print(users["Alex7"]["password"])

# pricelist = {"morkovka": 5, "pomidory": 2, "kurica": 4.5, "tapinambur": 68}
# def buy():
#     korzina = 0
#     while True:
#         enter = input("chto berem???\n")
#         if enter == "end":
#             print("Pozdravljaju s pokupkami!")
#             break
#         if enter in pricelist:
#             korzina += pricelist[enter]
#         else:
#             print("No such item bro!")
#     return korzina
# print(buy(), "baksov k oplate")
# ---
# s = "stroka teksta"
# print(s.upper())
# print(s.capitalize())
# print(s)
# u = s.upper()
# print(u)
#
# path = "C:\Program Files (x86)\IDEMIA\AWP\DLLs"
# path1 = path.replace("\\", "/")
# print(path1)
# print(list(path.split("\\"))[-1])

# o = open("tekst.txt")
# r1 = o.read()
# # print(r1)
# list_znaki = ["-", ":", "!", "?", "'"]
# for i in r1:
#     if i in list_znaki:
#         r1 = r1.replace(i, "")
# print(r1)
# r2 = r1.split()
# print(r2)
# joind = " ".join(r2)
# print(joind)
# nokavychki = joind.replace('"', '')
# print(nokavychki)
# with open("tekst.txt", "w") as o:
#     o.write(nokavychki)

# def twicefunc(insidefung):
#     insidefung()
#     insidefung()
# def hello():
#     print("hello")
#
# test = twicefunc(hello)


# def twicefunc(insidefung):
#     def wrapper():
#         insidefung()
#         insidefung()
#     return wrapper
# def hello():
#     print("hello")
#
# test = twicefunc(hello)
# test()

# def mainfunc(inside):
#     def wrapper():
#         inside()
#         inside()
#     return wrapper()
#
# def badwordfunc():
#     print("HUI")
#
# mainfunc(badwordfunc)

# def make_adder(x):
#     def adder(n):
#         return x+n
#     return adder(5)
# print(make_adder(5))

# def mydecorator(afunctiontodecorate):
#     def wrapper():
#         print("Я буду выполнен до основного вызова!")
#         result = afunctiontodecorate()
#         print("Я буду выполнен после основного вызова!")
#         return result
#     return wrapper
#
# def myfunction():
#     print("Я - оборачиваемая функция!")
#
# print(myfunction())
#
# decoratedfunction = mydecorator(myfunction)
# print(decoratedfunction)


# def my_decorator(a_function_to_decorate):
#       def wrapper():
#         print("Я буду выполнен до основного вызова!")
#         result = a_function_to_decorate()
#         print("Я буду выполнен после основного вызова!")
#         return result
#       return wrapper
# def my_function():
#    print("Я - оборачиваемая функция!")
#    return 0
# print(my_function())
#
# decorated_function = my_decorator(my_function)  # декорирование функции
# print(decorated_function())

# import time
# def decorator_time(fn):
#    def wrapper():
#        print(f"Запустилась функция {fn}")
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        print(f"Функция выполнилась. Время: {dt:.10f}")
#        return dt  # задекорированная функция будет возвращать время работы
#    return wrapper
#
#
# def pow_2():
#    return 10000000 ** 2
#
#
# def in_build_pow():
#    return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# pow_2()
#
#
# in_build_pow()

# def in_build_pow():
#     return pow(10000000, 2)
# print(in_build_pow())

# def my_decorator(fn):
#     print("Этот код будет выведен один раз в момент декорирования функции")
#     def wrapper(*args, **kwargs):
#         print('Этот код будет выполняться перед каждым вызовом функции')
#         result = fn(*args, **kwargs)
#         print('Этот код будет выполняться после каждого вызова функции')
#         return result
#     return wrapper


# L = ('a', 'b', 'c')
# print(type(L))
# print(id(L))
#
# D = (44)
# print(type(D))
# LD = L + (D,)
# print(LD, id(LD))


# c = 123456789
# d = 123456789
#
# print(c == d)
# print(c is d)

# print(id(a))
# print(id(b))

# a = 0
# b = 0
#
# while id(a) == id(b):
#     a += 1
#     b += 1
# print("the last number is:", a, "its ID: ", id(a))
# print("the last number is:", b, "its ID: ", id(b))
# print(id(257))
# print(id(257))
# print(id(250))
# print(id(250))

# while id(a) == id(b):
#     a -= 1
#     b -= 1
# print(a)
# print(b)

# x = 257
# y = 257
#
# print(x == y)  # Use == for value comparison
# print(x is y)  # Use is for identity check

# c = 123456789
# d = 123456789
#
# print(c == d)
# print(c is d)
#
# print(id(c))
# print(id(d))

# L = ["Hello", "world"]
# M = L.copy()
#
# print(L is M)
#
# M.append("!")
# print(L)

# L = [1, 2, 3, 8, 8, ["H&M", "Zara"]]
# S1 = (1, 2, 3, 8, 8, ["H&M", "Zara"])
# print(L)
# print(S1)
# S1[-1].append("Uniqlo")
# newlist = S1
# print(S1)
# print(newlist)

# S = set(L)
# T = tuple(L)
# print(S)
# print(T)
#

# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
# print(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
# print(shopping_center[-1])
#
# print(list_id_before)
# print(list_id_after)
# print(list_id_before is list_id_after)

# g = 5
# d = 6
# print(g == d)


# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]
#
# print(a is b)  # True, because a and b reference the same object
# print(a is c)  # False, because a and c reference different objects
#
# # Using == for value equality
# print(a == c)  # True, because the values of a and c are equal

# a = "False, because a and c reference different objects"
# b = "False, because a and c reference different object"
# print(a is b)


# text = input("Введите текст: ")
# textlist = list(text)
# setlist = set(textlist)
# # print(len(textlist))
# print("Количество уникальных символов: ", len(setlist))

# set1 = {"Иванов", "Петров", "Васильев", "Антонов"}
# set2 = {"Gurmanov", "Deverev"}
# print(set1.union(set2))

# 1 2 3 4 5 6 7 8
# 2 4 6 8 10 12

# a = input("Введите последовательность целых чисел 1: ")
# b = input("Введите последовательность целых чисел 2: ")
# a1 = a.split()
# b1 = b.split()
# # print(a1)
# # print(b1)
# # print(type(a1))
# # print(type(b1))
# a_set, b_set = set(a1), set(b1)
# # print(a_set)
# # print(b_set)
# a_and_b = list(a_set.symmetric_difference(b_set))
# intlist = []
# for i in a_and_b:
#     intlist.append(int(i))
# sorted = sorted(intlist)
# joinedback = " ".join(map(str, sorted))
# print(joinedback)

# some_var = [5]
# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))

# b = None or 1
# print(b)

# print(1 and "hello" and [True])

# a = 4
# b = 2
# # пусть a и b - переменные, которые мы хотим проверить
# if a and b: # проверка истинности обеих переменных
#     print("Обе переменные истинные")
#     print(a,b)

# a = None
# b = None
# # пусть a и b - переменные, которые мы хотим проверить
# if a and b:
#     print("Обе переменные истинные")
#     print(a,b)
# elif a or b:
#     print("Одна из переменных истинная")
#     print(a or b) # печать значения одной переменной, которая является истинной
# else:
#     print("Обе переменные ложные")

# print(7 % 3)
# print(22 // 3)
#
# while True:
#     a = int(input("Введите число: "))
#     if type(a) == int and a in range(100, 1000) and a % 3 == 0 and a % 2 == 0:
#         print("Отвечает условиям!!!")
#         break
#     else:
#         print("Не подходит")
# while True:
#     a = int(input("Введите число: "))
#     if all([type(a) == int, a in range(100, 1000), a % 3 == 0, a % 2 == 0]):
#         print("Отвечает условиям!!!")
#         break
#     else:
#         print("Не подходит")
# 4 5 6 7 9 7 2 4 0

# a = input("Введите последовательность чисел: ")
# a1 = a.split()
# listint = list(map(int, a1))
# print(listint)
# if all(listint):
#     print(True)
# else:
#     print(False)

# if any in:
#     print(True)
# else:
#     print(False)

# a = [4, 5, 6, 7, 9, 7, 2, 4, 1]
# if all(a):
#     print(True)


# 4 5 6 7 9 7 2 4 0
# 0 0 0 0 0 0 0
# a = input("Введите последовательность чисел: ")
# a1 = a.split()
# listint = list(map(int, a1))
# print(listint)
# if not any(listint):
#     print(True)
# else:
#     print(False)


# squares = [i**2 for i in range(1,11) if i % 2 == 1]
# print(squares)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in nums:
#     for i2 in nums2:
#         result = i * i2
#         print(i, "*", i2, "=", result)
#     print("----------")

# tablicaumn = [i * i2 for i in range(1, 11) for i2 in range(1, 11)]
# print(tablicaumn)

# print(list(range(1, 11)))
# tablicaumn = [i * i for i in range(1, 11)]
# print(tablicaumn)

# T = [[i*j for j in range(1,11)] for i in range(1,11)]
# print(T)

# L = ["Even" if int(input()) % 2 == 0 else "Not even" for i in range(5)]
# print(L)

# L = [int(input()) % 2 == 0 for i in range(5)]
# print(not all(L))
#
# L = [int(input()) % 2 == 0 for i in range(5)]
# print(not any(L))

# L = [2, 2, 2, 1, 2]
# Leven = [i % 2 == 0 for i in L]
# print(any(Leven) and not all(Leven))
#
# L = [2, 1, 1, 1, 1]
# Leven = [i % 2 == 0 for i in L]
# print(any(Leven) and not all(Leven))

# l = [i for i in range(10)]
# print(l)
# m = [i for i in range(10, 0, -1)]
# print(m)
# lm = []
# for a, b in zip(l, m):
#     lm.append(a * b)
# # print(lm)
# # print(type(lm))
# joined = " ".join(map(str, lm))
# print(joined)
    # print('a =', a, 'b =', b, "...", "a x b = ", a*b)

# a3b2c4d1a2
# t = "aaabbccccdaa"
# l = list(t)
# counter = 0
# while i
#
# for i in l:
#     if i == l[1]:
#         counter += 1
#         print(counter)

# string = "aaabbccccdaa"
# # a3
# l = list(string)
# print(l)
# count = 0
# result = ""
# firstchar = string[0]
# for i in string:
#     if i == firstchar:
#         count += 1
#     else:
#         result += firstchar + str(count)
#         firstchar = i
#         count = 1
# result += firstchar + str(count)
# print(result)

# numbers = [2, 1, 3, 4, 7]
# more_numbers = [*numbers, 11, 18]
# print(more_numbers)
# print(*more_numbers, sep=", ")

# fruits = ['lemon', 'pear', 'watermelon', 'tomato']
# print(*fruits, sep=", ")

# fruits = {'lemon': 1, 'pear': 4, 'watermelon': 67, 'tomato': 3}
# print(type(fruits))
# newdict = {**fruits}
# print(newdict)

# def linear_solve(a, b):
#     if a != 0:
#         return b / a
#     else:
#         return "no return"
# print(linear_solve(2,9))
# print(linear_solve(-5,1))

# a = float(input("Введите a: "))
# b = float(input("Введите b: "))
# c = float(input("Введите c: "))
# def D(a, b, c,):
#     return b**2 - 4*a*c
# discriminant = D(a, b, c)
# print("Дискриминант: ", discriminant)
#
# def quadratic_solve(a, b, c):
#     if discriminant < 0:
#         return "Не имеет вещественных корней"
#     elif discriminant == 0:
#         return -b / (2 * a)
#     else:
#         return (-b - discriminant **0.5)/(2*a), (-b + discriminant **0.5)/(2*a)
# print("Решение уравнения: ", quadratic_solve(a, b, c))

# fruits = ['lemon', 'pear', 'watermelon', 'tomato']
# print(*fruits)

# Recursion

# L = [8, 7, 6]
# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:])\
#         else min_list(L[1:])
# result = min_list(L)
# print(result)

# L = [5, 7, 54, 6, 4, 7, 8, 4, 33]
# if L[0] < (L[1:]):
#     print(L[0])
# else:
#     print(L[1:])

# def recursive(i):
#     print(i)
#     if i < 4:
#         recursive(i + 1)
#     print(i)
# recursive(1)

# def fact(n):
#     print(n)
#     if n <= 0:
#         return 1
#     else:
#         return n * fact(n - 1)
#
# print(fact(3))

# def rec(x):
#     if x < 5:
#         print("Func 1:", x)
#         rec(x + 1)
#         print("Func 2:", x)
# rec(1)

# def palindrome(s):
#     if len(s)<=1:
#         return True
#     if s[0]!=s[-1]:
#         return False
#     return palindrome(s[1:-1])
# print(palindrome("shalahs"))


# x = 0
# if x < 5:
#     x += 1
#     print(x)
#     if x < 5:
#         x += 1
#         print(x)
#         if x < 5:
#             x += 1
#             print(x)
#             if x < 5:
#                 x += 1
#                 print(x)

# L = [5, 7, 4, 9, 5, 3, 3, 6]
# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     else:
#         return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])
# print(min_list(L))

# res = 0
# def mirror(a, res = 0):
#     if a == 0:
#         return res
#     else:
#         return mirror(a // 10, res*10 + a % 10)
# result = mirror(12345)
# print(result)

# def rec_sum(n):
#     if n == 1:
#         return 1
#     return n + rec_sum(n - 1)
# print(rec_sum(5))
# n = "использовать"
# print(len(n))
# print(n[::])
# print(n[:-2])

# def restr(n):
#     if len(n) == 0:
#         return ""
#     else:
#         return n[-1] + restr(n[:-1])
# print(restr("test"))

# def reverse_str(string):
#    if len(string) == 0:
#        return ''
#    else:
#        return string[-1] + reverse_str(string[:-1])
#
# print(reverse_str('test'))  # tset

# def f():
#     return [43, 65, 32]
# print(f())
# print(f())

# def genf():
#     # s = 7
#     for i in [43, 65, 32, 98, 54]:
#         yield i
#         # print(s)
#         # s = s*10+7
# genobj = genf()
# print(next(genobj))
# print(next(genobj))
# print(next(genobj))
# print(next(genobj))

# def fact(n):
#     pr=1
#     a=[]
#     for i in range(1, n+1):
#         pr=pr*i
#         a.append(pr)
#     return a
# print(fact(5))
#
# def fact(n):
#     pr=1
#     for i in range(1, n+1):
#         pr=pr*i
#         yield pr
# f = fact(5)
# print(next(f))
# print(next(f))
# print(next(f))

# e = 2.718
#
# last = 0
# for a in e(): # e() - генератор
#     if (a - last) < 0.00000001: # ограничение на точность
#         print(a)
#         break # после достижения которого завершаем цикл
#     else:
#         last = a # иначе - присваиваем новое значение
#
# def e():
#     n = 1
#
#     while True:
#         yield (1 + 1 / n) ** n
#         n += 1
# result = e()
# print(next(result))

# def e_generator():
#     n = 1
#     while True:
#         yield (1 + 1/n) ** n
#         n += 1
#
# e = e_generator()
#
# last = 0
# for a in e:
#     if (a - last) < 0.00000001:
#         print(a)
#         break
#     else:
#         last = a
#
# # You can continue to get more values from the generator if needed
# print(next(e))

# iter_obj = iter("Hello!")
#
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# yesno = input("""Введите Y, если хотите авторизоваться, или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
# def is_auth(func):
#     def wrapper():
#         if auth:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь не авторизован. Функция выполнена не будет")
#     return wrapper
#
# @is_auth
# def from_db():
#     print("some data from database")
#
# from_db()

# userinput = input("Please input Y or N if you wish to login or not: ")
#
# auth = userinput == "Y"
#
# def login(func):
#     def wrapper():
#         if auth is True:
#             print("You are logged in!")
#             func()
#         else:
#             print("You are incognito!")
#     return wrapper
#
# @login
# def connectdatabase():
#     print("Wait... connecting to database")
# connectdatabase()





# ------------------USER LOGG IN PART 1---------------------------
# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
# userinput = input("Please input Y or N if you wish to login or not: ")
#
# auth = userinput == "Y"
#
# def is_auth(call):
#     def wrapper():
#         if auth is True:
#             print("You are going to logg in")
#             call()
#         else:
#             print("You continue not logged in!")
#     return wrapper
# def has_access(call):
#     def wrapper():
#         username = input("Enter your username: ")
#         if username in USERS:
#             print("Username is correct, please wait...")
#             call()
#         else:
#             print("No such user")
#     return wrapper
#
#
# @is_auth
# @has_access
#
# def accessdata():
#     print("Downloading data from server...")
# accessdata()

# -----------------------USER LOGG IN PART 2-------------------------------

# L = ['THIS', 'IS', 'LOWER', 'STRING']
# m = list(map(str.lower, L))
# print(m)

# f = "dsfdsfdDSGDFGFDD".lower()
# print(f)

# def negpos(i):
#     if i > 0:
#         return True
#
# L = [-2, -1, 0, 1, -3, 2, -3]
# p = list(filter(negpos, L))
# print(p)

# def even(i):
#     if i % 2 == 0:
#         return True
#
# L = [-2, -1, 0, 1, -3, 2, -3]
# p = list(filter(even, L))
# print(p)

# onelist = list(range(20))
# some_list = [i - 10 for i in range(20)]
# print(onelist)
# print(some_list)
#
# result = [i**2 for i in some_list if i > 0]
# print(result)

# x1 = 46
# x2 = 98
# result = lambda x1, x2: x1 + x2
# print(result(x1, x2))

# reslut2 = list(map(lambda x: x ** 2, range(1, 11)))
# print(reslut2)

# d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}
# print(d.items())
# print(sorted(d.items()))
# print(dict(sorted(d.items())))
# print(dict(sorted(d.items(), key = lambda x: x[1])))
# print("short code here------------------")
# # (weight, height)
# data = [
#     (94, 1.89),
#     (68, 1.74),
#     (90, 1.89),
#     (73, 1.79),
#     (76, 1.84)
# ]
#
# result = (x / y**2 for x, y in data)
# resultlist = list(result)
# print("Weight indexes: ", resultlist)
# sortedlist = sorted(resultlist, reverse=True)
# print("Weight indexes sorted: ", sortedlist)
#
# L = list(range(1, 11))
# print("Spisok: ",L)
#
# kvadratL = list(map(lambda x: x**2, L))
# print(kvadratL)

# print("short code here------------------")
# (weight, height)
# data = [
#     (94, 1.89),
#     (68, 1.74),
#     (90, 1.89),
#     (73, 1.79),
#     (76, 1.84)
# ]
#
# result = sorted(list(map(lambda x: x[0] / x[1]**2, data)))
# print("Sorted: ", result)
#
# result = min(list(map(lambda x: x[0] / x[1]**2, data)))
# print("Min index: ", result)

# a = ["asd", "bbd", "ddfa", "mcsa"]
# # print(len(a[2]))
# alen = list(map(lambda x: len(x), a))
# print(alen)

# alen = list(map(len(), a))
# print(alen)
# print(len(a[2]))

# a = ["asd", "bbd", "ddfa", "mcsa"]
# print([len(i) for i in a])

# a = ["это", "маленький", "текст", "обидно"]
# print(list(map(str.upper, a)))


# Krestiki noliki-------------------------------------------------------

player1 = "X"
player2 = "O"

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------")
    print("\t", board[6], "|", board[7], "|", board[8])
    print("\t")
display_board(board)

def take_turn (player):
    while True:
        player_turn = int(input(f"{player} turn! Please enter number (0 - 8): "))
        if 0 <= player_turn <= 8 and board[player_turn] not in [player1, player2]:
            board[player_turn] = player
            break
        else:
            print("Invalid input! Try again!")
    display_board(board)

# win situations:
def win_situations():
    if (board[0] == board[1] == board[2])\
            or (board[3] == board[4] == board[5])\
            or (board[6] == board[7] == board[8])\
            or (board[0] == board[4] == board[8])\
            or (board[2] == board[4] == board[6]):
        return True
win_situations()

for _ in range(5):
    take_turn(player1)
    if win_situations():
        print(f"{player1} win win congratulations!!")
        break
    take_turn(player2)
    if win_situations():
        print(f"{player2} win win congratulations!!")
        break
print("Game Over!")















