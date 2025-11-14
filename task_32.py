class ATM():
    def __init__(self,user_name,user_list,trans_list):
        self.user_name = user_name
        self.user_list = user_list
        self.trans_list = trans_list
    # User defined functions
    # login method - User id and pswd validation method
    def login(self):
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
    def display(self):
        print("-"*50)
        print("\n")
        for i,j in trans_list.items():
            print(f"{i}\t{j.title()}")
        user_option = input("Select the transaction - 1,2,3,4 or 5: ")  
        return(user_option)

    # Deposit method - Deposits amount 
    def deposit(self,user_name):
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
    def balance(self,cur_bal):
        print("-"*50)
        print("Transaction: Balance Inquiry...")
        print("-"*50)
        print(f"Your current account balance is Rs. {float(cur_bal)} /-")

    # Withdraw method - Withdraw amount 
    def withdraw(self,user_name):
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
    def chg_pin(self, user_name):
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
    def logout(self,a):
        is_exit = input("Do you want to end transaction? yes or no - ").lower()
        if is_exit == "yes":
            print("** \t End of transaction..... \t **")
            print("-"*50)
            print(f"** Thank you {a} for banking with us. Have a good day! **")
            print("-"*50)
        else:
            return(is_exit)
    
#Main logic
print("*"*50)
print(f"**\t  Welcome to PythonLife Bank \t**\n")
print("*"*50)

#initialization
#user_list = {"usr1":1234,"usr2":1234,"usr3":1234} #userid:(pswd,balance)
#user_bal = {"usr1":500,"usr2":8000,"usr3":2000} #userid:balance
# user_list = {"usr1":[1234,40],"usr2":[1234,50],"usr3":[1234,60]} #userid:[pswd,balance]
# trans_list = {1:"balance inquiry",2:"deposit",3:"withdraw",4:"change pin",5:"exit"}

# initialization
user_name = ""
#userid:[id,pswd,balance,name]
user_list = {"usr1":["usr1",1234,40,"User One"],"usr2":["usr2",1234,50,"User Two"],"usr3":["usr3",1234,60,"User Three"]} 
trans_list = {1:"balance inquiry",2:"deposit",3:"withdraw",4:"Change pin",5:"exit"}

atm_obj = ATM(user_name,user_list,trans_list)

user_dtl = atm_obj.login()  
user_option = atm_obj.display()
if user_option.isdigit and int(user_option) in range(0,6):
    while True:
        if user_option == "1":
           # print(f"Your current account balance is Rs {user_dtl[1]}")
            atm_obj.balance(user_dtl[2])
            next_transaction = input("Do you want to do another transaction? yes or no - ").lower()
            if next_transaction == "yes":
                user_option = atm_obj.display()
            else:
                end_of_transaction = atm_obj.logout(user_dtl[3])
                if end_of_transaction == "no":
                    continue
                else:
                    break   
        elif user_option == "2":
            user_update = atm_obj.deposit(user_dtl[0])     
            next_transaction = input("Do you want to do another transaction? yes or no - ").lower()
            if next_transaction == "yes":
                user_option = atm_obj.display()
            else:
                end_of_transaction = atm_obj.logout(user_dtl[3])
                if end_of_transaction == "no":
                    continue
                else:
                    break   
        elif user_option == "3":
            user_update = atm_obj.withdraw(user_dtl[0])     
            next_transaction = input("Do you want to do another transaction? yes or no - ").lower()
            if next_transaction == "yes":
                user_option = atm_obj.display()
            else:
                end_of_transaction = atm_obj.logout(user_dtl[3])
                if end_of_transaction == "no":
                    continue
                else:
                    break      
        elif user_option == "4":
            user_update = atm_obj.chg_pin(user_dtl[0])     
            next_transaction = input("Do you want to do another transaction? yes or no - ").lower()
            if next_transaction == "yes":
                user_option = atm_obj.display()
            else:
                end_of_transaction = atm_obj.logout(user_dtl[3])
                if end_of_transaction == "no":
                    continue
                else:
                    break                      
        if user_option == "5":
            end_of_transaction = atm_obj.logout(user_dtl[3])
            if end_of_transaction == "no":
                continue
            else:
                break