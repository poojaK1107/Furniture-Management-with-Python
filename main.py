# main.py

from admin_module import AdminModule
from user_module import UserModule

def main():
    print("Welcome to Furniture Management System!")
    print("1. Admin Login")
    print("2. User Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    admin_module = AdminModule()
    user_module = UserModule()

    if choice == '1':
        admin_module.admin_login()
        admin_menu(admin_module, user_module)
    elif choice == '2':
        user_module.user_login()
        user_menu(user_module)
    elif choice == '3':
        print("Exiting program.")
    else:
        print("Invalid choice. Please try again.")

def admin_menu(admin_module, user_module):
    while True:
        print("\nAdmin Menu:")
        print("1. Manage Furniture")
        print("2. View Furniture")
        print("3. Display User Details")
        print("4. Manage Orders")
        print("5. Generate Reports")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            admin_module.manage_furniture()
        elif choice == '2':
            admin_module.view_furniture()
        elif choice == '3':
            admin_module.display_user_details()
        elif choice == '4':
            admin_module.manage_orders()
        elif choice == '5':
            admin_module.generate_reports()
        elif choice == '6':
            print("Logging out.")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(user_module):
    while True:
        print("\nUser Menu:")
        print("1. View Furniture")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove from Cart")
        print("5. Place Order")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            user_module.view_furniture()
        elif choice == '2':
            user_module.add_to_cart()
        elif choice == '3':
            user_module.view_cart()
        elif choice == '4':
            user_module.remove_from_cart()
        elif choice == '5':
            user_module.proceed_to_order()
        elif choice == '6':
            print("Logging out.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
