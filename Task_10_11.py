# Task1: Vowel Checker: Write a Python program that takes a character as input 
# and checks whether it is a vowel or not. Use the if-else statement. 
#----------------------------------------------------------------------------
#task - 1 - vowel checker
# #----------------------------------------------------------------------------
print("----------------------------------------------------------------------------")
print("task - 1 - vowel checker")
print("----------------------------------------------------------------------------")
vowel_list = ['a','e','i','o','u']
user_char = input("Enter a character: ")

if (user_char in vowel_list): 
    print(f"""The user entered character "{user_char}" is a vowel.""")
else:
    print(f"""The user entered character "{user_char}" is a consonant.""")    

print("----------------------------------------------------------------------------")

# # Task2: Age Group Classification Write a program that takes an age as input and 
# # classifies the person into one of the following age groups: 
# # a)	Child: 0 - 12 years 
# # b)	Teenager: 13 - 17 years 
# # c)	Adult: 18 - 64 years 
# # d)	Senior: 65 years and older 

# #----------------------------------------------------------------------------
# #task - 2 - Age group classification
# #----------------------------------------------------------------------------
print("task - 2 - Age group classification")
print("----------------------------------------------------------------------------")
age_input = int(input("Please enter an age to know the age group: "))
# # approach 1 - if-elif-else
if age_input < 0:
    print(f"""The user entered invalid value "{age_input}", enter age above 0""")
elif age_input >= 65:
    print(f"""The user entered age "{age_input}" falls under "Senior" category.""")
elif age_input < 65 and age_input >= 18:
    print(f"""The user entered age "{age_input}" falls under "Adult" category.""")
elif age_input < 18 and age_input >= 13:
    print(f"""The user entered age "{age_input}" falls under "Teenager" category.""") 
else:
    print(f"""The user entered age "{age_input}" falls under "Child" category.""")

# Approach 2 - nested if
# if age_input > 0:
#     if age_input <= 12:
#         print(f"""The user entered age "{age_input}" falls under "Child" category.""")
#     elif age_input < 18:
#         print(f"""The user entered age "{age_input}" falls under "Teenager" category.""")
#     elif age_input < 64 :
#         print(f"""The user entered age "{age_input}" falls under "Adult" category.""")
#     else:
#         print(f"""The user entered age "{age_input}" falls under "Senior" category.""") 
# else:
#     print(f"""The user entered invalid value "{age_input}", enter age above 0""")
     
print("----------------------------------------------------------------------------")

# Task 3: Number Classifier: Write a program that takes an integer as input and 
# classifies it as positive, negative, or zero. Use the if-elif-else statement. 
#----------------------------------------------------------------------------
#task - 3 - Number classification
#----------------------------------------------------------------------------
print("task - 3 - Number classification")
print("----------------------------------------------------------------------------")
user_num = int(input("Please enter the number to be classified: "))
if user_num > 0:
    print(f"""User entered number "{user_num}" is a positive number.""")
elif user_num < 0:
    print(f"""User entered number "{user_num}" is a negative number.""")
else:
    print(f"""User entered number "{user_num}" is a value zero.""")        
print("----------------------------------------------------------------------------")

# Task 4: Leap Year Checker: Create a program that checks whether a given year is a 
# leap year or not. 
# A leap year is divisible by 4, but not by 100 unless it is divisible by 400. 
# Examples
# 2024: Divisible by 4 but not 100. Is a leap year.
# 1900: Divisible by 4 and 100, but not 400. Is not a leap year.
# 2000: Divisible by 4, 100, and 400. Is a leap year.
# 2100: Divisible by 4 and 100, but not 400. Will not be a leap year. 
#----------------------------------------------------------------------------
#task - 4 - Leap year checker
#----------------------------------------------------------------------------
print("task - 4 - Leap year checker")
print("----------------------------------------------------------------------------")
user_year = int(input("Enter the year: "))
if user_year%4==0:
    if user_year%100==0: 
        if user_year%400==0:
            print(f"""User entered year "{user_year}" is a leap year""")
        else:
            print(f"""User entered year "{user_year}" is not a leap year""")
    else:
        print(f"""User entered year "{user_year}" is a leap year""")
