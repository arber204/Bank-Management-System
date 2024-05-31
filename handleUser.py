import uuid

user_table = {}

def add_user(name):
    while True:
        balance = input("Enter initial balance: ")
        try:
            balance = float(balance)
            break
        except:
            print(' << ATTENTION >> Insert only a number please!')
    id = uuid.uuid1()
    user_table[name] = {"name": name, "balance": balance, "id": id}

def find_user(name):
    user = user_table.get(name)
    if user:
        print(f"|  Name: {user['name']}|  Balance: ${user['balance']}")
    else:
        print(f"User '{name}' does not exist in the database.")
    return user

def delete_user(name):
    while True:
        if name in user_table:
            del user_table[name]
            print(f"User '{name}' deleted successfully.")
            break
        else:
            print(f"User '{name}' does not exist in the database.")