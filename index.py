import heapq
from handleTransaction import transaction
from handleUser import add_user, find_user, delete_user, user_table

# Initialize an empty priority queue
priority_queue = []

def add_action(priority, action):
    heapq.heappush(priority_queue, (priority, action))
    # print(f"Added action: {action} with priority: {priority}")
    print("Wait in the line for your time to come, based on priority")

# Function to pop the highest priority action from the priority queue
def pop_action():
    if priority_queue:
        priority, action = heapq.heappop(priority_queue)
        print(f"Processed action: {action} with priority: {priority}")
        return action
    else:
        print("No actions in the queue.")
        return None

# building the queue
def build_queue():
        print("\n1. Create an account")
        print("2. Check balance")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Delete your account")
        transaction_type = input('What type of transcation you wanna make?')
        print("____________________________________________________________")
        match(transaction_type):
            case "1":
                add_action(4, 'create')
            case "2":
                add_action(1, 'check')
            case "3":
                add_action(3, 'deposit')
            case "4":
                add_action(3, 'withdraw')
            case "5":
                add_action(2, 'delete')

def main():
    while True:
        n = input('how many people are waiting in the queue?')
        for i in range(int(n)):
            build_queue()
        if(len(priority_queue) > 0):
            for i in priority_queue:
                priority, action = i
                match(action):
                    case "create":
                        print("______________________________________________________")
                        add_user()
                    case "check":
                        print("______________________________________________________")
                        user = find_user()
                        if user:
                            print(f"|  Name: {user['name']}  |  Balance: {user['balance']}  |  ID: {user['id']}")
                        else:
                            print("User not found.")
                    case "deposit":
                        transaction("deposit")
                    case "withdraw":
                        transaction("withdraw")
                    case "delete":
                        delete_user()
                heapq.heappop(priority_queue)
main()
