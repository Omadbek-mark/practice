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
