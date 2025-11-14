# Task 1: Dictionary Update Write Python code to add a new key-value pair to the following dictionary: 
# my_dict = {'name': 'python', 'age': 25} 
# # Your code here # Output should be: {'name': 'python', 'age': 25, 'city': 'we st godavari'} 
print("*"*50)
print("Task 1 - add a new key-value pair")
task1_dict = {'name': 'python', 'age': 25} 
print(f"original dictionary is {task1_dict}")
#approach 1: using square brackets []
task1_dict['city'] = 'west godavari'
print(f"Updated dictionary is {task1_dict}")

#approach 2: update method
# task1_dict2 = {'city':'west godavari'}
# task1_dict.update(task1_dict2)
# print(f"seocond dictionary is {task1_dict2}")
# print(f"Updated dictionary is {task1_dict}")
print("*"*50)

# Task 2: Dictionary Access Write Python code to access and print the value associated with the key 'price' in the following dictionary: 
# product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1 200} 
# # Your code here # 
# Output should be: 1200 
print("*"*50)
print("Task 2 - to access and print value with key 'price'")
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200} 
print(f"product info dict details - {product_info}")
#approach 1 - using square brackets []
print(f"Value of the key 'price' is {product_info['price']}")
#approach 2 - using value method
# print(f"Value of the key 'price' is {product_info.get('price')}")

print("*"*50)
# Task 3: Dictionary Removal Write Python code to remove the key-value pair with the key 'city' from the 
# following dictionary: my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'} 
# # Your code here # 
# Output should be: {'name': 'John', 'age': 30}
print("*"*50)
print("Task 3 - remove a new key-value pair")
task3_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'} 
print(f"original dict {task3_dict}")
removed_key_value = task3_dict.pop('city')
print(f"after removal of key city and its value {removed_key_value} dict is  {task3_dict}")
print("*"*50)
#  Task 4: Dictionary Keys Write Python code to print all the keys present in the following dictionary: 
# my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'} 
# # Output should be: ['name', 'age', 'city'] 
print("*"*50)
print("Task 4 - print all the keys ")
task4_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'} 
print(f"original dict: {task4_dict} and its keys are {task4_dict.keys()}")

print("*"*50)
# Task 5: Dictionary Values Write Python code to print all the values present in the following dictionary: 3 
# my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
# Output should be: ['python', 25, 'tanuku'] 
print("*"*50)
print("Task 5 - print values of dict")
task5_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(f"original dict: {task5_dict} and its values are {task4_dict.values()}")
print("*"*50)


task5_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
