''' List
    (1) Working with lists
    (2) List methods
    (3) Lambda function
    (4) enumerate, map and filter
'''

print("===== Working with lists =====")
# Java/PHP/NodeJS array => Python list

# literal
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list
for team in groups:
    print(f"the team: {team}")


# constructor
letters = list("Hello World!")
print(f"the letters: {letters} and size: {len(letters)}")


print("------")
fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2]
c = fruits[::3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)


print("===== List methods =====")
# methods > append() insert() pop() remove() clear() sort() index()

letters = ["a", "d", "b"]

letters.append("c")  # add behind
print(f"the append results: {letters}")

letters.insert(1, "z")  # add front
print(f"the insert result: {letters}")

size = len(letters) - 1
result = letters.pop(size)  # pop behind
print(f"the pop result: {result} and letters: {letters}")

result2 = letters.pop(1)  # pop front
print(f"the pop result2: {result2} and letters: {letters}")


print("-----")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")
print("remove:", animals)

del animals[2:4]
print("animals delete:", animals)

exist = animals.index("cat")
print("cat exist:", exist)

animals.clear()
print("animals clear:", animals)

if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")


print("-----")
numbers = [2, 20, 12, 7, 58]
numbers.sort()
print("numbers:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)

# inmutable sorted
numbs = [2, 20, 100, 15]
new_numbs = sorted(numbs)
print(f"the sorted numbs: {numbs} and new_numbs: {new_numbs}")


print("===== Lambda function =====")
# Lambda is small anonymous function
def calculate(x, y): return x*y


result = calculate(3, 5)
print("result:", result)

people = [
    ("Robert", 20),
    ("Steve", 29),
    ("Joseph", 25),
    ("Michael", 30),
    ("Ali", 40)
]
people.sort()
print("people(1)", people)

# sort by age via lambda
people.sort(key=lambda person: person[1])
print("people2:", people)


print("===== enumerate, map and filtern =====")
# enumerate for index & value

animals = ["dog", "cat", "fish"]  # list
for element in enumerate(animals):
    print("element:", element)

for (index, value) in enumerate(animals):
    print(f"the index: {index} and value: {value}")

# similar in dictionaries
car_obj = dict(brand="Ferrari", year=2020)
result = car_obj.items()
for (key, value) in result:
    print(f"the key: {key} and value: {value}")


print("-----")
# map
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

result_map = map(lambda car: car[0], cars)
print(f"the result_map: {result_map} and type: {type(result_map)}")
new_cars = list(result_map)
print("new_cars(2):", new_cars)

print("-----")
# filter
result_filter = filter(lambda car: car[1] > 80, cars)
print(f"the result_filter: {result_filter} and type: {type(result_filter)}")
print(list(result_filter))
