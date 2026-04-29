from login_register.Register import Register
from login_register.Login import Login
from colors import RED_END, RED_START, BLUE_START,BLUE_END,GREEN_START, GREEN_END, YELLOW_START, YELLOW_END, CYAN_START,CYAN_END

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
                print( f"{RED_START}Invalid input. Try again.{RED_END}")
                self.login_register_page()

        self.render_page()

    def register_page(self):
        print(f"{BLUE_START}--- Register ---{BLUE_END}")
        username = input("Username: ")
        password = input("Password: ")
        role = input("Role: ")

        r1 = Register(username, password, role)

        validation_result = r1.validate_everything()

        if not validation_result:
            msg = "\nInvalid, Try Again!"
            print(f"{RED_START}{msg}{RED_END}")
            return self.register_page()
            
        resutl = r1.create_new_user()   
        if resutl:
            self.state = "login_register"
            self.render_page()


    def login_page(self):
        print(f"{BLUE_START}--- Login ---{BLUE_END}")
        username = input("Username: ")
        password = input("Password: ")

        l1 = Login(username, password)
        result = l1.validate_everthing()

        if not result:
            msg ="Invalid, Try Again!"
            print(f"{RED_START}{msg}{RED_END}")
            return self.login_page()


        if l1.logined_user["role"] == "staff":
            self.state = "staff_main"
        elif l1.logined_user['role'] == "admin":
            self.state = "admin_main"
        
        self.render_page()


    def staff_main_page(self):
        print(f"\n============================\n    {BLUE_START}QUICKMART MAIN MENU{BLUE_END}    \n============================\n1. Inventory Management\n2. New Sale\n3. Order History\n4. Reports\n5. Logout\n6. Exit\n============================\n")
        input_value = input("Enter Choice: ")

    def admin_main_page(self):
        print("HOME PAGE ADMIIN")


ih = InputHandling()
