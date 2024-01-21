# # linked list
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
# # Creating a linked list: 1 -> 2 -> 3 -> None
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)


#stack

# stack = []
#
# # Pushing elements onto the stack
# stack.append(1)
# stack.append(2)
# stack.append(3)
#
# print(stack)
#
# # Popping elements from the stack
# top_element = stack.pop()  # Removes and returns the last element (LIFO)
# print(stack)
# print(top_element)
#
# # Checking if the stack is empty
# is_empty = len(stack) == 0
# print(is_empty)

#par checker

# input_str = "[]()[(]()))"
#
# def par_checker():          #using list
#     stack = []
#     for char in input_str:
#         if char == "(" or char == "[":
#             stack.append(char)
#         elif char == ")" or char == "]":
#             if len(stack) > 0 and (stack[-1] == "(" or stack[-1] == "["):
#                 stack.pop()
#         # else:
#         #     return False
#
#     if len(stack) == 0:
#         print("balanced")
#     else:
#         print("not balanced")
#
# par_checker()


# input_str = "(())[]"
#
# sym_dict = {")": "(", "]": "["}
# def par_checker():          #using dictionary
#     stack = []
#     for char in input_str:
#         if char in sym_dict.values():
#             stack.append(char)
#         elif char in sym_dict.keys():
#             if len(stack) > 0 and stack[-1] == sym_dict[char]:
#                 stack.pop()
#             else:
#                 return False
#
#
#     if len(stack) == 0:
#         print("balanced")
#     else:
#         print("not balanced")
#
# par_checker()

# Grahps

# Alice (Person 1)
# Bob (Person 2)
# Carol (Person 3)
# Dave (Person 4)

# Alice is friends with Bob and Carol.
# Bob is friends with Carol.
# Carol is friends with Dave.
# Dave is friends with Alice.

# social_network = {
#     1: [2, 3],    # Alice is friends with Bob (2) and Carol (3)
#     2: [3],      # Bob is friends with Carol (3)
#     3: [4],      # Carol is friends with Dave (4)
#     4: [1]       # Dave is friends with Alice (1)
# }
# test

# underground_map = {
#     "admiralteiskaja": ["sadovaja"],
#     "sadovaja": ["sennaja", "spasskaja", "admiralteiskaja", "zvenigorodskaja"],
#     "sennaja": ["sadovaja", "spasskaja"],
#     "spasskaja": ["sadovaja", "sennaja", "dostoevskaja"],
#     "dostoevskaja": ["spasskaja", "vladimirskaja"],
#     "vladimirskaja": ["dostoevskaja", "pushkinskaja"],
#     "pushkinskaja": ["zvenigorodskaja", "vladimirskaja"],
#     "zvenigorodskaja": ["pushkinskaja", "sadovaja"]
# }
#
# # FIND THE SHORTEST WAY
# underground_map_weighted = {
#     "admiralteiskaja": {"sadovaja": 4},
#     "sadovaja": {"sennaja": 4, "spasskaja": 3, "admiralteiskaja": 4, "zvenigorodskaja":5},
#     "sennaja": {"sadovaja": 4, "spasskaja": 4},
#     "spasskaja": {"sadovaja": 3, "sennaja": 4, "dostoevskaja": 6},
#     "dostoevskaja": {"spasskaja": 6, "vladimirskaja": 3},
#     "vladimirskaja": {"dostoevskaja": 3, "pushkinskaja": 4},
#     "pushkinskaja": {"zvenigorodskaja": 3, "vladimirskaja": 4},
#     "zvenigorodskaja": {"pushkinskaja": 3, "sadovaja": 5}
# }
# inf = 1000
# # set distances to infinity
# distnaces = {"admiralteiskaja": 0,
#              "sadovaja": inf,
#              "sennaja": inf,
#              "spasskaja": inf,
#              "zvenigorodskaja": inf,
#              "dostoevskaja": inf,
#              "vladimirskaja": inf,
#              "pushkinskaja": inf,
#              }
#
# # set all nodes as unvisited
# unvisited = {"admiralteiskaja": True,
#              "sadovaja": True,
#              "sennaja": True,
#              "spasskaja": True,
#              "zvenigorodskaja": True,
#              "dostoevskaja": True,
#              "vladimirskaja": True,
#              "pushkinskaja": True,
#              }

