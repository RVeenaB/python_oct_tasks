# Exercise 1- Sum of Squares Write a Python program that calculates and
#  prints the sum of the squares of numbers from 1 to 5 using a for loop.
print("----------------------------------------------------------------------------")
print("task - 1 - sum of squares")
sum_of_square = 0
for num in range(1,6):
    square_val = num ** 2
    print(f"""Square of {num} is {num ** 2}""")
    sum_of_square+=num ** 2

print(f"Sum of Squares of numbers 1 to 5 is {sum_of_square}")
print("----------------------------------------------------------------------------")
# Exercise 2- Countdown Write a Python program that uses a while loop to print a countdown from 5 to 1. 
print("----------------------------------------------------------------------------")
print("task - 2 - countdown from 5 to 1")
decr_counter = 5
print("countdown from 5 to 1 is:")
while decr_counter >= 1:
    print(f"{decr_counter}")
    decr_counter-=1
print("----------------------------------------------------------------------------")
# Exercise 3: Multiplication Table with Nested For Loop Write a 
# Python program to print the multiplication table for a user-specified number using a nested for loop.
print("----------------------------------------------------------------------------")
print("task - 3 - multiplication table")
times_table = int(input("Please enter the multiplication table for:"))
times_table_limit = int(input("Please enter multiplication level:"))
for i in range(1,2):
    for j in range(1,times_table_limit + 1):
        print(f"{times_table} X {j} = {times_table * j}")
    print(f"*** End of table for {times_table} upto {times_table_limit} ***")    
print("----------------------------------------------------------------------------")

# Exercise 4 - Write a Python program that uses a "for" loop 
# to find the sum of all even numbers between 0 and 10 (inclusive).
print("----------------------------------------------------------------------------")
print("task - 4 - sum of even numbers")
start_range = int(input("Enter the start range to fetch even numbers: "))
end_range = int(input("Enter the end range of the sum calculation: "))
even_sum = 0
for i in range(start_range,end_range + 1):
    if i%2 == 0:
        print(f"Even numbers in the range are {i}")
        even_sum+=i
print(f"Sum of even numbers in the range {start_range} to {end_range} is {even_sum}")        

print("----------------------------------------------------------------------------")

# Exercise 5 - Calculate the sum of all numbers from 1 to a given number 
print("----------------------------------------------------------------------------")
print("task - 5 - sum of numbers from 1 to given number")
num_limit = int(input("Enter the summation limit: "))
sum = 0
for i in range(1,num_limit + 1):
    print(i)
    sum+=i
print(f"Sum of numbers from 1 to {num_limit} is {sum}")    

print("----------------------------------------------------------------------------")

# Exercise 6 - Display numbers from a list using loop 
print("----------------------------------------------------------------------------")
print("task - 6 - numbers from a list using loop")
#num_list = [2,4,6,8,10,12,14]
num_list = list(input("enter a list"))
for i in num_list:
    print(f"current element in the list is {i}") 

print("----------------------------------------------------------------------------")

# Exercise 7 - Display numbers from 10 to 1 using for loop 
print("----------------------------------------------------------------------------")
print("task - 7 - display from 10 to 1")
loop_limit = int(input("Enter the loop limit: "))
for i in range(0,loop_limit):
    print(loop_limit)
    loop_limit-=1

print("----------------------------------------------------------------------------")

# Exercise 8 - Write a Python program to print the cube of all numbers from 1 to a given number
print("----------------------------------------------------------------------------")
print("task - 8 - cube of all numbers from 1 to given num")
cube_limit = int(input("Enter the cube list limit : "))
for i in range(1,cube_limit + 1):
    print(f"Cube of {i} is {i**3}")
print("----------------------------------------------------------------------------")

