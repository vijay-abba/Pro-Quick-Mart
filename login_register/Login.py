from pathlib import Path
import json
import hashlib
import hmac

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


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.file_path = Path("data/employees")
        self.file_name = self.file_path / f"{self.username}.txt"

        self.logined_user = {}

    def is_user_exist(self):
        if self.file_name.is_file():
            with open(self.file_name, "r") as f:
                json_string = f.readline()
                user_obj = json.loads(json_string)
                self.logined_user = user_obj
                return True

        print(f"{RED_START}Username does not exist{RED_END}")
        return False

    def is_user_account_locked(self):
        failed_attempts = self.logined_user["failed-login-attempts"]
        if failed_attempts >= 3:
            print(f"{RED_START}Your account is locked. Contact admin.{RED_END}")
            return False
        return True

    def check_password(self, stored_string, provided_password):
        try:
            salt_hex, hash_hex = stored_string.split(":")
            salt = bytes.fromhex(salt_hex)
            stored_hash = bytes.fromhex(hash_hex)
            new_hash = hashlib.pbkdf2_hmac(
                "sha256", provided_password.encode("utf-8"), salt, 100000
            )
            return hmac.compare_digest(new_hash, stored_hash)  # True or False
        except Exception:
            return False

    def update_file_date(self):
        json_string = json.dumps(self.logined_user)
        with open(self.file_name, "w") as f:
            f.write(json_string)

    def is_password_valide(self):
        veryify_password = self.check_password(
            self.logined_user["password"], self.password
        )
        if veryify_password != True:
            msg = "Incorrect Password"
            print(f"{RED_START}{msg}{RED_END}")
            self.logined_user["failed-login-attempts"] += 1

            msg2 = (
                f"only {3 - self.logined_user["failed-login-attempts"]} attempts left"
            )
            print(f"{RED_START}{msg2}{RED_END}")
            self.update_file_date()
            return False

        self.logined_user["failed-login-attempts"] = 0
        self.update_file_date()
        print(
            f"{GREEN_START}Welcome, {self.logined_user["username"]}! (Role: {self.logined_user["role"]}){GREEN_END}"
        )
        return True

    def validate_everthing(self):
        return (
            self.is_user_exist()
            and self.is_user_account_locked()
            and self.is_password_valide()
        )
