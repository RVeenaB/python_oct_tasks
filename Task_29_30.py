# Task1 Write a Python function square_all(numbers) that takes a list of numbers as input 
# and returns a new list containing the square of each number in the input list. 
# Use the # map() function with a lambda function to implement this.
#approach 1 - looping and function
# def square_all(num):
#     return(num**2)

# square_val = []
# list_1 = [10,2,5,8,9,3]
# for i in list_1:
#     square_val.append(square_all(i))

# print(f"list_ is {list_1} and square val is {square_val}")

#approach 2 - map function
# def square_all(num):
#     return(num**2)

# list_1 = [10,2,5,8,9,3]
# square_val = list(map(square_all, list_1))

# print(square_val)

#approach 3 - using lambda function
list_1 = [10,2,5,8,9,3]
square_val = list(map(lambda a: a**2,list_1))
print(square_val)

# task2 Write a Python function # filter_positive(numbers) that takes a list of numbers as 
# input and returns a new list containing only the positive numbers from the 
# input list. Use the  filter() function with a lambda function to implement this.
#approach 1 function and looping
# def filter_positive(numbers):
#     if numbers >= 0:
#         return(numbers)
# positive_list = []
# list_1 = [10,2,-5,-8,9,-3,0,100,-200,50]
# for i in list_1:
#     a = filter_positive(i)
#     if a != None:
#         positive_list.append(filter_positive(i))

# print(positive_list)

#approach 2 - filter function
# def filter_positive(numbers):
#         return(numbers>=0)

# list_1 = [10,2,-5,-8,9,-3,0,100,-200,50]
# print(list(filter(filter_positive,list_1)))
#approach 3 - filter function using lamda

list_1 = [10,2,-5,-8,9,-3,0,100,-200,50]
print(list(filter(lambda a:a>=0,list_1)))

# task3 Write a Python function calculate_factorial(n) that calculates the factorial of a 
# given number n. Use the  reduce() function with an appropriate lambda 
# function to implement this.
#approach1 - functino and loop
# def factorial(n):
#     decr_cnt = n
#     fact = 1
#     while decr_cnt > 1:
#         fact = decr_cnt * fact
#         decr_cnt -=1
#     return (fact) 

# user_in = int(input("enter a number"))
# print(f"factorial of {user_in} is {factorial(user_in)}")   

#approach2 - using reduce() function
# from functools import reduce
# user_in = int(input("enter a number"))
# fact_list = []
# for i in range(1,user_in + 1):
#     fact_list.append(i)
# fact = reduce(lambda x,y:x*y,fact_list)
# print(f"factorial of {user_in} is {fact}")   


#approach3 - using reduce(), lambda and consolidated loop
from functools import reduce
user_in = int(input("enter a number"))
fact_list = []
[fact_list.append(i) for i in range(1,user_in + 1) if i >1]
print(f"fact list {fact_list}")
fact = reduce(lambda x,y:x*y,fact_list)
print(f"factorial of {user_in} is {fact}")   

# task4 Write a Python function  count_vowels(string) that takes a string as input and 
# returns the count of vowels (a, e, i, o, u) in the input string. Use the 
# reduce()  function with an appropriate lambda function to implement this.
#approach 1 function
# def count_vowels(string):
#     vowels_list = ['a','e','i','o','u']
#     vowel_cnt = 0
#     for i in vowels_list:
#         vowel_cnt += string.count(i)
#     return(vowel_cnt)

# user_str = input("enter a sentence: ")
# print(f"number of vowels in {user_str} is {count_vowels(user_str)}")

#approach 2 lamda and reduce function
vowels_list = ['a','e','i','o','u']
user_str = input("enter a sentence: ").lower()

cnt = reduce(lambda cnt,vowel:cnt + user_str.count(vowel),vowels_list,0)
print(f"number of vowels in {user_str} is {cnt}")
