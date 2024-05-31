import heapq
from handleTransaction import transaction
from handleUser import add_user, find_user, delete_user, user_table

# Initialize an empty priority queue
priority_queue = []

def add_action(priority, action, name):
    heapq.heappush(priority_queue, (priority, action, name))
    print("Wait in the line for your time to come, based on priority")
    print("-----------------------------------------------------------")

# Function to pop the highest priority action from the priority queue
def pop_action():
    if priority_queue:
        action = heapq.heappop(priority_queue)
        return action
    else:
        print("No actions in the queue.")
        return None

# building the queue
def build_queue():
    name = input('Enter your name for processing: ')
    print("-----------------------------------------------------")
    while True:
        transactions = input('How many transcations you wanna make? ')
        print("-----------------------------------------------------")
        try:
            transactions = int(transactions)
            break
        except ValueError:
            print(' << ATTENTION >> Insert a number please!')
    actions = []
    for i in range(transactions):
        print("\n1. Create an account")
        print("2. Check balance")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Delete your account")
        while True:
            transaction_type = input('\nWhat type of transaction you wanna make? ')
            print("-----------------------------------------------------")
            try:
                transaction_type = int(transaction_type)
                if transaction_type in [1, 2, 3, 4, 5]:
                    actions.append(transaction_type)
                    break
                else:
                    print(' << ATTENTION >> Insert only a number from 1 to 5 please!')
            except ValueError:
                print(' << ATTENTION >> Insert only a number please!')
    add_action(transactions, actions, name)

def main():
    while True:
        while True:
            n = input('\nHow many people are waiting in the queue? ')
            print('--------------------------------------------------')
            try:
                n = int(n)
                break
            except ValueError:
                print(' << ATTENTION >> Insert a number please!')
        for i in range(int(n)):
            build_queue()
        if(len(priority_queue) > 0):
            for people in priority_queue:
                priority, action, name = people
                print(f"There {'are' if len(action) > 1 else 'is'} {len(action)} transaction{'s' if len(action) > 1 else ''} to be processed for {name}")
                for act in action:
                    match(act):
                        case 1:
                            print("\n----------------------------------")
                            print("YOU ARE CREATING YOUR ACCOUNT")
                            print("----------------------------------\n")
                            found_user = find_user(name)
                            while True:
                                if found_user:
                                    print(f"{name} already exists in our database. Please enter a unique name.")
                                else:
                                    add_user(name)
                                    break
                        case 2:
                            print("\n-----------------------------------------")
                            print("YOU ARE CHECKING YOUR ACCOUNT BALANCE")
                            print("-----------------------------------------\n")
                            find_user(name)
                        case 3:
                            print("\n------------------------------------------")
                            print("YOU ARE DEPOSITING MONEY INTO YOUR ACCOUNT")
                            print("------------------------------------------\n")
                            transaction("deposit", name)
                        case 4:
                            print("\n------------------------------------------")
                            print("YOU ARE WITHDRAWING MONEY FROM YOUR ACCOUNT")
                            print("------------------------------------------\n")
                            transaction("withdraw", name)
                        case 5:
                            delete_user(name)
                            print("\n------------------------------------")
                            print("YOUR ACCOUNT WAS SUCCESSFULLY DELETED")
                            print("---------------------------------------\n")
            pop_action()

main()
