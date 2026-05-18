from pathlib import Path
import json
import random


class Bank:
    db_path = 'database.json'
    data = []
    try:
        if Path(db_path).exists():
            with open(db_path, 'r') as fs:
                data = json.loads(fs.read())
        else:
            print("Database file does not exist.")


    except Exception as e:
        print(f"An error occured: {e}")

    @staticmethod
    def update_database(data):
        with open(Bank.db_path, 'w') as fs:
            fs.write(json.dumps(data))
            fs.flush()  #Force Windows/Python to immediately write the data to the file disk




    def create_account(self):
        info  = {
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "gender": input("Enter your gender 'M' or 'F' or 'NA': "),
            "account_number": random.randint(1000000000, 9999999999),
            "mobile_number": input("Enter your mobile number: "),
            "email": input("Enter your email: "),
            "balance": 0

        }
        if info['age'] < 18:
            print("Sorry, you must be at least 18 years old to create an account.")
        elif info['age'] > 100:
            print("Sorry, you must be less than 100 years old to create an account.")
        elif len(info['mobile_number']) != 10:
            print("Sorry, mobile number must be 10 digits long.")
        elif '@' not in info['email'] or '.' not in info['email']:
            print("Sorry, email must be valid.")
        elif info['gender'] not in ['M', 'F', 'NA']:
            print("Gender can only be M, F or NA.")
        else:

            print("Please validate your information:")
            for key, value in info.items():
                print(f"{key}: {value}")
            confirm = input("Is the information correct? (Y/N): ")
            if confirm.upper() == 'Y':
                Bank.data.append(info)
                Bank.update_database(Bank.data)
                print("Account created successfully!")
            else:
                print("Account creation cancelled.")


    def deposit_money(self):
        search_account_number = int(input("Enter the account number to deposit money into: "))
        target_account_details = {}

            #Loop through the list of dictionaries directly
        for accounts_dict in Bank.data:
                #Check the key for the current dictionary against the search account number
            if accounts_dict["account_number"] == search_account_number:
                target_account_details = accounts_dict
        
                deposit_amt = int(input("Enter the deposit amount: "))
                target_account_details["balance"] += deposit_amt
        
                # Print the transaction details and update the database
                print(f"Transaction successful: you have deposited Rs. {deposit_amt}. New balance: Rs. {target_account_details['balance']}")
                Bank.update_database(Bank.data)
                # 3. Stop looping since we found the account!
                break 
                
        # 4. If the loop finishes and target_account_details is still empty
        if not target_account_details:
            print("Account not found")




Bankobj = Bank()

print("Welcome to the Dan's Bank Management System")
print("Please select an option:")
print("1. Create a new account")
print("2. Deposit money")
print("3. Withdraw money")
print("4. Check balance")
print("5. Update account information")

option = input("Enter your choice (1-5): ")

if option == '1':
    Bankobj.create_account()

elif option == '2':
    Bankobj.deposit_money()



