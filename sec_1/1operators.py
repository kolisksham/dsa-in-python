# -----------------------------------------
# 1. Arithmetic Operators
# -----------------------------------------
a = 10
b = 6

print("Arithmetic Operators:")
print("Addition:", a + b)          # 16
print("Subtraction:", a - b)       # 4
print("Multiplication:", a * b)    # 60
print("Division:", a / b)          # 1.666...
print("Modulus:", a % b)           # 4
print("Exponent:", a ** b)         # 1000000
print("Floor Division:", a // b)   # 1

print("\n-------------------------------\n")

# -----------------------------------------
# 2. Comparison Operators
# -----------------------------------------
x = 5
y = 10

print("Comparison Operators:")
print("x == y:", x == y)     # False
print("x != y:", x != y)     # True
print("x < y:", x < y)       # True
print("x > y:", x > y)       # False
print("x <= y:", x <= y)     # True
print("x >= y:", x >= y)     # False

print("\n-------------------------------\n")

# -----------------------------------------
# 3. Identity Operators
# -----------------------------------------
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("Identity Operators:")
print("a is b:", a is b)     # True (same object)
print("a is c:", a is c)     # False (different objects)
print("a == c:", a == c)     # True (values are same)

print("\n-------------------------------\n")

# -----------------------------------------
# 4. Bitwise Operators
# -----------------------------------------
a = 5                    # binary: 0101
b = 3                    # binary: 0011

print("Bitwise Operators:")
print("a & b =", a & b)  # 0101 & 0011 = 0001 -> 1
print("a | b =", a | b)  # 0101 | 0011 = 0111 -> 7
print("a ^ b =", a ^ b)  # 0101 ^ 0011 = 0110 -> 6

# Bitwise NOT flips all bits.
# ~a is the bitwise NOT of 5 -> flips 0101 to 1010 (in binary)
# In Python (two’s complement), ~n = -(n + 1)
print("~a =", ~a)        # Output: -6
