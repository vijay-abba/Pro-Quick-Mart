class InputHandling:

    def __init__(self):
        self.state = "login_register"
        self.input_value = 0

        self.render_page()

    def render_page(self):
        if self.state == "login_register":
            self.login_register_page()
        elif self.state == "register_page":
            self.register_page()

    def login_register_page(self):
        print("Login and Register page")
        input_value = input("1.Register 2. Login 3. Exit: \n")
        if input_value == "1":
            self.state = "register_page"
            self.input_value = input_value
        elif input_value == "2":
            self.state = "login_page"
        elif input_value == "3":
            self.state = "exit"
        else:
            print("Invalid Input Try Again")
            self.login_register_page()

        self.render_page()

    def register_page(self):
        print('register page')
        username = input("Username: ")
        password = input("Password: ")
        role = input("Role: ")


        # TASK
            #1. Check Validate Username
            #2. check Validate Password
            #3.  Validate Role 

        # Description 
            # Createing Register Class 
                # creating instance  (username, passd, role)
                # checking 
                    #  rc1.username_validate  if(worng ) try agin
                    #  rc1.password_validate. if(worng ) try agin
                    #  rc1.role_validate.  if(worng ) try agin

                # if successs then 
                    # rc1.create_new_user
                    # go back to update state to "login_register" page 
                    # run render_page

                






ih = InputHandling()
