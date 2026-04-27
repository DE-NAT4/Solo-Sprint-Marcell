import csv

users_active = [{'name': 'John', 'password': '1234' }, {'name': 'Kate', 'password': '5678'}]
users_disabled = []

def save_users_to_csv():
    pass


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
                print("Invalis status")


while True:
    print_menu()        
    menu_selection = input("Chose a menu option: ")
    
    match menu_selection:
        case "0":
            break
        case "1":
            print("\n---Add User")
            add_user()
        case "2":
            print("\n---View Users---")
            print_users()
        case "3":
            print("You're in option 3")
        case _:
            print("Invalid option, try again")
        