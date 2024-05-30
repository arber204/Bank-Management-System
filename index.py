import heapq
from handleTransaction import transaction
from handleUser import add_user, find_user, delete_user, user_table

# Initialize an empty priority queue
priority_queue = []

def add_action(priority, action):
    heapq.heappush(priority_queue, (priority, action))
    print("Wait in the line for your time to come, based on priority")

# Function to pop the highest priority action from the priority queue
def pop_action():
    if priority_queue:
        priority, action = heapq.heappop(priority_queue)
        return action
    else:
        print("No actions in the queue.")
        return None

# building the queue
def build_queue():
        transactions = int(input('How many transcations you wanna make?'))
        actions = []
        for i in range(transactions):
            print("\n1. Create an account")
            print("2. Check balance")
            print("3. Deposit money")
            print("4. Withdraw money")
            print("5. Delete your account")
            transaction_type = input('\nWhat type of transcation youwanna make? ')
            actions.append(transaction_type)
            # match(transaction_type):
            #     case "1":
            #         add_action(4, 'create')
            #     case "2":
            #         add_action(1, 'check')
            #     case "3":
            #         add_action(3, 'deposit')
            #     case "4":
            #         add_action(3, 'withdraw')
            #     case "5":
            #         add_action(2, 'delete')
        add_action(transactions, actions)

def main():
    while True:
        n = input('\nhow many people are waiting in the queue? ')
        for i in range(int(n)):
            build_queue()
        if(len(priority_queue) > 0):
            for people in priority_queue:
                priority, action = people
                was_account_created = False
                for act in action:
                    match(act):
                        case "1":
                            print("\nYOU ARE CREATING YOUR ACCOUNT\n")
                            created_account = add_user()
                            was_account_created = True
                        case "2":
                            if was_account_created:
                                print("\nYOU ARE CHECKING YOUR ACCOUNTBALANCE\n")
                                print(created_account)
                                # user = find_user()
                                # if user:
                                #     print(f"|  Name: {user['name']}|  Balance: {user['balance']}  |  ID: {user['id']}")
                                # else:
                                #     print("User not found.")
                        case "3":
                            print("\nYOU ARE DEPOSITING MONEY INTO YOUR ACCOUNT\n")
                            transaction("deposit")
                        case "4":
                            transaction("withdraw")
                        case "5":
                            delete_user()
                pop_action()

main()
