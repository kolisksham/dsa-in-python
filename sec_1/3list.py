#examples
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [42, "hello", True, 3.14]

#Accessing
print(fruits[0])   # Output: apple
print(fruits[2])   # Output: cherry

#Modifying
fruits[1] = "orange"
print(fruits)      # Output: ['apple', 'orange', 'cherry']

#Adding
fruits.append("guava")
print(fruits)  # ['apple', 'orange', 'cherry', 'guava']

fruits.insert(1, "kiwi")
print(fruits)  # ['apple', 'kiwi', 'orange', 'cherry', 'guava']

_____________________________________________________________________________________________
#questions:
_____________________________________________________________________________________________

#print 1 - 10 

for i in range(1, 11):
    print(i)

print("_"*100)

#^2 of numbers

for i in range(1, 10):
    print(i, "^ 2 = ", i*i)

print("_"*100)

#sum of all nums 1-20

sum = 0
for i in range(1, 21):
    if(i % 2 == 0):
        sum += i
    else:
        continue
print("Sum of 1-20 is: ", sum)

print("_"*100)

#reverse a string

string = "hello"
reverse = ""

for c in string:
    reverse = c+reverse
print(reverse)

print("_"*100)

#5

# multiply elements in a list

nums = [1,2,3,4]
product = 1

for num in nums:
    product *= num

print("Product: ", product)

print("_"*100)

#add 5 to each element of list

nums = [10, 20, 30]
new_list = []

for num in nums:
    new_list.append(num + 5)
print("New List: ", new_list)

print("_"*100)

#which items are integers
items = [3, 'a', 4.5, 7, 'b']

for i in items:
    if type(i) == int:
        print(i, "is integer")

print("_"*100)

#max value

vals = [45, 67, 12, 89, 34, 149]

max_val = vals[0]

for val in vals:
    if(val > max_val):
        max_val = val
print("Max Value: ", max_val)

print("_"*100)

#10

#print index for values

fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(i, "-> ", fruits[i])

print("_"*100)

#12 

#list comprehension

sqrs = [i*i for i in range(1,6)]
print("Squares: ", sqrs)
print("_"*100)

#seperate even and odd

nums = [i for i in range(1,10)]
odd = []
even = []

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        even.append(nums[i])
    else:
        odd.append(nums[i])

print("Odd: ", odd)
print("Even: ", even)

#Capitalize first letter of each word
sentence = "hello world"
words = sentence.split()
for word in words:
    print(word.capitalize())

#Replace space with underscore
text = "learn python fast"
new_text = ""
for ch in text:
    if ch == " ":
        new_text += "_"
    else:
        new_text += ch
print("Updated:", new_text)

#Convert list of strings to uppercase
words = ["apple", "banana", "cherry"]
for i in range(len(words)):
    words[i] = words[i].upper()
print("Uppercase:", words)

#multiplication table of 5
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")

#Check which items are divisible by 3 and 5
nums = list(range(1, 31))
for n in nums:
    if n % 3 == 0 and n % 5 == 0:
        print(n, "is divisible by 3 and 5")

#Print only unique characters
s = "programming"
for ch in s:
    if s.count(ch) == 1:
        print(ch)
