import csv

users_active = [{'name': 'John', 'password': '1234' }, {'name': 'Kate', 'password': '5678'}]
users_disabled = []

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


while True:
    print_menu()        
    menu_selection = input("Chose a menu option: ")
    
    match menu_selection:
        case "0":
            break
        case "1":
            print("You're in option 1")
        case "2":
            print("\n---View Users---")
            print_users()
        case "3":
            print("You're in option 3")
        case _:
            print("Invalid option, try again")
        