else:
    print(f"""User entered year "{user_year}" is not a leap year""")

print("----------------------------------------------------------------------------")

# Task 5: Calculator: Build a simple calculator program that takes two numbers 
# and an operator (+, -, *, /) as input and performs the corresponding operation. 
#----------------------------------------------------------------------------
#task - 5 - Calculator
#----------------------------------------------------------------------------
print("task - 5 - Calculator")
print("----------------------------------------------------------------------------")
user_input_1 = int(input("Enter first number: "))
user_input_2 = int(input("Enter second number: "))
user_operator = input("""Enter the operation you want to perform:" /
                          "+" for adding,
                          "-" for subtracting,
                          "*" for multiplying,
                          "/" for dividing. 
                          enter your selection: """)
if user_operator=="+":
    print(f"""You selected "{user_operator}" for Adding. The sum of the two numbers {user_input_1} and {user_input_2} is {user_input_1 + user_input_2}""")
elif user_operator == "-":
    print(f"""You selected "{user_operator}" for Subtracting. The difference of the two numbers {user_input_1} and {user_input_2} is {user_input_1 - user_input_2}""")
elif user_operator == "*":
    print(f"""You selected "{user_operator}" for Multplying. The product of the two numbers {user_input_1} and {user_input_2} is {user_input_1 * user_input_2}""")
elif user_operator == "/":
    print(f"""You selected "{user_operator}" for Dividing. The division of the two numbers {user_input_1} and {user_input_2} is {user_input_1 / user_input_2}""")
else:
    print(f"""You selected an invalid operation "{user_operator}" """)                  

print("----------------------------------------------------------------------------")

# Task 6: Short Hand If: Rewrite the following code using the short-hand if statement:
#  x = 8
# if x % 2 == 0: 
#     result = "Even" 
# else: 
#    result = "Odd" 
#----------------------------------------------------------------------------
#task - 6 - short hand if
#----------------------------------------------------------------------------
print("task - 6 - short hand if")
print("----------------------------------------------------------------------------")
x = 8
print(f"""short hand if equivalent of given code is ""even" if x % 2 == 0 else "odd"" and its result is {"even" if x % 2 == 0 else "odd"} """)
print("----------------------------------------------------------------------------")
# Task 7: Discount Calculator: Create a program that calculates the final price after 
# applying a discount. The program should take the original price and 
# the discount percentage as input. 
#----------------------------------------------------------------------------
#task - 7 - Discount calculator
#----------------------------------------------------------------------------
print("task - 7 - Discount calculator")
print("----------------------------------------------------------------------------")
product_cost = float(input("Enter the product price: "))
discount_pct = (int(input("Enter the discount to be applied: "))) / 100
print(f"""The product cost is {product_cost} and discount to be applied is {discount_pct * 100}%. 
The final product price is {product_cost-(product_cost*discount_pct)}""")

print("----------------------------------------------------------------------------")

# Task 8: BMI Calculator: Write a program that calculates the Body Mass Index (BMI) 
# using the formula: BMI = weight (kg) / (height (m))^2. 
# The program should take weight and height as input
#----------------------------------------------------------------------------
#task - 8 - BMI calculator
#----------------------------------------------------------------------------
print("task - 8 - BMI calculator")
print("----------------------------------------------------------------------------")
user_weight = float(input("Please enter the weight in Kgs: "))
user_height_mt = float(input("Please enter the height meters: "))
print(f"""For a weight (kg) of "{user_weight}" and height (mt) of "{user_height_mt}" 
      The BMI calculates to "{round(user_weight / (user_height_mt ** 2),2)}" """)                       
print("----------------------------------------------------------------------------")