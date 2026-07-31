
# Operators in Python

# Arithmetic Operators
x = 65
y = 15

print("x + y =", x + y)
print("x // y =", x // y)
print("2 * 3 =", 2 * 3)
print("2 ** 3 =", 2 ** 3)

# Logical Operators
print("True and False =", True and False)
print("True or False =", True or False)

# Bitwise Operators
a = 2
b = 3

print("a ^ b =", a ^ b)
print("a << 2 =", a << 2)
print("a >> 2 =", a >> 2)

# Membership Operators
st = "abc"
num = 98.89

lst = [10, 20, 30, 40]

print("70 in lst =", 70 in lst)
print("70 not in lst =", 70 not in lst)

# Identity Operators
emp = ("emp-1", "abc", 25000.00)

lst1 = lst

print("lst is lst1 =", lst is lst1)
print("lst is not lst1 =", lst is not lst1)

print(lst)
print(id(lst))