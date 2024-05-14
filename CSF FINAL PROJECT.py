import uuid

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# Create a hash table to store user information
user_table = {}

# Create a queue to maintain the order of users
queue = Queue()

def add_user():
    name = input("Enter user name: ")
    balance = float(input("Enter initial balance: "))
    # Generate a unique ID
    id = uuid.uuid1()  # Simple way to generate unique ID (not very secure)
    # Store user information in hash table
    user_table[name] = {"balance": balance, "id": id}
    # Enqueue user into Queue
    queue.enqueue((name, id))

def find_user(name):
    return user_table.get(name)

def deposit_money():
    name = input("Enter user name: ")
    amount = float(input("Enter amount to deposit: "))
    user = find_user(name)
    if user:
        user['balance'] += amount
        print(f"Amount deposited successfully. Updated balance: ${user['balance']}")
    else:
        print("User not found.")

def withdraw_money():
    name = input("Enter user name: ")
    amount = float(input("Enter amount to withdraw: "))
    user = find_user(name)
    if user:
        if user['balance'] >= amount:
            user['balance'] -= amount
            print(f"Amount withdrawn successfully. Updated balance: {user['balance']}")
        else:
            print("Insufficient funds.")
    else:
        print("User not found.")

def delete_user():
    name = input("Enter user name to delete: ")
    if name in user_table:
        del user_table[name]
        print(f"User '{name}' deleted successfully.")
    else:
        print("User not found.")

def main():
    while True:
        print("\n1. Add User")
        print("2. Find User")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Delete User")
        print("6. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            name = input("Enter user name to find: ")
            user = find_user(name)
            if user:
                print(f"User found - Name: {name}, Balance: {user['balance']}, ID: {user['id']}")
            else:
                print("User not found.")
        elif choice == "3":
            deposit_money()
        elif choice == "4":
            withdraw_money()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

# Call the 1
# main function directly
main()
