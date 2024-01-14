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

social_network = {
    1: [2, 3],    # Alice is friends with Bob (2) and Carol (3)
    2: [3],      # Bob is friends with Carol (3)
    3: [4],      # Carol is friends with Dave (4)
    4: [1]       # Dave is friends with Alice (1)
}
# test

