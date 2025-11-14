#This code is to practice exception handling
num1 = int(input("Enter 1st integer value: "))
num2 = int(input("Enter 2nd integer value: "))
operation = input("Enter Operation: (A)dd/(S)ubtract/(M)ultiply/(D)ivide: ")
try:
    if operation.upper() == "A":
        print(f"Sum of {num1} and {num2} is {num1 + num2}")
    elif operation.upper() =='S'    :
        print(f"Difference of {num1} and {num2} is {num1 - num2}")
    elif operation.upper() == 'M'    :
        print(f"Product of {num1} and {num2} is {num1 * num2}")
    elif operation.upper() == 'D'    :
        print(f"Division of {num1} and {num2} is {num1 / num2}")
    else:
        print(f"Invalid operation selected {operation}")
except Exception as e:
    print(f"Exception {e} occurred")
