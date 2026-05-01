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

    def create_coupon(
        self, coupon_code, coupon_type, value, min_order, expiry_date, usage_limit
    ):
        coupon_list_with_given_name = self.is_active_coupon(coupon_code)

        if len(coupon_list_with_given_name) != 0:
            msg = "A coupon with this code already exists and active"
            print(f"{RED_START}{msg}{RED_END}")
            return False

        if not (coupon_type.isdigit() and (coupon_type == "1" or coupon_type == "2")):
            msg = "Please enter a valid number for the coupon type."
            print(f"{RED_START}{msg}{RED_END}")
            return False

        if not value.isdigit():
            msg = "Please enter a valid numeric amount for the value."
            print(f"{RED_START}{msg}{RED_END}")
            return False

        if not min_order.isdigit():
            msg = "The minimum order amount must be a number."
            print(f"{RED_START}{msg}{RED_END}")
            return False

        if not usage_limit.isdigit():
            msg = "The usage limit must be a number."
            print(f"{RED_START}{msg}{RED_END}")
            return False

        try:
            expiry_date_obj = datetime.strptime(expiry_date, "%Y-%m-%d")
        except ValueError:
            msg = "Please provide a valid expiry date using the YYYY-MM-DD format (e.g., 2025-05-21)."
            print(f"{RED_START}{msg}{RED_END}")
            return False

        coupon_obj = {
            "coupon_code": coupon_code,
            "coupon_type": int(coupon_type),
            "value": int(value),
            "min_order": int(min_order),
            "expiry_date": expiry_date,
            "usage_limit": int(usage_limit),
            "status": "active",
        }

        self.coupons_list.append(coupon_obj)
        self.save_list(self.coupons_file_name, self.coupons_list)
        msg = f"Coupon {coupon_code} created!"
        print(f"{GREEN_START}{msg}{GREEN_END}")
        # TASK  ACTION LOG

    def list_coupons(self):

        heading = f"{"CODE".ljust(9)} | {"TYPE"} |  {"VALUE"}  | {"MIN ORDER"} | {"EXPIRY DATE"} | {"USAGE LIMIT LEFT"} |  {"STATUS"}  |"
        print(f"{BLUE_START}{heading}{BLUE_END}")

        def print_obj(obj):

            b = "|".center(3)
            print(
                f"{obj["coupon_code"].ljust(9)}{b}{str(obj["coupon_type"]).center(4)}{b}{str(obj["value"]).center(7)}{b}{str(obj["min_order"]).center(9)}{b}{obj["expiry_date"].center(11)}{b}{str(obj["usage_limit"]).center(16)}{b}{obj["status"].center(8)}{b}"
            )
            # f"{obj["coupon_code"].ljust(8)} | {str(obj["coupon_type"]).rjust(2)} {"|".rjust(3)} {obj["value"]} | {obj["min_order"]} | {obj["expiry_date"]} | {obj["usage_limit"]} | {obj["status"]}"

        list(map(lambda c: print_obj(c), self.coupons_list))

    def deactivate(self, coupon_code):

        coupon_list_with_given_name = self.is_active_coupon(coupon_code)

        if len(coupon_list_with_given_name) <= 0:
            msg = "A coupon with this code don't exists or active"
            print(f"{RED_START}{msg}{RED_END}")
            return False

        def deactivate_status(obj):
            obj["status"] = "inactive"
            return obj

        edited_coupon_list = list(
            map(
                lambda c: (
                    deactivate_status(c) if c["coupon_code"] == coupon_code else c
                ),
                self.coupons_list,
            )
        )

        msg = f"{coupon_code} coupon code deactivated"
        print(f"{RED_START}{msg}{RED_END}")
        self.coupons_list = edited_coupon_list
        self.save_list(self.coupons_file_name, self.coupons_list)

    # is ACtive
    def is_active_coupon(self, coupon_code):

        available_coupon_list = []
        msg = ""

        coupon_list_with_given_name = list(
            filter(
                lambda c: c["coupon_code"] == coupon_code,
                self.coupons_list,
            )
        )

        if len(coupon_list_with_given_name) < 1:
            msg = "We couldn't find a coupon with that code."
            # print(f"{RED_START}{msg}{RED_END}")
            return available_coupon_list

        for coupon in coupon_list_with_given_name:

            today = datetime.now()
            today_time = datetime.combine(today, time.min)
            today_timestamp = today_time.timestamp()
            expiry_date_obj = datetime.strptime(coupon["expiry_date"], "%Y-%m-%d")
            expiry_date_timestamp = expiry_date_obj.timestamp()

            if expiry_date_timestamp < today_timestamp:
                msg = "This coupon expired on 21 April 2026."
                continue

            if int(coupon["usage_limit"]) < 1:
                msg = "The usage limit for this coupon has been reached."
                continue

            if coupon["status"] != "active":
                msg = "This coupon is inactive."
                continue

            msg = "This coupon is active and ready to use."
            # print(f"{GREEN_START}{msg}{GREEN_END}")
            available_coupon_list.append(coupon)

        # print(msg)
        return available_coupon_list

    def validate_coupon():
        pass

    def log_action(self):
        pass


# | TYPE |
