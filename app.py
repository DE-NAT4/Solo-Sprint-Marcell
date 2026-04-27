import csv

users_active = []
users_disabled = []

def print_menu():
    print("\n-----------------------")
    print("User Management System\n")
    print("0 - Save & Exit")
    print("1 - Add User")
    print("2 - View Users")
    print("3 - Enable/Disable User")
    print("-----------------------")


while True:
    print_menu()        
    menu_selection = input("Chose a menu option: ")

    match menu_selection:
        case "0":
            break
        case "1":
            print("You're in option 1")
        case "2":
            print("You're in option 2")
        case "3":
            print("You're in option 3")
        case _:
            print("Invalid option, try again")
        