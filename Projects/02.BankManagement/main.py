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

    


    def Createaccount(self):
        pass

user = Bank()


print("Press 1 for creating an account")
print("Press 2 for depositing the money in the bank")
print("Press 3 for withdrawing the money")
print("Press 4 for details")
print("Press 6 for updating the details")

check = int(input("Tell your response:-"))


if check == 1:
    user.Createaccount()
