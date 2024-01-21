# # List comprehension
# squares_list = [x**2 for x in range(5)]
#
# # Generator expression
# squares_generator = (x**2 for x in range(5))
#
# # With a Key Function:
# words = ["apple", "banana", "cherry", "date"]
# min_word_by_length = min(words, key=lambda x: len(x))
# print(min_word_by_length)  # Outputs: "date"
#
# words = ["apple", "banana", "cherry", "date"]
# length_list = list(map(lambda x: len(x), words))
# print(length_list)
#
# # BINARY TREE
#
# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#         self.left_subordinate = None
#         self.right_subordinate = None
#
#     def add_subordinate_left(self, subordinate):
#         if self.left_subordinate is None:
#             self.left_subordinate = subordinate
#         else:
#             new_subordinate = subordinate
#             new_subordinate.left_subordinate = self.left_subordinate
#             self.left_subordinate = new_subordinate
#
#     def add_subordinate_right(self, subordinate):
#         if self.right_subordinate is None:
#             self.right_subordinate = subordinate
#         else:
#             new_subordinate = subordinate
#             new_subordinate.right_subordinate = self.right_subordinate
#             self.right_subordinate = new_subordinate
#
#     def display_hierarchy(self, level=0):
#         indentation = "    " * level
#         print(f"{indentation}{self.name} - {self.position}")
#
#         if self.left_subordinate:
#             self.left_subordinate.display_hierarchy(level + 1)
#         if self.right_subordinate:
#             self.right_subordinate.display_hierarchy(level + 1)
#
#     # TREE TRAVERSAL
#     def pre_order(self):
#         print(self.name)
#
#         if self.left_subordinate is not None:
#             self.left_subordinate.pre_order()
#
#         if self.right_subordinate is not None:
#             self.right_subordinate.pre_order()
# # Example usage:
# Director = Employee("John Doe", "1")
# Finance_director = Employee("Alice Johnson", "2")
# Managing_director = Employee("Bob Smith", "2")
# Manager1 = Employee("Eva Brown", "3")
# Manager2 = Employee("Charlie Davis", "3")
# Manager3 = Employee("Vasili Huev", "3")
#
# Director.add_subordinate_left(Finance_director)
# Director.add_subordinate_right(Managing_director)
# Director.add_subordinate_left(Manager3)
# # Managing_director.add_subordinate_left(Manager1)
# # Managing_director.add_subordinate_right(Manager2)
#
#
# Director.display_hierarchy()
# Director.pre_order()
#
# #FIND ELEMENT IN ARRAY
#
# array_str = input("enter array: ")
# element_str = int(input("enter element: "))
#
# array_list = list(map(int, array_str))
# print(array_list)
#
# array_list_enum = list(enumerate(array_list))
# print(array_list_enum)
#
#
# def find(array_list_enum, element_str):
#     for i, a in array_list_enum:
#         if a == element_str:
#             return i
#     else:
#         return False
#
# print(find(array_list_enum, element_str))
#
# # BINARY SEARCH
#
# def binary_search(array, element, left, right):
#     if left > right or left >= len(array):  # если левая граница превысила превысила правую или длину массива,
#         return False  # значит, элемент отсутствует
#
#     middle = (right + left) // 2  # находим середину
#     if array[middle] == element:  # если элемент в середине
#         return middle  # возвращаем этот индекс
#     elif element < array[middle]:  # если элемент меньше элемента в середине
#         # рекурсивно ищем в левой половине
#         return binary_search(array, element, left, middle - 1)
#     else:  # иначе в правой
#         return binary_search(array, element, middle + 1, right)
#
#
# element = int(input())
# array = [i for i in range(1, 100)]  # 1,2,3,4,...
#
# # запускаем алгоритм на левой и правой границе
# print(binary_search(array, element, 0, 99))