from pathlib import Path
import json
from datetime import datetime, date, time

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


class Coupon:
    def __init__(self):
        self.file_path = Path("data")
        self.coupons_file_name = self.file_path / f"coupons.txt"

        self.coupons_list = []
        self.coupons_list = self.fetch_list(self.coupons_file_name)

    def fetch_list(self, file_name):
        # if no file create empty
        # print("fetching...")
        if not file_name.is_file():
            with open(file_name, "w") as f:
                f.write(json.dumps([]))

        with open(file_name, "r") as f:
            str_list_name = f.readline()
            list_name = json.loads(str_list_name)
            return list_name

    def save_list(self, file_name, list_name):
        str_list_name = json.dumps(list_name)
        with open(file_name, "w") as f:
            f.write(str_list_name)
        # self.fetch_cart_list()

    def create_coupon(self, coupon_obj):
        print(coupon_obj)
        pass

    def list_coupons(self):
        pass

    def deactivate(self):
        pass

    def is_active_coupon(self, coupon_name):

        filtered_coupon_list = list(
            filter(lambda c: c["code"] == coupon_name, self.coupons_list)
        )

        if filtered_coupon_list >= 1:

            for coupon in filtered_coupon_list:
                print(coupon)

                if coupon["usage_limit"] > 1 and True:
                    pass

            pass

    def check(self):
        todays_date = date.today()
        print(todays_date)

        pass

    def validate_coupon():
        pass

    def log_action(self):
        pass
