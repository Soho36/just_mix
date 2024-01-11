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

input_str = "((()))"

def par_checker():
    stack = []
    for char in input_str:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
        # else:
        #     return False

    if len(stack) == 0:
        print(True)
    else:
        print(False)

par_checker()