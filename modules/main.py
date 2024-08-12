from reg import register
from tab import table
from upd import update
from dele import delete
from ext import exit
data = []

while True:
    print("1. Add \n2. View \n3. Update \n4. Delete \n5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        register(data)
    elif ch == 2:
        table(data)
    elif ch == 3:
        update(data)
    elif ch == 4:
        delete(data)
    elif ch == 5:
        exit(data)