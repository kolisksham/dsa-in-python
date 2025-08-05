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
