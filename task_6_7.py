#fundamentals day 2 tasks
"""
Tasks given
1. comments 
2. print stmt
3. data structure and data types 
4. string operation
5. keyword
6. variables
7. type conversion
8. simple input and output
"""

#----------------------------------------------------------------------------
#task - 1 - comments
#----------------------------------------------------------------------------
print("task - 1.1 - single line and multi line comments")
#Course Day2 fundamentals Day 1 topics covered
'''
Following topics were covered
Topics covered in day2:
1.  Types of datatyopes - mutable, immutable
2.  Datatypes and definitions - 
    a) List, 
    b) set, 
    c) tuple, 
    d) dictionary, 
    e) boolean, 
    f) complex
'''
print("task - 1.2 - create a simple task and add comments")
#code to swap two numbers without a third variable
#accept two numbers from user to swap
print("enter first number: ")
user_input_1 = input()
print("enter second number: ")
user_input_2 = input()
print("User_input_1 before swap is " + str(user_input_1))
print("User_input_2 before swap is " + str(user_input_2))
#swap logic
user_input_1,user_input_2=user_input_2,user_input_1
print("User_input_1 after swap is " + str(user_input_1))
print("User_input_2 after swap is " + str(user_input_2))
print("----------------------------------------------------------------------------")

#----------------------------------------------------------------------------
#task - 2 - Print stmt
#----------------------------------------------------------------------------
print("task - 2.1 - print your name")
#printing my name
print("My name is : Veena")
print("task - 2.2 - print a pattern")
#displaying a pattern
print("**********************")
print("*     PYTHON LIFE    *")
print("* Fundamentals Day 2 *")
print("*        Tasks       *")
print("**********************")
print("----------------------------------------------------------------------------")
#----------------------------------------------------------------------------
#task - 3 - data structure and datatype
#----------------------------------------------------------------------------
print("task - 3.1 - define list with different datatypes")
new_list = ["this is a list with different datatypes ",  #string
            -3,                                          #int
            45.52,                                       #float
            ["inner list",2,2,2],                        #list
            {33,44,55,"abc"},                            #set
            (21,"xyz",89.0),                             #tuple
            {1:"this",2:"is",3:"a",4:"dictionary"},      #dict
            True,                                        #boolean
            8 + 8j                                       #complex
            ]
print(new_list)
print("task - 3.2 - define set with employee ids")
new_set = {1000,1001,1002,1003,1004,1005}
print("This is a set of employee ids " + str(new_set))
print("task - 3.3 - dictionary to store book information")
new_dict = {
            "title":"The immortals of Meluha",
            "author":"Amish Tripathi",
            "publication year":"2010"
            }
print("This is a dictionary to store book information " + str(new_dict))
print("----------------------------------------------------------------------------")
#----------------------------------------------------------------------------
#task - 4 - String operations
#----------------------------------------------------------------------------
print("task - 4.1 - concatenate two strings")
first_string = "This is first string "
print(first_string)
second_string = 'This is second string'
print(second_string)
concate_string = first_string + " " + second_string
print("this is concate string " + concate_string)

print("task - 4.2 - repeat a string three times and print")
task_four = "String "
#print(task_four + " " + task_four + " " + task_four)
print(task_four*3)

print("task - 4.3 - accept input and convert to float")
print("enter a numeric value: ")
user_input_3 = input()
print("user entered - " + user_input_3 + " and its datatype is " + str(type(user_input_3)))
#convert input to float
conv_input_3 = float(user_input_3)
print("converted user input to " + str(conv_input_3) + " and its converted datatype is" + str(type(conv_input_3)) )

print("task - 4.4 - accept two names and concat")
print("enter first name")
first_name = input()
print("enter last name")
last_name = input()
full_name = first_name + " " + last_name
print("full name is " + full_name)
print("----------------------------------------------------------------------------")

#----------------------------------------------------------------------------
#task - 5 - keywords
#----------------------------------------------------------------------------
print("task 5.1 use a keyword as a variable name and observe")
#True = "boolean keyword"  throws SyntaxError: cannot assign to True
#print = "print keyword" throws typeerror 'str' object is not callable
print("----------------------------------------------------------------------------")

#----------------------------------------------------------------------------
#task - 6 - variables
#----------------------------------------------------------------------------
print("task 6.1 declare int and string variable and display")
employee_name = "employee name"
employee_age = 35
print("string variable is "+ employee_name + " int variable is "+ str(employee_age))
print("----------------------------------------------------------------------------")

#----------------------------------------------------------------------------
#task - 7 - type conversion
#----------------------------------------------------------------------------
print("task 7.1 Convert a float to an integer and print the result")
employee_salary = 15000.4554
int_emp_sal = int(employee_salary)
print("Float value is " + str(employee_salary) + " whose datatype is " + str(type(employee_salary)))
print("converted value is " + str(int_emp_sal) + " whose datatype is " + str(type(int_emp_sal)))

print("task 7.1 Convert an integer to a string and display the output.")
str_emp_sal = str(int_emp_sal)
print("Integer value is " + str(int_emp_sal) + " whose datatype is " + str(type(int_emp_sal)))
print("converted value is " + str(str_emp_sal) + " whose datatype is " + str(type(str_emp_sal)))

print("----------------------------------------------------------------------------")
#----------------------------------------------------------------------------
#task - 8 - type conversion/input output
#----------------------------------------------------------------------------

print("task 8.1 take user input for age, converts it to an integer, add 5, and then print the result")
print("enter your age: ")
user_age = input()
print("user entered age is " + user_age + " and type is " + str(type(user_age)))
int_usr_age = int(user_age)
print("converted entered age is " + str(int_usr_age) + " and type is " + str(type(int_usr_age)))
modified_age = int_usr_age + 5
print("modified age is " + str(modified_age) + " and type is " + str(type(modified_age)))

print("task 8.2 take two numbers as input, compute the product then print the result")
print("enter the first number")
first_num = int(input())
print("enter the second number")
second_num = int(input())
product_of_numbers = first_num * second_num
print("first number is " + str(first_num) + " second number is " + str(second_num) + " and the product is " + str(product_of_numbers))
print("----------------------------------------------------------------------------")