class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = []

    def queue_max_size_reached(self):
        if len(self.items) == self.max_size:
            return True
    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        if not self.queue_max_size_reached():
            self.items.append(item)
        else:
            print("que max size is reached")

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) #returns and removes first element
        else:
            print("queue is empty")

    def peek(self):
        if not self.is_empty():
            print("Front of the queue: ", self.items[0])
            return self.items[0]
        else:
            print("queue is empty")

    def size(self):
        print("Queue size is: ", len(self.items))
        return len(self.items)

#user cmds
# add_to_queue = "add"
# remove_from_queue = "remove" #returns and removes first element
# peek_first_element = "show first"
# show_queue_size = "show size"

queue_max_size = int(input("Enter the Queue max size: "))
queue1 = Queue(queue_max_size)

while True:
    user_input = str(input("add, remove, show, size: "))
    if user_input == "add":

        queue1.enqueue(user_input)



#init


# queue1.enqueue([1, {"name": "Covertex"}, 6])
# queue1.enqueue(63)
# queue1.enqueue(98.5)
# queue1.enqueue("chart")


