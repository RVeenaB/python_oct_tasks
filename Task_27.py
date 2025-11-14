# Task 1: Add Function #  Write a Python function named add takes two arguments a and  b and 
# returns their sum.
def add(a,b):
    sum = a + b
    return (sum)
print(f"sum of 20 and 30 is {add(20,30)} ")
#  Task 2: Square Function add that takes a number x as input and  returns its square.
def square(x):
    return(x**2)
print(f"square of 10 is {square(10)}")
#  Task 3: Factorial Function  Write a Python function named input and returns its factorial.
#  factorial that takes a positive integer 
def factorial(n):
    if n < 0:
        return(f" Negative number {n} cannot be factored!")
    elif n == 0:
        return(f"n! of {n} is 1")
    else:
        calc_factorial = 1
        for i in range(1,n+1):
            calc_factorial *= i
        return(f"{n}! is {calc_factorial}")    
    
print(factorial(-1))

# Task 4: Maximum Function Write a Python function named  maximum that 
# takes a list of numbers as input and returns the maximum value in the list.
def maximum(num_list):
    max_num = 0
    for i in num_list:   
        if i > max_num:
           max_num = i
    return(max_num)

input_list = [10,20,400,5,6000]
print(f"maximum number in the list {input_list} is {maximum(input_list)}")         
#  Task 5: Reverse Function  Write a Python function named reverse that takes a string 
# returns its reverse.
def reverse(input):
    return(input[-1::-1])

input_str = "python life"
print(f"reverse of string {input_str} is {reverse(input_str)}")
#  Task 6: Check Prime Function  Write a Python function named as is_prime and 
# that takes a positive integer n as input and returns True if n is prime, otherwise returns false
def is_prime(n):
    if n <= 1:
        return(False)
    elif n == 2:
        return(True)
    else:    
        for i in range(2,n):
            if n % i != 0:
                return(True)
            else:
                return(False)

usr_input = 4
print(f"Is {usr_input} a prime number? {is_prime(usr_input)}")
# Task 7: Fibonacci Function  Write a Python function named fibonacci
# that takes a positive integer n as n th Fibonacci number.
# f(n) = f(n-1) + f(n-2)
def fibonacci(n):
    fib_list = []
    nth_val_2 = 0
    nth_val_1 = 1
    fib_list.append(nth_val_2)
    fib_list.append(nth_val_1)
    for i in range(1,n):
        nth_val_0 = nth_val_1 + nth_val_2
        nth_val_2 = nth_val_1
        nth_val_1 = nth_val_0
        fib_list.append(nth_val_1)
    return(fib_list)

print(f"Fibonacci series till {10} is {fibonacci(10)}")

#  Task 8: Palindrome Function  Write a Python function named  is_palindrome that takes a string 
# returns True if it is a palindrome, otherwise false
def is_palindrome(input_str):
    reverse_input = input_str[-1::-1]
    print(f"{reverse_input} and {input_str} ")
    print(f" spaces replaced {reverse_input.replace(' ','')} and {input_str.replace(' ','')} ")
    if input_str.replace(' ','').lower() == reverse_input.replace(' ','').lower():
        return(True)
    else:
        return(False)

input_str = "nurses run"
print(f"Is the string {input_str} palindrome? {is_palindrome(input_str)}")

# Task 9: Sum of Squares Function Write a Python function named 
#  sum_of_squares that takes a list of numbers as 
# input and returns the sum of the squares of those numbers.
def sum_of_square(num_list):
    sum = 0
    for i in num_list:
        sum += (i**2)
    return(sum)

num_list = [10,20,30,40]
print(f"sum of squares of list {num_list} is {sum_of_square(num_list)}")


#  Task 10: Average Function
# average that takes a list of numbers as input and 
# Write a Python function named returns the average value
def average(num_list):
    avg = 0
    sum = 0
    for i in num_list:
        sum += i
    avg = sum/len(num_list)
    return(avg)
num_list = [10,20,30,40]
print(f"Average of {num_list} with {len(num_list)} elements is {average(num_list)}")

