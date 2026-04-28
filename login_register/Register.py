import hashlib
import os
from pathlib import Path
import json

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


class Register:

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.hash_password = ""
        self.role = role

        self.file_path = Path("data/employees")
        self.file_name = self.file_path / f"{self.username}.txt"

    def validate_username(self):
        length_username = len(self.username)
        spaces_count = self.username.count(" ")
        if length_username >= 4 and length_username <= 20 and spaces_count == 0:
            return True
        else:
            msg = "The username must be 4–20 characters long and should not contain spaces."
            print(f"{RED_START}{msg}{RED_END}")
            return False

    def unique_username(self):
        if self.file_name.is_file():
            msg = "Username taken. Try another."
            print(f"{RED_START}{msg}{RED_END}")
            return False
        else:
            return True

    def validate_password(self):
        length_password = len(self.password)
        upper_count = len(list(filter(lambda c: c.isupper(), self.password)))
        digits_count = len(list(filter(lambda i: i.isnumeric(), self.password)))
        if length_password > 8 and upper_count >= 1 and digits_count >= 1:
            return True
        else:
            msg = "Password must be at least 9 characters long, with 1 uppercase letter and 1 digit."
            print(f"{RED_START}{msg}{RED_END}")
            return False

    def validate_role(self):
        if self.role != "staff" and self.role != "admin":
            msg = "Role must be either 'staff' or 'admin'"
            print(f"{RED_START}{msg}{RED_END}")
            return False
        else:
            return True

    def create_hash_password(self):
        salt = os.urandom(16)
        dk = hashlib.pbkdf2_hmac("sha256", self.password.encode("utf-8"), salt, 100000)
        if dk is None:
            raise RuntimeError(
                "Hashlib failed to generate a key. Check your OpenSSL installation."
            )
        self.hash_password = salt.hex() + ":" + dk.hex()
        return True

    def create_new_user(self):

        new_user_obj = {
            "username": self.username,
            "password": self.hash_password,
            "role": self.role,
            "failed-login-attempts": 0,
        }

        json_user_obj = json.dumps(new_user_obj)

        with open(self.file_name, "w") as f:
            f.write(json_user_obj)
            msg = "Registration successful!"
            print(f"{GREEN_START}{msg}{GREEN_END}")

        return True

    def validate_everything(self):
        return (
            self.validate_username()
            and self.unique_username()
            and self.validate_password()
            and self.validate_role()
            and self.create_hash_password()
        )
