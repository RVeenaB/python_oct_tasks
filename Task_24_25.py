# Task 1: Create a Tuple Write a program that creates a tuple containing three 
# elements: your name, your age, and your favorite color. Then print the tuple.
print("Task 1 - create tuple")
User_input = ("abhi",10,"blue")
print(User_input)

#  Task 2: Access Tuple Elements Write a program that creates a tuple containing the 
# days of the week. Then, print the third element of the tuple.
print("Task 2 - Access tuple element")
days_of_week = ("Sun","mon","tue","wed,","thu","fri","sat")
print(f"third element of tuple {days_of_week} is {days_of_week[2]}")

#  Task 3 Tuple Concatenation Write a program that creates two tuples, one 
# containing odd numbers from 1 to 5 and another containing even numbers 
# from 2 to 6. Concatenate these two tuples and print the result.
print("Task 3 - Tuple concatenation")
odd_tuple = (1,3,5,7,9)
even_tuple = (2,4,6,8,10)
print(f"concatenation of {odd_tuple} and {even_tuple} tuples is {odd_tuple + even_tuple}")

# Task 4: Tuple Unpacking Write a program that defines a tuple containing the 
# dimensions of a rectangle (length and width). Then, unpack this tuple into 
# two variables and calculate the area of the rectangle.
print("Task 4 - Tuple unpack")
rect_dimension = (10,4)
print(f"rect dimension - {rect_dimension}")
length = rect_dimension[0]
width = rect_dimension[1]
print(f"length {length} and width {width} and area of rect is {length * width}")

#  Task 5: Check if an Element Exists Write a program that checks if a given element 
# exists in a tuple.
print("Task 5 - check if element exists")
task5_tuple = (45,55,66,77,88)
if 99 in task5_tuple:
    print(f"99 is present in {task5_tuple}")
else:
    print(f"99 not in {task5_tuple}")    


#  Task 6: Write a Python program to generate a bill for a supermarket purchase. The 
# program should store the items and their prices in a list of tuples. It should 
# then iterate over this list to print out each item along with its price. Finally, 
# calculate and print the total cost of all the items
#  Sample Input:
#  items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
#  Sample Output:
#  Item#  Price
# -------------------
#  Apple  99.00
#  Banana 99.00
#  Milk  49.00
# -------------------
# Total  247.0
print("Task 6 - Bill")
items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
total =0
print("-"*30)
print("\tItemized Bill")
print("-"*30)
print("\tItem\t Price")
print("-"*30)
for i,j in items:
    print(f"\t{i}\t {float(j)}")
    total+=j
print("-"*30)
print(f"\tTotal \t {float(total)}")
print("-"*30)
print("Thank you for shopping!!")
print("-"*30)
