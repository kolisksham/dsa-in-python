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

#Question 5: Sum of Multiples (for loop)
# Write a for loop that finds the sum of all multiples of 3 
# between 1 and 30 (inclusive). Print the final sum.

print("5. Sum of multiples of 3 from 1 to 30:")
sum_multiples = 0
for i in range(1, 31):
    if i % 3 == 0:
        sum_multiples += i
print("Total sum is:", sum_multiples)
print("_" * 100, "\n")

# Question 6: Number Guessing (while loop + input)
# Write a while loop that keeps asking the user to guess a number.
# If the guess is correct, print "Correct!" and exit the loop.
# If the guess is wrong, print "Try again!" and loop again.

print("Guessing Game: ")

num = 7
guess = 0

while(guess != num):
    guess = int(input("Enter your choice(1-10): "))
    if(guess < num):
        print("Try a greater number. ")
        continue
    elif(guess > num):
        print("Try a smaller number. ")
        continue
    else:
        print("You Won!")
        break
print("_" * 100, "\n")

# Question 7: Print a Square Pattern (nested loops)
# Print a square of size 4x4 using "*". Your output should look exactly like:
# * * * *
# * * * *
# * * * *
# * * * *

print("7. Rectangle pattern: ")
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))

for i in range(l):
    for j in range(b):
        print("*", end=" ")
    print()
print("_" * 100, "\n")

# Question 8: Skip Odd Numbers (continue in for loop)
# Write a for loop that prints only the even numbers from 1 to 10 (inclusive). 
# Use continue to skip odd numbers.

print("8. Skipping Odd numbers: ")
ul = int(input("Enter upper limit: ")) #we're taking a custom number
for i in range(1, ul+1):
    if(i % 2 != 0):
        continue
    else:
        print(i)
print("_" * 100, "\n")
