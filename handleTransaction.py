from handleUser import find_user

def transaction(action, name):
    while True:
        user = find_user(name)
        if user:
            while True:
                amount = input("Insert amount: ")
                try:
                    amount = int(amount)
                    break
                except ValueError:
                    print(' << ATTENTION >> Insert a number please!')
            floated_balance = float(user['balance'])
            match(action):
                case "deposit":
                    user['balance'] = floated_balance + float(amount)
                    print(f"Amount deposited successfully. Updated balance: ${user['balance']}")
                case "withdraw":
                    if floated_balance >= amount:
                        user['balance'] = floated_balance - float(amount)
                        print(f"Amount withdrawn successfully. Updated balance: ${user['balance']}")
                    else:
                        print("Insufficient funds.")
            break
        else:
            print("User not found.")