# TREES

# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#
#     def insert_left(self, next_value):
#         if self.left_child is None:
#             self.left_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.left_child = self.left_child
#             self.left_child = new_child
#         return self
#
#     def insert_right(self, next_value):
#         if self.right_child is None:
#             self.right_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.right_child = self.right_child
#             self.right_child = new_child
#         return self
#
# A_node = BinaryTree('A').insert_left('B').insert_right('C')

# def find(array, element):
#     for i, a in enumerate(array):
#         if a == element:
#             return i
#     return False
#
# array = list(map(int, input().split()))
# element = int(input())
#
# print(find(array, element))

# Bogosort
# import random
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# is_sort = False
# count = 0
#
# while not is_sort:
#     count +=1
#
#     random.shuffle(array)
#
#     is_sort = True
#     for i in range(len(array)-1):
#         if array[i] > array[i+1]:
#             is_sort = False
#             break
# print(array)
# print(count)


# def calculate_factorial():
#     factorial = 1
#     for i in range(1, 101):
#         factorial = factorial * i
#     print(f"The factorial of 100 is: {factorial}")
#     print(f"This number has {len(list(map(str, str(factorial))))} digits")
# calculate_factorial()
#
#
# # splitted = hh.split()
# # print(splitted)

# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# counter1 = 0
# counter2 = 0
#
# for i in range(len(array)):
#     idx_min = i
#     for j in range(i+1, len(array)):
#
#         counter1 += 1
#         if array[j] < array[idx_min]:
#
#             # count_list.append()
#             idx_min = j
#         print("counter1", counter1)
#         counter2 += 1
#     if i != idx_min:
#         array[i], array[idx_min] = array[idx_min], array[i]
#     print("counter2", counter2)
# # print(countlist)
# print(array)

# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# for i in range(len(array)):
#     idx_max = i
#     for j in range(i+1, len(array)):
#
#         if array[j] > array[idx_max]:
#             idx_max = j
#
#     if i != idx_max:
#         # array[i], array[idx_min] = array[idx_min], array[i]
#         array[idx_max], array[i] = array[i], array[idx_max]
#
#
# print(array)
#
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# for i in range(len(array)): #range of indexes
#     for j in range(len(array) - i - 1):
#         if array[j] > array[j + 1]:
#             array[j], array[j + 1] = array[j + 1], array[j]
#
# print(array)

#Insertion Sort algorithm

# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# indexes = range(len(array))
# print(array)
#
# for i in indexes:
#     j = i
#     while j > 0 and array[j] < array[j-1]:
#         array[j], array[j - 1] = array[j - 1], array[j]
#         j -= 1
# print("sorted: ", array)

# count = 0
#
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# for i in range(1, len(array)):
#     x = array[i]
#     idx = i
#     while idx > 0:
#         count += 1
#         if (array[idx - 1] <= x):
#
#             break
#         array[idx] = array[idx - 1]
#         idx -= 1
#     array[idx] = x
#
# print(count)

#Merge Sort
# def merge_sort(L):  # «разделяй»
#     if len(L) < 2:  # если кусок массива равен 2,
#         return L[:]  # выходим из рекурсии
#     else:
#         middle = len(L) // 2  # ищем середину
#         left = merge_sort(L[:middle])  # рекурсивно делим левую часть
#         right = merge_sort(L[middle:])  # и правую
#         return merge(left, right)  # выполняем слияние
#
#
# def merge(left, right):  # «властвуй»
#     result = []  # результирующий массив
#     i, j = 0, 0  # указатели на элементы
#
#     # пока указатели не вышли за границы
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     # добавляем хвосты
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#
#     return result


#Quicksort

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# def qsort(array, left, right):
#     middle = (left + right) // 2
#
#     p = array[middle]
#     i, j = left, right
#     while i <= j:
#         while array[i] < p:
#             i += 1
#         while array[j] > p:
#             j -= 1
#         if i <= j:
#             array[i], array[j] = array[j], array[i]
#             i += 1
#             j -= 1
#
#     if j > left:
#         qsort(array, left, j)
#     if right > i:
#         qsort(array, i, right)

import random

def qsort_random(array, left, right):
    count = 0
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            count += 1
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)













