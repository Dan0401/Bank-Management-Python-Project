from pathlib import Path
import json
import random


class Bank:
    db_path = 'database.json'
    data = []
    try:
        if Path(db_path).exists():
            with open(db_path, 'r') as fs:
                print(fs.read())
                data = json.loads(fs.read())
        else:
            print("Database file does not exist.")


    except Exception as e:
        print(f"An error occured: {e}")

    @staticmethod
    def update_database(data):
        with open(Bank.db_path, 'a') as fs:
            fs.write(json.dumps(Bank.data))




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



