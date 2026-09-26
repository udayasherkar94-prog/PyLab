
from datetime import datetime


def add_transaction(account, message):
    time = datetime.now().strftime("%d-%m-%Y %H:%M")
    account["transactions"].append(f"{time} - {message}")


def check_balance(account):
    print("Your balance: Rs.", account["balance"])


def deposit(account):
    amount = int(input("Enter deposit amount: "))

    if amount <= 0:
        print("Enter a valid amount.")
    else:
        account["balance"] += amount
        add_transaction(account, f"Deposited Rs. {amount}")

        print("Money deposited successfully!")
        check_balance(account)


def withdraw(account):
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Enter a valid amount.")

    elif amount <= account["balance"]:
        account["balance"] -= amount
        add_transaction(account, f"Withdrawn Rs. {amount}")

        print("Withdrawal successful!")
        check_balance(account)

    else:
        print("Insufficient balance!")


def transaction_history(account):
    if len(account["transactions"]) == 0:
        print("No transactions found.")
    else:
        for transaction in account["transactions"]:
            print(transaction)


def change_pin(account):
    old_pin = input("Enter current PIN: ")

    if old_pin == account["pin"]:
        new_pin = input("Enter new 4-digit PIN: ")

        if len(new_pin) == 4 and new_pin.isdigit():
            account["pin"] = new_pin
            print("PIN changed successfully!")
        else:
            print("PIN must contain exactly 4 digits.")
    else:
        print("Incorrect PIN!")


def transfer(accounts, sender):
    bank_id = input("Enter receiver bank ID: ").upper()
    account_number = input("Enter receiver account number: ")

    receiver_id = bank_id + "-" + account_number

    if receiver_id not in accounts:
        print("Receiver account not found!")
        return

    receiver = accounts[receiver_id]

    if receiver is sender:
        print("Cannot transfer money to the same account.")
        return

    amount = int(input("Enter transfer amount: "))

    if amount <= 0:
        print("Enter a valid amount.")

    elif amount > sender["balance"]:
        print("Insufficient balance!")

    else:
        sender["balance"] -= amount
        receiver["balance"] += amount

        add_transaction(
            sender, f"Sent Rs. {amount} to {receiver_id}"
        )

        add_transaction(
            receiver, f"Received Rs. {amount} from {sender['bank_id']}-{sender['account_number']}"
        )

        print("Transfer successful!")
        check_balance(sender)

