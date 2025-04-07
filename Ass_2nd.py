# operators.py

# Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("a = 10")
print("b = 3")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)
print("\n")

# Assignment Operators
x = 5
print("Assignment Operators:")
print("Initial value of x:", x)
x += 3
print("After x += 3:", x)
x -= 2
print("After x -= 2:", x)
x *= 4
print("After x *= 4:", x)
x /= 3
print("After x /= 3:", x)
x %= 2
print("After x %= 2:", x)
print("\n")

# Comparison Operators
a = 10
b = 20
print("Comparison Operators:")
print('a =', a)
print('b  =', b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print('\n')

# Logical Operators
p = True
q = False
print("Logical Operators:")
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)
print('\n')

# Identity Operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("Identity Operators:")
print("list1 is list3:", list1 is list3)
print("list1 is list2:", list1 is list2)
print("list1 is not list2:", list1 is not list2)
print('\n')

# Membership Operators
colors = ["purple", "green", "blue"]
print('"colors = ["purple", "green", "blue"]"')
print("Membership Operators:")
print("'green' in colors:", "green" in colors)
print("'black' not in colors:", "black" not in colors)
print('\n')

# Bitwise Operators
a = 5  # 0101
b = 3  # 0011
print("Bitwise Operators:")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)