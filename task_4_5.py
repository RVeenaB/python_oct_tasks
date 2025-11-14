#Day2 fundamentals topics covered
'''
Following topics were covered
1. Comment - single line and multi line
2. Variables - rules, standards, case used (snake_case)
3. Datatypes - Int, float, string
4. data type conversion - implicit and explicit
5. Accept user inputs
'''

#comment - this is a single line comment
'''
this is a 
multi line
comment
comments are non executable lines of codes meaning they do not execute
'''

#variable - syntax is "var = value"
"""
variables are dynamical typed 
variables can start with _ or a character and never with a number.
variables can have alpha numeric charcters and only allowed special char is _
keywords/reserved words cannot be used as variable names
it denotes the memory location of the value stored
can be fetched using the function id(var)
"""
this_is_a_variable = "this is a value"
print(this_is_a_variable)
print("the memory location of this_is_a_variable is : ")
print(id(this_is_a_variable))

_is_this_valid = "yes _is_this_valid is a valid variable name"
print(_is_this_valid)
print("the memory location of _is_this_valid is : ")
print(id(_is_this_valid))

#datatypes - Integer
"""
to determine the datatype of a variable 
you can use the function "type(var)" function
"""
pythonlife_course_duration = 45
print("pythonlife_course_duration is ")
print(pythonlife_course_duration)
print(type(pythonlife_course_duration))

pythonlife_course_time_hrs = 2 * pythonlife_course_duration 
print("pythonlife_course_time_hrs is ")
print(pythonlife_course_time_hrs)
print(type(pythonlife_course_time_hrs))


#datatypes - float
total_bill = 45.50
amount_paid = 50
amount_balance = total_bill - 50
print(total_bill)
print(type(total_bill))
print(amount_balance) #negative value
print(type(amount_balance)) 

#datatypes - string
#used single quote
course_name = 'Basic to Advanced python programming' 
print("course name is : " + course_name)
print(type(course_name))

#used double quotes as there is ' in the text
instructor_name = "Instructor's name is Vasu Kumar" 
print("instructor's name is : " + instructor_name)
print(type(instructor_name))

#used triple quotes as there is ' in the text
institute_name = """Institute's name is "Python Life" """
print("institute's name is : " + institute_name)
print(type(institute_name))

#Datatype conversion - explicit
days_covered_in_course = "2"
print("days covered in course" + days_covered_in_course)
print(type(days_covered_in_course))
int_conv_days_completed = int(days_covered_in_course)
print("datatype conversion of days covered in course")
print(int_conv_days_completed)
print(type(int_conv_days_completed))

#user input
"""
this performs implicit datatype conversion where user input is always converted to string
"""
print("Enter the item cost: ")
item_cost = input()
print("Enter the amount paid: ")
cost_paid = input()
print("the balance is: ")
#this gives type error TypeError: unsupported operand type(s) for -: 'str' and 'str'
#balance_amt = item_cost - cost_paid
balance_amt = float(item_cost) - float(cost_paid)
print(balance_amt)