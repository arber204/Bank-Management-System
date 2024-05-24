from handleUser import find_user

def transaction(action):
    name = input("Insert your account name: ")
    amount = float(input("Insert amount: "))
    user = find_user()
    if user:
        match(action):
            case "deposit":
                user['balance'] += amount
                print(f"Amount deposited successfully. Updated balance: ${user['balance']}")
            case "withdraw":
                if user['balance'] >= amount:
                    user['balance'] -= amount
                    print(f"Amount withdrawn successfully. Updated balance: {user['balance']}")
                else:
                    print("Insufficient funds.")
    else:
        print("User not found.")