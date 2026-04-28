from login_register.Register import Register
from login_register.Login import Login

red_start  = "\033[91m"
red_end = "\033[0m"

green_start = "\033[92m" 
green_end =  "\033[0m"

blue_start = "\033[94m"
blue_end = "\033[0m"

yellow_start = "\033[93m"
yellow_end = "\033[0m"

class InputHandling:

    def __init__(self):
        self.state = "login_register"
        self.input_value = 0

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
            case "new_sale":
                self.new_sale_page()
            case "order_history":
                self.order_history_page()


    def login_register_page(self):
        print(f"{blue_start}\n===== QuickMart ====={blue_end}")
        print("\n1.Register 2.Login 3.Exit\n")
        input_value = input("Enter Choice: ")

        match input_value:
            case "1":
                self.state = "register"
            case "2":
                self.state = "login"
            case "3":
                self.state = "exit" 
            case _:
                print( f"{red_start}Invalid input. Try again.{red_end}")
                self.login_register_page()

        self.render_page()

    def register_page(self):
        print(f"{blue_start}--- Register ---{blue_end}")
        username = input("Username: ")
        password = input("Password: ")
        role = input("Role: ")

        r1 = Register(username, password, role)
        user_result = r1.validate_username()
        pass_result = r1.validate_password()
        role_result = r1.validate_role()

        if not user_result:
            print("Invalid, Try Again!")
            self.state = "register_page"
            self.render_page()
            # self.register_page

        resutl = r1.create_new_user()

        if resutl:
            self.state = "login_register"
            self.render_page()

    def login_page(self):
        print("Login page")
        username = input("Username: ")
        password = input("Password: ")

        l1 = Login(username, password)
        user_result = l1.is_user_exist()
        pass_result = l1.is_password_valide()

        if not user_result:
            print("Invalid, Try Again!")
            print("Invalid, Username")
            self.login_page

        self.state = "main_page_staff"
        self.render_page
    
    def main_page_staff(self):
        pass



ih = InputHandling()
