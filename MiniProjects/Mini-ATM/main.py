# This file handles registration, login, menu selection and saving account data.

# login for existing users 
# signin for new users

# parameter for signin

# name 
# bank_name
# bank_id
# account number
# pin

# create userid using combination of bankid+"-"+accountnumber

# create dictionary of dictionary  accounts ["user_id"]
# here accounts main dictionary and user_id another dectionary which carries all details of user accounts

# here we define a function for registration

def register(accounts):

    name = input("enter your name:")
    bank_id = input("enter bank id").upper() #conver the string into capitalcase
    bank_name = input("enter the bank name:")
    account_number = input("enter the bank account number:")
    pin = input("enter the pin:")

    # here we notice all data taken in the format of string 

    user_id = bank_id + "-"+account_number

    # here comes to edge cases
    # user have already account or pin restrictions

    if user_id in accounts:
        print("Account already exits!")
        return

    # for pin length must be 4 and digits not characters

    if len(pin)!=4 or not pin.isdigit():
        print("pin must contains exactly four digits")
        return

    # add the user detais to accounts dictionary

    accounts["user_id"] = {
        "name":name,
        "bank_id":bank_id,
        "bank_name":bank_name,
        "account_number":account_number,
        "pin":pin,
        "balance":500,  # default saving amount 
        "transactions":[]
    }

    save_accounts(accounts) # here save_accounts() funtion save acounts dict to json file 
    print("registration successful")



# now login

def login(accounts):
    bank_id = input("enter your bank id:").upper()
    account_number = input("enter your account number:")

    user_id = bank_id +"-"+account_number

    if user_id not in accounts:
        print("account not found")
        return None

    for attemps in range(3):

        pin = input("enter the pin:")

        if pin == accounts[user_id]["pin"]:
            print("login succesful")
            return accounts[user_id]
        else:
            print("incorrect pin")

    else:
        print("to mainy faild attemps ")
        return None

# here comes menu

def atm_menu(accounts,account):

    while True:

        print("========================================================================================================")
        print("============================================Mini ATM ====================================================")
        print(f" Welcome : {account["name"]}")

        print()
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Change PIN")
        print("6. Transfer Money")
        print("7. Logout")


        choice = input("enter the choice:")

        if choice == "1":
            check_balance(account)

        elif choice =="2":
            deposit(account)
            save_accounts(accounts)

        elif choice == "3":
            withdraw(account)
            save_accounts(accounts)

        elif choice =="4":
            transaction_history(account)

        elif choice =="5":
            change_pin(account)
            save_accounts(accounts)

        elif choice == "6":
            transfer(accounts,account) # here account as sender
            save_accounts(accounts)

        elif choice =="7":
            print("logged out successfully!")
            break
        else:
            print("invalid choice")


# progaram execution

accounts = load_accounts()
# load_accounts() function loads the json file


# main execution

while True:

    print("=======================================================================================================================")
    print("===============================================WELCOME==================================================================")

    print("1. REGISTER")
    print("2. LOGIN")
    print("3. EXIT")

    choice = input('enter your choice')

    if choice == "1":
        register(accounts)

    elif choice == "2":
        account = login(accounts)

        if account is not None:
            atm_menu(accounts,account)

    elif choice == "3":
        print("thank you for visitin miniATM")
        break
    else: 
        print("invalid choice")


            

        


