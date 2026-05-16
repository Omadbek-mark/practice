''' Tuple
    (1) What is tuple: vs list
    (2) Unpacking arguments
    (3) zip
'''

print(("===== What is tuple: vs list ====="))
# Java/PHP/NodeJS array => Python list

# literal
numbs = [3, 5, 1, 2]

# constructor
letters = list("Hello World!")

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = 'melon'
print("after fruits:", fruits)

animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("mit", 100, True, None)

print(animals[0])
# animals[0] = "bird"
