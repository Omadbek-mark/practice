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


# try avoid this
people = "andrew", "John"
animals = "dog,"


print(("===== Unpacking arguments ====="))
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"the x: {x} and the y: {y}")
print("z:", z)  # list


# *args > tuple
def calculate(*args):
    total = 1
    for x in args:
        total *= x
    print(f"the type(args) value: {type(args)}")
    print(f"the total value: {total}")
    return total


# CALL
calculate(1, 7, 2, 3)
print("-----")
calculate(0, 2, 300)
print("-----")
calculate(7, 5)
