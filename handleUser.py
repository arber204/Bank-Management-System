import uuid

user_table = {}

def add_user():
    while True:
        name = input("Enter user name: ")
        if name in user_table:
            print(f"'{name}' already exists in our database. Please
enter a unique name.")
        else:
            break

    balance = float(input("Enter initial balance: "))
    id = uuid.uuid1()
    user_table[name] = {"name": name, "balance": balance, "id": id}
    created_user = find_user(name)
    print('createduser', created_user)
    return created_user

def find_user(name):
    if not name:
        name = input("Insert your account name: ")
    user = user_table.get(name)
    if user:
        return user
    else:
        print(f"User '{name}' not found in the database.")
        return None

def delete_user():
    name = input("Enter user name to delete: ")
    if name in user_table:
        del user_table[name]
        print(f"User '{name}' deleted successfully.")
    else:
        print("User not found.")