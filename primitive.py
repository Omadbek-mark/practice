print("==== number ====")
# in JAVA, variable is a name of storage location!
# in Python, variable is named reference!

count = 100
count_type = type(count)
print(f"the count: {count} and type: {count_type}")

result = count.bit_count()  # method
result2 = count.numerator  # state
print(result, result2)
