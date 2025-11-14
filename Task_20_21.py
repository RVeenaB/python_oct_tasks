# Problem: You are given a string Example: sentence . Print the characters at even indices. 
# sentence = "Python is amazing" 
# # Output: "Pto saaig" 
print("*"*50)
print("Task 1 - print characters at even indices")
#sentence = "Python is amazing" 
sentence = input("Please enter a string: ")
print(f"characters at even indices of {sentence} is {sentence[::2]}")
print("*"*50)

# Problem: You are given a string s . 
# Replace all spaces in the string with underscores ( and print the modified string. Example: s = "Python is fun and powerful" 
#  Output: "Python_is_fun_and_powerful" _ ) 
print("*"*50)
print("Task 2 - replace spaces in string with underscore")
task2_sentence = input("please enter a string with spaces: ")
print(f"Original Sentence is {task2_sentence} ")
print(f"Replaced spaces with underscore is {task2_sentence.replace(' ','_')}")
print("*"*50)

# Problem: You are given a string Example: s = "12345" Check if the string contains only digits. 
print("*"*50)
print("Task 3 - check if string contains only digits")
task3_input = input("please enter string to validate if it has digits: ")
print(f"Does user entered string {task3_input} have only digits? {task3_input.isdigit()}")
print("*"*50)

# Problem: You are given a string. Print the string in reverse order. 
# s = "Python is amazing" #
# Output: "gnizama si nohtyP 
print("*"*50)
print("Task 4 - reverse order")
task4_sentence = input("Please enter a string: ")
print(f"Reverse of the user entered string {task4_sentence} is {task4_sentence[-1::-1]}")
print("*"*50)

# Problem: You are given a string s . 
# Capitalize the first letter of each word in the string and print the modified string. Example: s = "python programming is fun" 
# Output: "Python Programming Is Fun
print("*"*50)
print("Task 5 - capitalize first letter of each word in the string")
task5_sentence = input("Please enter a string in lower case: ")
print(f"String entered is {task5_sentence} and camel case of it is {task5_sentence.title()}")
print("*"*50)

