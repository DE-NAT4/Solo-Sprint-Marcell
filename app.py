import csv

users_active = [{'name': 'John', 'password': '1234', 'status': 'active'}, {'name': 'Kate', 'password': '5678', 'status': 'active'}]
users_disabled = []

def save_users_to_csv():
    with open('users.csv', 'w', newline='') as csvfile:
        fieldnames = ['username', 'password', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for user in users_active:
            writer.writerow({'username': user['name'], 'password': user['password'], 'status': user['status']})

        for user in users_disabled:
            writer.writerow({'username': user['name'], 'password': user['password'], 'status': user['status']})

def load_users_from_csv():
    pass



def print_menu():
    print("\n-----------------------")
    print("User Management System\n")
    print("0 - Save & Exit")
    print("1 - Add User")
    print("2 - View Users")
    print("3 - Enable/Disable User")
    print("-----------------------")


def print_users():
    print("Active users:")
    if not users_active:
        print("No Users")

    for i, user in enumerate(users_active, start=1):
        print(f"{i}. Name: {user['name']} | Password: {user['password']}")
    
    print("\nDisabled users:")
    if not users_disabled:
        print("No Users")

    for i, user in enumerate(users_disabled, start=1):
        print(f"{i}. Name: {user['name']} | Password: {user['password']}")   

def add_user():
    while True:
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        status = input('Enter status ("active" or "disabled"): ').lower()

        match status:
            case "active":
                users_active.append({
                    'name': username,
                    'password': password,
                    'status': status
                })
                break
            case "disabled":
                users_disabled.append({
                    'name': username,
                    'password': password,
                    'status': status
                })
                break
            case _:
                print("Invalid status")


def toggle_user_status():
    while True:
        choice = input('Type "disable" to disable an active user or type "enable" to enable a  disabled user: ').lower()

        match choice:
            case "disable":
                if not users_active:
                    print("No active users")

                for i, user in enumerate(users_active, start=0):
                    print(f"Index: {i} | Name: {user['name']}")

                index = int(input("Enter the index of the user you want to disable: "))
                try: 
                    user = users_active[index]
                    user['status'] = 'disabled'
                    users_disabled.append(user)

                    users_active.pop(index)
                    
                    break

                except Exception as e:
                    print(f"Invalid input. Error: {e} ")

            case "enable":
                if not users_disabled:
                    print("No active users")

                for i, user in enumerate(users_disabled, start=0):
                    print(f"Index: {i} | Name: {user['name']}")

                index = int(input("Enter the index of the user you want to enable: "))
                try: 
                    user = users_disabled[index]
                    user['status'] = 'enabled'
                    users_active.append(user)

                    users_disabled.pop(index)
                    
                    break

                except Exception as e:
                    print(f"Invalid input. Error: {e} ")

            case _:
                print("Invalid input")

            


while True:
    print_menu()        
    menu_selection = input("Chose a menu option: ")
    
    match menu_selection:
        case "0":
            save_users_to_csv()
            break
        case "1":
            print("\n---Add User")
            add_user()
        case "2":
            print("\n---View Users---")
            print_users()
        case "3":
            print("\n---Enable/Disable User---")
            toggle_user_status()
        case _:
            print("Invalid option, try again")
        