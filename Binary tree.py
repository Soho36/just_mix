class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def insert_new_left_node(self, new_value):
        if self.left_node is None:
            self.left_node = new_value

        else:
            new_node = new_value    #new node will get the new value
            new_node.left_node = self.left_node #left node of the old node becomes left node of the new node
            self.left_node = new_node #left node of the current node is updated to the new node
        return self


    def insert_new_right_node(self, new_value):
        if self.right_node is None:
            self.right_node = new_value

        else:
            new_node = new_value
            new_node.right_node = self.right_node
            self.right_node = new_node
        return self

    def display_hierarchy(self, level=0):
        indentation = "    " * level
        print(f"{indentation}{self.value}")
        if self.left_node:
            self.left_node.display_hierarchy(level + 1)
        if self.right_node:
            self.right_node.display_hierarchy(level + 1)


#TREE TRAVERSAL
    def pre_order(self):
        print(self.value)

        if self.left_node is not None:
            self.left_node.pre_order()
        if self.right_node is not None:
            self.right_node.pre_order()

    def post_order(self):
        if self.left_node is not None:
            self.left_node.post_order()
        if self.right_node is not None:
            self.right_node.post_order()
        print(self.value)

    def in_order(self):
        if self.left_node is not None:
            self.left_node.in_order()

        print(self.value)

        if self.right_node is not None:
            self.right_node.in_order()

node_1 = BinaryTree("2 root")
node_2 = BinaryTree("7 left")
node_3 = BinaryTree("5 right")
node_4 = BinaryTree("2 left")
node_5 = BinaryTree("6 right")
node_6 = BinaryTree("4 left")
node_7 = BinaryTree("5 left")
node_8 = BinaryTree("11 right")
node_9 = BinaryTree("9 right")

node_1.insert_new_left_node(node_2)
node_1.insert_new_right_node(node_3)
node_2.insert_new_right_node(node_5)
node_2.insert_new_right_node(node_4)
node_5.insert_new_left_node(node_7)
node_5.insert_new_right_node(node_8)
node_3.insert_new_left_node(node_6)
node_3.insert_new_left_node(node_9)

node_1.display_hierarchy()
node_1.pre_order()
print("*****")
node_1.post_order()
print("*****")
node_1.in_order()











