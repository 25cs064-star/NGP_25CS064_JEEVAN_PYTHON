# Python Programs - Single Copy Program

# 1. Variable Type Example
x = 100
print(x)
print(type(x))

x = "Python"
print(x)
print(type(x))

print("--------------------------------")

# 2. Delete Variable and Multiple Assignment
x = 100
del x

y = 200
x = y = z = 300

print(x)
print(y)
print(z)

print("--------------------------------")

# 3. Student Details
rno, stname, rank, mark = 1, "Arun", 5, 95

print(rno)
print(stname)
print(mark)

print("--------------------------------")

# 4. Employee Details
empid, empname, salary = 101, "Rahul", 50000

print(empid)
print(empname)
print(salary)

print("--------------------------------")

# 5. Variable Name Example
first_name = "abc"
print(first_name)

print("--------------------------------")

# 6. Lambda Function
res = lambda x: x + 100
print(res(200))

print("--------------------------------")

# 7. Multiline String
text = """Welcome to Python
Hello Python
Arrays
"""

print(text)