# List comprehension
squares_list = [x**2 for x in range(5)]

# Generator expression
squares_generator = (x**2 for x in range(5))

# With a Key Function:
words = ["apple", "banana", "cherry", "date"]
min_word_by_length = min(words, key=lambda x: len(x))
print(min_word_by_length)  # Outputs: "date"

words = ["apple", "banana", "cherry", "date"]
length_list = list(map(lambda x: len(x), words))
print(length_list)
