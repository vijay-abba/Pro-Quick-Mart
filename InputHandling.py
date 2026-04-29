from login_register.Register import Register
from login_register.Login import Login

from inventory.products import GeneralProducts

from colors import (
    RED_END,
    RED_START,
    BLUE_START,
    BLUE_END,
    GREEN_START,
    GREEN_END,
    YELLOW_START,
    YELLOW_END,
    CYAN_START,
    CYAN_END,
)


class InputHandling:

    def __init__(self):
        self.state = "inventory_management"
        self.input_value = 0
        self.logined_user = {
            "username": "abba",
            "password": "b0eafb7c71ffe185963738ef1aa9aa05:592c8bbeaea2c02d7e7bf95593457d28d7d4819e6e59d6b62aec252203d1be8b",
            "role": "admin",
            "failed-login-attempts": 0,
        }

        self.render_page()

    def render_page(self):

        match self.state:
            case "login_register":
                self.login_register_page()
            case "register":
                self.register_page()
            case "login":
                self.login_page()
            case "staff_main":
                self.staff_main_page()
            case "admin_main":
                self.admin_main_page()
            case "inventory_management":
                self.inventory_management_page()
            case "add_product":
                self.add_product_page()
            case "update_product":
                self.update_product_page()
            case "delete_product":
                self.delete_product_page()
            case "search_product":
                self.search_product_page()
            case "new_sale":
                self.new_sale_page()
            case "order_history":
                self.order_history_page()

    def login_register_page(self):
        print(f"{BLUE_START}\n===== QuickMart ====={BLUE_END}")
        print("\n1.Register 2.Login 3.Exit\n")
        input_value = input("Enter Choice: ")

        match input_value:
            case "1":
                self.state = "register"
            case "2":
                self.state = "login"
            case "3":
                self.state = "exit"
                print("---Exit---")
            case _:
                print(f"{RED_START}Invalid input. Try again.{RED_END}")
                self.state = "login_register"

        self.render_page()

    def register_page(self):
        print(f"{BLUE_START}--- Register ---{BLUE_END}")
        username = input("Username: ")
        password = input("Password: ")
        role = input("Role: ")

        r1 = Register(username, password, role)

        validation_result = r1.validate_everything()

        if validation_result:
            resutl = r1.create_new_user()
            if resutl:
                self.state = "login_register"
        else:
            msg = "\nInvalid, Try Again!"
            print(f"{RED_START}{msg}{RED_END}")
            self.state = "register"

        self.render_page()

    def login_page(self):
        print(f"{BLUE_START}--- Login ---{BLUE_END}")
        username = input("Username: ")
        password = input("Password: ")

        l1 = Login(username, password)
        result = l1.validate_everthing()

        if result:
            self.logined_user = l1.logined_user

            if l1.logined_user["role"] == "staff":
                self.state = "staff_main"
            elif l1.logined_user["role"] == "admin":
                self.state = "admin_main"
        else:
            msg = "Invalid, Try Again!"
            print(f"{RED_START}{msg}{RED_END}")
            self.state = "login"

        self.render_page()

    def staff_main_page(self):
        print(
            f"\n============================\n    {BLUE_START}QUICKMART MAIN MENU{BLUE_END}    \n============================\n1. Inventory Management\n2. New Sale\n3. Order History\n4. Reports\n5. Logout\n6. Exit\n============================\n"
        )
        input_value = input("Enter Choice: ")
        print(input_value)

        match input_value:
            case "1":
                print("Inventory Management")
                self.state = "inventory_management"
            case "2":
                print("New Sale")
            case "3":
                print("Order History ")
            case "4":
                print("Reports")
            case "5":
                print("Logout")
            case "6":
                print("Exit")
            case _:
                print(f"{RED_START}Invalid input. Try again.{RED_END}")
                self.state = "staff_main"

        self.render_page()

    def admin_main_page(self):
        print(
            f"\n============================\n    {BLUE_START}QUICKMART MAIN MENU{BLUE_END}    \n============================\n1. Inventory Management\n2. New Sale\n3. Order History\n4. Reports\n5. Coupons\n6. User Mgmt\n7. Logout\n8. Exit\n============================\n"
        )
        input_value = input("Enter Choice: ")
        print(input_value)

        match input_value:
            case "1":
                self.state = "inventory_management"
            case "2":
                print("New Sale")
            case "3":
                print("Order History ")
            case "4":
                print("Reports")
            case "5":
                print("Coupons")
            case "6":
                print("User Mgmt")
            case "7":
                print("Logout")
            case "8":
                print("Exit")
            case _:
                print(f"{RED_START}Invalid input. Try again.{RED_END}")
                self.state = "admin_main"

        self.render_page()

    def inventory_management_page(self):
        print(f"{BLUE_START}===== Inventory ====={BLUE_END}")
        print("1.Add 2.Update 3.Delete 4.Search 5.View All 6.Low Stock 7. Back")
        input_value = input("Enter Choice: ")
        print(input_value)

        match input_value:
            case "1":
                print("Add")
                self.state = "add_product"
            case "2":
                print("Update")
                self.state = "update_product"
            case "3":
                print("Delete")
                self.state = "delete_product"
            case "4":
                print("Search")
                self.state = "search_product"
            case "5":
                print("View All")
            case "6":
                print("Low Stock")
            case "7":
                print("Back")
            case _:
                print(f"{RED_START}Invalid input. Try again.{RED_END}")
                self.state = "inventory_management"

        self.render_page()

    def add_product_page(self):
        print(f"{BLUE_START}===== Type ====={BLUE_END}")
        print("1-General 2-Perishable 3-Electronic 4-Clothing 5-Back")
        type_input_value = input("Enter Choice: ")
        print(type_input_value)
        match type_input_value:
            case "1":
                print("--- Add General Product ---")
                product_name = input("Name: ")
                quantity = input("Quantity: ")
                price = input("Price: ")

                gp1 = GeneralProducts()
                gp1.add_product(product_name, quantity, price)

            case "2":
                print("--- Add Perishable Product ---")
            case "3":
                print("--- Add Electronic Product ---")
            case "4":
                print("--- Add Clothing Product ---")
            case _:
                print(f"{RED_START}Invalid input. Try again.{RED_END}")
                self.state = "add_product"

        self.render_page()

    def update_product_page(self):
        print(f"{BLUE_START}===== Type ====={BLUE_END}")
        print("1-General 2-Perishable 3-Electronic 4-Clothing 5-Back")
        type_input_value = input("Enter Choice: ")
        print(type_input_value)
        match type_input_value:
            case "1":
                print("--- Update General Product ---")
                product_id = input("Product ID: ")
                gp1 = GeneralProducts()
                product = gp1.fetch_product(product_id)

                if not product:
                    msg = "Product does not exist."
                    print(f"{RED_START}{msg}{RED_END}")
                    self.state = "update_product"
                else:
                    msg = "Previous values are in parentheses, e.g., 'Name (apples):'"
                    print(f"{YELLOW_START}{msg}{YELLOW_END}")

                    product_name = input(f"Name ({product["product_name"]}): ")
                    quantity = input(f"Quantity ({product["quantity"]}): ")
                    price = input(f"Price ({product["price"]}): ")
                    gp1.update_product(product_id, product_name, quantity, price)

            case "2":
                print("--- Update Perishable Product ---")
            case "3":
                print("--- Update Electronic Product ---")
            case "4":
                print("--- Update Clothing Product ---")
            case "5":
                print("--- Back ---")
                self.state = "inventory_management"
            case _:
                print(f"{RED_START}Invalid input. Try again.{RED_END}")
                self.state = "update_product"

        self.render_page()

    def delete_product_page(self):
        print("--- Delete Product ---")
        product_id = input("Product ID: ")
        gp1 = GeneralProducts()
        product = gp1.fetch_product(product_id)

        if not product:
            msg = "Product does not exist."
            print(f"{RED_START}{msg}{RED_END}")
            self.state = "delete_product"
        else:
            gp1.delete_product(product_id)
            self.state = "inventory_management"

        self.render_page()

    def search_product_page(self):
        print("--- Search Product ---")
        product_name = input("Product Name: ")
        gp1 = GeneralProducts()
        products = gp1.search_product(product_name)
        if not products:
            msg = "Product does not exist."
            print(f"{RED_START}{msg}{RED_END}")
            self.state = "search_product"
        else:
            # print(products)
            pass

ih = InputHandling()
