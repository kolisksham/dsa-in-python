# Question 1: For Loop
# Write a for loop that prints all numbers from 1 to 5 (inclusive), one per line.

print("1.Numbers inclusive 1-5: ")
for i in range(1, 6):
    print(i)
print("_" * 100,"\n")

# Question 2: While Loop
# Write a while loop that starts with a variable num = 3 
# and keeps doubling its value (num = num * 2) until it is greater than 20.
# Print the value each time.

print("2.Numbers are: ")
num = 3
while(num < 20):
    print(num)
    num = num * 2
print("_" * 100, "\n")

# Question 3: Nested Loop
# Print the following using nested loops:
#*
#**
#***

print("3. Pattern: ")
for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()
print("_" * 100, "\n")

# Question 4: Loop Break
# Write a for loop to print numbers from 1 to 10,
# but stop the loop if the number is 7.

print("4. The numbers are: ")
for i in range(1, 11):
    if(i == 7):
        break
    else:
        print(i)
print("_" * 100, "\n")
