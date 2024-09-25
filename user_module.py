# user_module.py

class UserModule:
    def __init__(self):
        # Initialize any necessary data structures or variables
        self.user_data_file = "user_data.txt"  # Assuming this is the user data file name
        self.furniture_data_file = "furniture_data.txt"  # Assuming this is the furniture data file name
        self.cart_data_file = "cart_data.txt"  # Assuming this is the cart data file name

    def user_login(self):
        print("User Login")
        # Placeholder logic for user login
        # Implement user login functionality

    def view_furniture(self):
        print("View Furniture")
        try:
            with open(self.furniture_data_file, "r") as file:
                furniture_list = file.readlines()
            if furniture_list:
                print("Furniture List:")
                for furniture in furniture_list:
                    print(furniture.strip())
            else:
                print("No furniture available.")
        except FileNotFoundError:
            print("Furniture data file not found.")

    def add_to_cart(self):
        print("Add to Cart")
        furniture_name = input("Enter furniture name to add to cart: ").strip()
        furniture_found = False
        try:
            with open(self.furniture_data_file, "r") as file:
                furniture_list = file.readlines()
            for furniture in furniture_list:
                name, _ = furniture.split("\t")
                if name.strip() == furniture_name:
                    furniture_found = True
                    break
            if furniture_found:
                with open(self.cart_data_file, "a") as file:
                    file.write(f"{furniture_name}\n")
                print(f"{furniture_name} added to cart successfully.")
            else:
                print(f"{furniture_name} not found in furniture list.")
        except FileNotFoundError:
            print("Furniture data file not found.")

    def view_cart(self):
        print("View Cart")
        try:
            with open(self.cart_data_file, "r") as file:
                cart_items = file.readlines()
            if cart_items:
                print("Items in Cart:")
                for item in cart_items:
                    print(item.strip())
            else:
                print("Cart is empty.")
        except FileNotFoundError:
            print("Cart data file not found.")

    def remove_from_cart(self):
        print("Remove from Cart")
        furniture_name = input("Enter furniture name to remove from cart: ").strip()
        try:
            with open(self.cart_data_file, "r") as file:
                cart_items = file.readlines()
            with open(self.cart_data_file, "w") as file:
                removed = False
                for item in cart_items:
                    if item.strip() != furniture_name:
                        file.write(item)
                    else:
                        removed = True
                if removed:
                    print(f"{furniture_name} removed from cart successfully.")
                else:
                    print(f"{furniture_name} not found in cart.")
        except FileNotFoundError:
            print("Cart data file not found.")

    def proceed_to_order(self):
        print("Proceed to Order")
        self.provide_details()
        self.place_order()

    def provide_details(self):
        print("Provide Details")
        user_name = input("Enter your name: ")
        user_address = input("Enter your address: ")
        user_contact = input("Enter your contact number: ")
        print("Details received.")

    def place_order(self):
        try:
            with open(self.cart_data_file, "r") as file:
                cart_items = file.readlines()
            if cart_items:
                print("Order Summary:")
                for item in cart_items:
                    print(item.strip())
                print("Your order has been placed. Thank you for shopping with us!")
                # Clear the cart after placing the order
                open(self.cart_data_file, 'w').close()
            else:
                print("Your cart is empty. Please add items to your cart before placing an order.")
        except FileNotFoundError:
            print("Cart data file not found.")

    # Other functions remain unchanged



    



    def browse_furniture(self):
        print("Browse Furniture")
        furniture_list = self._read_furniture_data()
        if furniture_list:
            print("Available Furniture Items:")
            for idx, furniture in enumerate(furniture_list, start=1):
                print(f"{idx}. {furniture}")
        else:
            print("No furniture items available.")

    def search_furniture(self, keyword):
        print(f"Search Furniture by Keyword: {keyword}")
        furniture_list = self._read_furniture_data()
        if furniture_list:
            matching_items = [item for item in furniture_list if keyword.lower() in item.lower()]
            if matching_items:
                print("Matching Furniture Items:")
                for item in matching_items:
                    print(item)
            else:
                print("No matching furniture items found.")
        else:
            print("No furniture items available.")

    def view_furniture_details(self, item_index):
        print("View Furniture Details")
        furniture_list = self._read_furniture_data()
        if furniture_list and 1 <= item_index <= len(furniture_list):
            print("Furniture Details:")
            print(furniture_list[item_index - 1])
        else:
            print("Invalid item index or no furniture items available.")

    def sort_furniture_by_price(self):
        print("Sort Furniture by Price")
        furniture_list = self._read_furniture_data()
        if furniture_list:
            try:
                sorted_items = sorted(furniture_list, key=lambda x: float(x.split(',')[2]))
                print("Sorted Furniture Items by Price:")
                for item in sorted_items:
                    print(item)
            except ValueError:
                print("Error: Price data is invalid for sorting.")
        else:
            print("No furniture items available.")

    def sort_furniture_by_availability(self):
        print("Sort Furniture by Availability")
        furniture_list = self._read_furniture_data()
        if furniture_list:
            sorted_items = sorted(furniture_list, key=lambda x: x.split(',')[3])
            print("Sorted Furniture Items by Availability:")
            for item in sorted_items:
                print(item)
        else:
            print("No furniture items available.")

    def _read_furniture_data(self):
        # Read furniture data from the file
        try:
            with open(self.furniture_data_file, "r") as file:
                furniture_list = file.readlines()
            return furniture_list
        except FileNotFoundError:
            print("Furniture data file not found.")
            return []
