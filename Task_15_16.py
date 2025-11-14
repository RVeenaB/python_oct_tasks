# Problem 1 - Using break in a While Loop 
# Write a Python program that takes a list of numbers as input 
# numbers = [25, 30, 20, 40, 15, 25] and prints the sum of the numbers. 
# However, if the sum exceeds 100, stop adding numbers and print "Sum exceeded 100". 
print("-"*25)
print("task - 1 - use break in a while loop")

num_list = [25, 30, 20, 40, 15, 25]
print(f"List entered is : {num_list} and its length is {len(num_list)}")

sum=0
i = 0
while i <= len(num_list):
    print(f"Adding element {num_list[i]} sum of elements till index {i} is {sum}")
    if sum > 100:
        print(f"Sum {sum} exceeded 100! stopping iteration")
        break
    sum+=num_list[i]
    i+=1

print(f"Added until element {i} ")
    
print("-"*25)

# Problem 2 - Using continue in a For Loop 
# Write a Python script that uses a for loop to iterate through numbers from 1 to 600.
# Print only the odd numbers, skipping the even ones using the statement.
print("-"*25)
print("task - 2 - use continue in a while loop")
num_limit = int(input("Please enter the limit to check for odd numbers: "))
for i in range(1,num_limit + 1):
    if i%2 == 0:
       continue
    print(f"{i} is odd number") 
print("-"*25)    
# Problem 3 - Using pass in Conditional Statements continue 
# Write a Python script that checks if a number is even or odd. 
# If the number is even, print "Even"; if odd, do nothing (use the pass statement). 
print("-"*25)    
print("task - 3 - use pass in a continal statements loop")
num_input = int(input("Please enter a number to check if even: "))
if num_input%2 == 0:
    print(f"number {num_input} is even")
else:
    pass    
print("end of even checker")
print("-"*25)
# Problem 4 - Combining Transfer Statements 
# Write a Python script that iterates through a list of words.
#  If the word is "break," exit the loop using the break statement.
#  If the word is "skip," skip the rest of the code for the current iteration using the continue statement. 
#  For any other word, print the word.
print("-"*25)    
print("task - 4 - use break in a while loop")
input_string_list = input("enter words list delimited by using space: ")
string_list = input_string_list.split()
print(f"User entered string list is : {string_list}")
for i in string_list:
    if i == "break":
        print(f"element in the string list is {i} hence breaking the remaining iterations")
        break
    elif i == "skip":
        print(f"element in the string list is {i}, hence skipping the current interation")    
        continue
    else:
        print(f"element in the string list is {i}")

    
print("-"*25)
