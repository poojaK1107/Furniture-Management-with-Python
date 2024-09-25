# admin_module.py

class AdminModule:
    def __init__(self):
        # Initialize any necessary data structures or variables
        self.user_data_file = "user_data.txt"  # Assuming this is the user data file name
        self.furniture_data_file = "furniture_data.txt"  # Assuming this is the furniture data file name
        self.order_data_file = "order_data.txt"  # Assuming this is the order data file name

    def admin_login(self):
        print("Admin Login")
        # Placeholder logic for admin login
        # Implement admin login functionality

    def add_furniture(self):
        print("Add Furniture")
        furniture_name = input("Enter furniture name: ")
        furniture_description = input("Enter furniture description: ")
        furniture_quantity = int(input("Enter quantity: "))
        furniture_price = float(input("Enter price: "))
        # Placeholder logic for adding furniture
        # Implement adding furniture functionality
        with open(self.furniture_data_file, "a") as file:
            file.write(f"{furniture_name}\t{furniture_description}\t{furniture_quantity}\t{furniture_price}\n")
        print("Furniture added successfully.")

    def remove_furniture(self):
        print("Remove Furniture")
        furniture_name = input("Enter furniture name to remove: ").strip()
        furniture_found = False
        lines = []
        # Read furniture data from file
        with open(self.furniture_data_file, "r") as file:
            lines = file.readlines()
        # Remove the furniture if found
        with open(self.furniture_data_file, "w") as file:
            for line in lines:
                if furniture_name not in line:
                    file.write(line)
                else:
                    furniture_found = True
        if furniture_found:
            print(f"Furniture '{furniture_name}' removed successfully.")
        else:
            print(f"Furniture '{furniture_name}' not found.")

    def manage_furniture(self):
        print("Manage Furniture")
        print("1. Add Furniture")
        print("2. Remove Furniture")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.add_furniture()
        elif choice == '2':
            self.remove_furniture()
        else:
            print("Invalid choice.")

    def view_furniture(self):
        print("View Furniture")
        # Placeholder logic for viewing furniture
        # Implement viewing furniture functionality

    def display_user_details(self):
        print("Display User Details")
        # Read user data from the file
        user_list = self._read_user_data()
        if user_list:
            print("User Details:")
            for user in user_list:
                print(user)
        else:
            print("No user details available.")

    def manage_orders(self):
        print("Manage Orders")
        order_list = self._read_order_data()
        if order_list:
            print("Existing Orders:")
            for order in order_list:
                print(order)
            while True:
                action = input("Select action for order (M - Mark as Processed, U - Update Status, E - Exit): ").upper()
                if action == 'M':
                    order_id = input("Enter the ID of the order to mark as processed: ")
                    # Update order status to processed
                    print(f"Order {order_id} marked as processed.")
                elif action == 'U':
                    order_id = input("Enter the ID of the order to update status: ")
                    new_status = input("Enter the new status for the order: ")
                    # Update order status
                    print(f"Status of order {order_id} updated to {new_status}.")
                elif action == 'E':
                    print("Exiting manage orders.")
                    break
                else:
                    print("Invalid action.")
        else:
            print("No orders available.")

    def generate_reports(self):
        print("Generate Reports")
        # Generate report based on order data
        order_list = self._read_order_data()
        if order_list:
            report_filename = "order_report.txt"
            with open(report_filename, "w") as report_file:
                report_file.write("Order Report:\n")
                report_file.write("ID\tUser\tFurniture\tQuantity\tStatus\n")
                for order in order_list:
                    report_file.write(order)  # Write each order to the report file
            print(f"Report generated successfully. Saved as '{report_filename}'.")
        else:
            print("No orders available.")

    def _read_user_data(self):
        # Read user data from the file
        try:
            with open(self.user_data_file, "r") as file:
                user_list = file.readlines()
            return user_list
        except FileNotFoundError:
            print("User data file not found.")
            return []

    def _read_order_data(self):
        # Read order data from the file
        try:
            with open(self.order_data_file, "r") as file:
                order_list = file.readlines()
            return order_list
        except FileNotFoundError:
            print("Order data file not found.")
            return []
