class Register:

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def validate_username(self):
        return False

    def validate_password(self):
        pass

    def validate_role(self):
        pass

    def create_new_user(self):
        return True
