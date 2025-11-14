# Task 1: Reverse List: Write Python code to reverse the order of elements in the given list 
# Print the reversed list. my_list = [10, 20, 30, 40, 50, 11] 
# # Output should be: [11,50,40,30,20,10] 
print("*"*50)
print("Task 1 - reverse list")
my_list = [10, 20, 30, 40, 50, 11] 
print(f"original list is {my_list}")
my_list.reverse()
print(f"reversed list is {my_list}")
print("*"*50)

# Task 2: Common Elements: Given two lists them. list1 and list2 , 
# find and print the common elements between list1 = [1, 2, 3, 4, 5] list2 = [4, 5, 6, 7, 8] 
# # Output should be: [4, 5] 
print("*"*50)
print("Task 2 - common elements")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(f"List1 is: {list1}")
print(f"List2 is: {list2} ")
common_list = []
for i in list1:
    for j in list2:
        if i == j:
            common_list.append(i)
print(f"common list is {common_list}")            
print("*"*50)

# Task 3: Unique Elements: Create a new list unique_list containing only the unique elements from the given list original_list . 
# Print the unique list. original_list = [1, 2, 2, 3, 4, 4, 5] 
# Output should be: [1, 2, 3, 4, 5] 
print("*"*50)
print("Task 3 - unique elements")
original_list = [1, 2, 2, 3, 4, 4, 5] 
unique_list = []
#approach 1
# count = 0
# for i in original_list:
#     count = original_list.count(i)
#     print(f"element {i} occurs {count}")
#     if (count == 1) or (count > 1 and i not in unique_list):
#        unique_list.append(i)
#     else:
#         continue    
#approach 2
# for i in original_list:
#     if i not in unique_list:    
#         unique_list.append(i)
#     else:
#         continue    
# print(f"unique list is {unique_list}")    
#consolidated approach
print(f"original list is {original_list}") 
[unique_list.append(i) for i in original_list if i not in unique_list]
print(f"unique list is {unique_list}")  

print("*"*50)
# Task 4: Remove Duplicates: Remove duplicate elements from the given list without duplicates while preserving the order. 
# duplicated_list and print the list duplicated_list = [1, 2, 2, 3, 4, 4, 5] 
# Output should be: [1, 2, 3, 4, 5] 
print("*"*50)
print("Task 4 - remove duplicate same as task 3")
print(f"original list is {original_list}") 
[unique_list.append(i) for i in original_list if i not in unique_list]
print(f"unique list is {unique_list}")  
print("*"*50)
# Exercise 1- List Concatenation  Write a Python script that concatenates two lists and prints the result. 
print("*"*50)
print("Task 5 - list concatenation")
task5_list1 = [1, 2, 3, 4, 5]
task5_list2 = [4, 5, 6, 7, 8]
task5_list1_copy = task5_list1.copy()
print(f"first list is {task5_list1}")
print(f"second list is {task5_list2}")
# print(f"concatenated list is {task5_list1.extend(task5_list2)}")  --> why did this not work
task5_list1.extend(task5_list2)
print(f"concatenated list is {task5_list1}")  
print(f"copy of list1 is {task5_list1_copy}")

#approach2
# for i in task5_list2:
#     task5_list1.append(i)
# print(f"concatenated list is {task5_list1}")


print("*"*50)
# Exercise 2 - List Repetition Write a Python script that repeats a list three times and prints the result. 
print("*"*50)
print("Task 6 - List repetition")
task6_list = [1,2,3]
repeat_list = []
i = 1
while i<= 3:
    repeat_list.append(task6_list) # if we use extend it is repeating as elements
    i+=1
print(f"repeat list {repeat_list}")    

print("*"*50)
# Exercise 3 - List Removal Write a Python script that removes the elements at even indices from a list. 
print("*"*50)
print("Task 7 - list removal")
task7_list = [10,20,30,40,50,60,70,80]
print(f"original list is {task7_list}")
print(f"elements at even indices {task7_list[::2]}")

print("*"*50)
# Exercise 4 - List Insertion Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of a list
print("*"*50)
print("Task 8 - list insertion")
task8_list = ["this","is","task7","list"]
print(f"original list is {task8_list}")
task8_list.insert(0,10)
print(f"list after appending number 10 at begining {task8_list}")
task8_list.insert(0,11)
print(f"list after appending number 11 at begining {task8_list}")
task8_list.insert(0,12)
print(f"list after appending number 12 at begining {task8_list}")

print("*"*50)
#  List comprehensions 
# 1 Square Numbers - Create a list of squares of numbers from 1 to 10. 
print("*"*50)
print("Task 9 - Create list of squares of num from 1 to 10")
task9_list = []
# for i in range(1,11):
#     task9_list.append(i**2)
[task9_list.append(i**2) for i in range(1,11) ]
print(f"square list of nums from 1 to 10 is {task9_list}")

print("*"*50)
# 2 Even Numbers - Generate a list of even numbers from 1 to 20. 
print("*"*50)
print("Task 10 - generate list of even numbers from 1 to 20")
task10_list = []
[task10_list.append(i) for i in range(1,21) if i%2 == 0]
print(f"even numbers from 1 to 20 {task10_list}")

print("*"*50)
# 3. Words Lengths - Given a list of words, create a list containing the lengths of each word. words = ["apple", "banana", "cherry", "date"]
print("*"*50)
print("Task 11 - word length in a list")
words = ["apple", "banana", "cherry", "date"]
print(f"original list is {words}")
task11_list = []
[task11_list.append(len(i)) for i in words]
print(f"lengths of list of words {words} is {task11_list}")
print("*"*50)