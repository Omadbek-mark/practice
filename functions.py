''' FUNCTIONS
(1) DEFINE VS CALL
(2) Parametr vs argument
(3) Keyword & default argumenta
(4) Scope
'''

print("===== DEFINE vs CALL =====")
# build in function > print() type()
# function - reusable block of code!
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - parametr
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - argument
result1 = greet("Mark")
print("result1:", result1)


result2 = greeting("justin")
print("result2:", result2)


print("===== Keyword & default arguments=====")
# DEFINE


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# CALL
result3 = give_greet(name="Justin", age=28)
print("result3:", result3)

result4 = give_greet("Mark")
print("result4:", result4)

print("===== Scope =====")
b = 100


# DEFINE
def calculate(a):
    c = a + b
    print(f"the c value: {c}")


# CALL
calculate(5)
