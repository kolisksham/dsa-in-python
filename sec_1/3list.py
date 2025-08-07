# 1-9
a = [x for x in range(10)]
print(a)
print("_"*100)

# 0-20
b = [x for x in range(21) if x % 2 == 0]
print(b)
print("_"*100)

# square of each nums
c = [x**2 for x in [1, 2, 3, 4, 5]]
print(c)
print("_"*100)

# convert strings to uppercase letter
d = [s.upper() for s in ["apple", "banana", "cherry"]]
print(d)
print("_"*100)

# filter +ve numbers
e = [x for x in [1, -5, 68, -52, -7] if x > 0]
print(e)
print("_"*100)

# add 5 to each nums
f = [x + 5 for x in [10, 20, 30]]
print(f)
print("_"*100)

# 7. Multiply elements from two lists (element-wise)
g = [x * y for x, y in zip([1, 2, 3], [4, 5, 6])]
print(g)
print("_"*100) #zip

# 8. Flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
h = [num for row in matrix for num in row]
print(h)
print("_"*100) #8 [1, 2, 3, 4, 5, 6]

# replace * with vowels
text = "hello world"
i = ['*' if c in 'aeiou' else c for c in text]
print(i)
print("_"*100)

# extract digit from string
j = [c for c in 'a1b2c3' if c.isdigit()]
print(j)
print("_"*100)

#reverse each word
k = [word[::-1] for word in ["hello", "world"]]
print(k)
print("_"*100)

#(x,y) pairs for 0-2
l = [(x,y) for x in range(3) for y in range(3)]
print(l)
print("_"*100)

#remove empty str
m = [s for s in ["str1", "", "str2", "  "] if s]
print(m) #space holds a value in str
print("_"*100) 

#filter strings with length > 3
n = [s for s in ["hello" , "world", "I'm", "Sam"] if len(s) > 3]
print(n)
print("_"*100)

#get ascii value of chars
o = [ord(c) for c in "ABC"]
print(o)
print("_"*100)

#filter and square odd nums
p = [x**2 for x in range(10) if x % 2 != 0]
print(p)
print("_"*100)

#create list of even/odd
q = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print(q)
print("_"*100)

#count chars in each word in list
words = ["pen", "pineapple", "apple", "pen"]
r = [len(word) for word in words]
print(r)
print("_"*100)

# replace nums < 0 with 0
nums = [-7, 5, -9, 22, -5, 73]
s = [0 for num in nums if num < 0]
print(s)
print("_"*100)

#duplicate each element in a list
arr=[1,2,3]
t = [x for x in arr for _ in range(2)]
print(t)
print("_"*100)

#filter out words starting with "a"
fruits = ["apple", "banana", "avocado", "cherry"]
u = [fruit for fruit in fruits if fruit.startswith('a')]
print(u)
print("_"*100)

#create list of tuples (x, x^2)
v = [(x, x**2) for x in range(1, 11)]
print(v)
print("_"*100)

#filter out common nums from 2 lists
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
w = [x for x in l1 if x in l2]
print(w)
print("_"*100)

#create dictionary from 2 lists
index = [1, 2, 3]
value = ["a", "b", "c"]
x = {ind : val for ind, val in zip(index, value)}
print(x)
print("_"*100)

#replace None with 0
l3 = [1, None, 3, 47, None]
y = [x if x != None in l3 else 0 for x in l3]
print(y)
print("_"*100)

#extract unique chars from strings
z = list({char for char in "programming"})
print(z)
print("_"*100)



