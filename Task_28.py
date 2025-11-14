#global variables initialization
user_name = ""
#userid:[id,pswd,balance,name]
user_list = {"usr1":["usr1",1234,40,"User One"],"usr2":["usr2",1234,50,"User Two"],"usr3":["usr3",1234,60,"User Three"]} 
trans_list = {1:"balance inquiry",2:"deposit",3:"withdraw",4:"Change pin",5:"exit"}

# User defined functions
# login method - User id and pswd validation method
def login():
    global user_name
    user_name = input("Enter login user id: ").lower()
    if user_name in user_list:
        user_dtl = user_list[user_name]
        user_in_pswd = input("Enter login password: ").lower()
        if user_in_pswd.isdigit and int(user_in_pswd) == user_dtl[1]:
            print("-"*50)
            print(f"** \t\t Welcome {user_list[user_name][3].title()} \t\t **")
            print("-"*50)
            return user_dtl
        else:    
            print(f" Invalid login - Incorrect password")
    else:
        print(" Invalid Login - User Id does not exist")

# Display method - Displays the transaction options
def display():
    print("-"*50)
    print("\n")
    for i,j in trans_list.items():
        print(f"{i}\t{j.title()}")
    user_option = input("Select the transaction - 1,2,3,4 or 5: ")  
    return(user_option)

# Deposit method - Deposits amount 
def deposit(user_name):
    global user_list
    print("-"*50)
    print("Transaction: Deposit...")
    print("-"*50)
    deposit_amt = float(input("Please enter the amount to deposit: Rs "))
    
    if user_name in user_list:      
        usr_dtl = user_list[user_name]
        print(f"Previous balance of {user_list[user_name][3]}: Rs. {float(usr_dtl[2])} /-")
        user_list[user_name][2] += deposit_amt 
        print(f"New balance of {user_list[user_name][3]}: Rs. {float(user_list[user_name][2])} /-")

    return(usr_dtl)

# Balance method - Balance inquiry 
def balance(cur_bal):
    print("-"*50)
    print("Transaction: Balance Inquiry...")
    print("-"*50)
    print(f"Your current account balance is Rs. {float(cur_bal)} /-")

# Withdraw method - Withdraw amount 
def withdraw(user_name):
    global user_list
    print("-"*50)
    print("Transaction: Withdraw...")
    print("-"*50)
    withdraw_amt = float(input("Please enter the amount to Withdraw: Rs "))
    
    if user_name in user_list:      
        usr_dtl = user_list[user_name]
        if usr_dtl[2] < withdraw_amt:
            print(f"Withdraw amount Rs. {withdraw_amt} exceeds current balance Rs. {usr_dtl[2]} /-")
        else:    
            print(f"Previous balance of {user_list[user_name][3]}: Rs. {float(usr_dtl[2])} /-")
            user_list[user_name][2] -= withdraw_amt 
            print(f"New balance of {user_list[user_name][3]}: Rs. {float(user_list[user_name][2])} /-")

    return(usr_dtl)    

# chg_pin method - Changes the login password
def chg_pin(user_name):
    global user_list
    print("-"*50)
    print("Transaction: Change Pin...")
    print("-"*50)
    new_pin = int(input("Please enter the new four digit pin: "))
    
    if user_name in user_list:      
        usr_dtl = user_list[user_name]
        if usr_dtl[1] == new_pin:
            print(f"New pin matches existing. Existing pin retained!")
        else:    
            usr_pin_confirm = input("Do you want to change pin? yes or no ")
            if usr_pin_confirm == "yes":
                user_list[user_name][1] = new_pin 
                print(f"Pin successfully updated!! ")
            else:
                print(f"Pin update cancelled. Existing pin retained!")
    return(usr_dtl)    

# Logout method - Logout  
def logout(a):
    is_exit = input("Do you want to end transaction? yes or no - ").lower()
    if is_exit == "yes":
        print("** \t End of transaction..... \t **")
        print("-"*50)
        print(f"** Thank you {a} for banking with us. Have a good day! **")
        print("-"*50)
    else:
        return(is_exit)