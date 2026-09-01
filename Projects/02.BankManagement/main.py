import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database)as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist")

    except Exception as err:
        print(f"an exception  occured as {err}")


    @staticmethod
    def update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @staticmethod

    


    def Createaccount(self):
        info ={
            "Name" : input("Tell your name :-"),
            "Age"  : int(input("Tell your age :-")),
            "Email": input("Tell your Email :-" ),
            "Pin"  : int(input("Tell your pin:-")),
            "AccountNo." : 1234,
            "Balance" : 0
        }
        if info['Age'] < 18 or len(str(info['Pin'])) != 4:
            print("sorry you cannot create your account")

        else:
            print("Account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number")

            Bank.data.append(info)
            Bank.update()



        

user = Bank()


print("Press 1 for creating an account")
print("Press 2 for depositing the money in the bank")
print("Press 3 for withdrawing the money")
print("Press 4 for details")
print("Press 6 for updating the details")

check = int(input("Tell your response:-"))


if check == 1:
    user.Createaccount()
