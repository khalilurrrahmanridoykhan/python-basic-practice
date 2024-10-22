
# Variable Declaration and Assignment
name = "Ridoy"
age = 30
height = 5.8
is_student = True
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Variable Update
name = "Ridoy Khan"
age = 31
height = 5.9
is_student = False
print("Updated Name:", name)

# Variable Type
print("Name Type:", type(name))
print("Age Type:", type(age))
print("Height Type:", type(height))
print("Is Student Type:", type(is_student))

# Variable Operaitions
a = 10
b = 5
c = a + b
d = a - b
e = a * b
f = a / b
print("Addition:", c)
print("Subtraction:", d)
print("Multiplication:", e)
print("Division:", f)

# Python Type Conversion
g = 10
h = 5.5
i = "10"
print("g Type:", type(g))
g = float(g)
print("g Type:", type(g))
h = str(h)
print("h Type:", type(h))
i = int(i)
print("i Type:", type(i))
num = int(1.9)
print("num:", num)
num1 = complex(1, 2)
print("num1:", num1)

# Python Input & Output
# input
# name = input("Enter Your Name: ")
# age = int(input("Enter Your Age:"))
# # Output
# print("Name:", name)
# print("Age:", age)

# Arithmetic Operations
a = 10
b = 5
c = a // b
d = a % b
e = a ** b
print("Floor Division:", c)
print("Modulus:", d)
print("Exponentiation:", e)

# Python List
for i in range(1, 6):
    print(i)

# Python List Operations
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number * number)

# Python List
list_of_strings = ["Ridoy", "Khan", "CSE", "BUET"]
for string in list_of_strings:
    print(string)
for i in range(5):
    if i == 3:
        break
    print(i)
for i in range(5):
    if i == 2:
        continue
    print(i)

print(list_of_strings[:-1])

# Python Tuple
tuplessin = (1, 2, 3, 4, 5)
for item in tuplessin:
    print(item)

# Python Tuple to list
tuples1 = ("Ridoy", "Khan", "CSE", "BUET")
tuples_to_list = list(tuples1)
print(tuples_to_list)

# list to Tuples
list1 = ["Ridoy", "Khan", "CSE", "BUET"]
list_to_tuples = tuple(list1)
print(list_to_tuples)

# Python Set
set1 = {1, 2, 3, 4, 5}
for item in set1:
    print(item)

set1.add(6)
print(set1)
set1.add(3)
print(set1)

# check membership of set
print(5 in set1)
print(len(set1))
set1.clear()
print(set1)

# Python Dectionary
dict1 = {"name": "Ridoy", "age": 30, "height": 5.8}
print(dict1)
if "name" in dict1:
    print("Name:", dict1["name"])

# Python Function
def add_numbers(a, b):
    return a + b

print(add_numbers(10, 5))