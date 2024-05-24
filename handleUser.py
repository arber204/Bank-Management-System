import uuid

user_table = {}

def add_user():
    name = input("Enter user name: ")
    balance = float(input("Enter initial balance: "))
    id = uuid.uuid1()
    user_table[name] = {"name": name, "balance": balance, "id": id}

def find_user():
    name = input("Insert your account name: ")
    user = user_table.get(name)
    if user:
        return user_table.get(name)

def delete_user():
    name = input("Enter user name to delete: ")
    if name in user_table:
        del user_table[name]
        print(f"User '{name}' deleted successfully.")
    else:
        print("User not found.")