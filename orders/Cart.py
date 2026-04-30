from pathlib import Path
import json
from functools import reduce
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


class Cart:

    def __init__(self):
        self.file_path = Path("data")
        self.cart_file_name = self.file_path / f"cart.txt"
        self.product_file_name = self.file_path / f"products.txt"

        self.cart = []
        self.cart = self.fetch_list(self.cart_file_name)

        self.product_list = []
        self.product_list = self.fetch_list(self.product_file_name)

        self.bill = []

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

    def fetch_product(self, product_id, product_type=0):

        filtered_product_list = []

        if product_type != 0:
            filtered_product_list = list(
                filter(
                    lambda p: p["product_id"] == product_id
                    and p["product_type"] == product_type,
                    self.product_list,
                )
            )
        else:
            filtered_product_list = list(
                filter(
                    lambda p: p["product_id"] == product_id,
                    self.product_list,
                )
            )

        if len(filtered_product_list) == 1:
            return filtered_product_list[0]
        return False

    # Testing Method
    def print_cart_product_list(self):
        print(self.cart)
        print(self.product_list)

        self.save_list(self.product_file_name, ["apples", "bananas"])
        self.save_list(self.cart_file_name, ["apples", "bananas"])

    def add_to_cart(self, product_id, req_quantity):

        product = self.fetch_product(product_id)

        product_in_cart = list(
            filter(lambda p: p["product_id"] == product_id, self.cart)
        )

        if len(product_in_cart) >= 1:
            msg = f"Product already exists in the cart."
            print(f"{RED_START}{msg}{RED_END}")
        else:
            new_cart_item = {
                "product_id": product["product_id"],
                "product_name": product["product_name"],
                "req_quantity": int(req_quantity),
                "price": product["price"],
                "product_type": product["product_type"],
            }
            self.cart.append(new_cart_item)
            self.save_list(self.cart_file_name, self.cart)
            g_msg = f"Added: {product["product_name"]} x{req_quantity}"
            print(f"{GREEN_START}{g_msg}{GREEN_END}")

    def get_bill_object(self):
        subtotal = reduce(
            lambda acc, curr: acc + (curr["price"] * curr["req_quantity"]),
            self.cart,
            0,
        )

        discount = 0
        discount_type = 0
        if subtotal >= 10000:
            discount_type = 15
            discount = (15 / 100) * subtotal
        elif subtotal >= 5000:
            discount_type = 10
            discount = (10 / 100) * subtotal

        net_amount = subtotal - discount

        gst = (18 / 100) * net_amount

        grand_total = net_amount + gst

        bill_obj = {
            "subtotal": subtotal,
            "discount": discount,
            "discount_type": discount_type,
            "net_amount": net_amount,
            "gst": gst,
            "grand_total": grand_total,
        }

        self.bill = bill_obj

        return bill_obj

    def print_invoice(self, logged_in_user):
        self.get_bill_object()

        divider = "================================================"
        heading = "              QUICKMART - INVOICE"
        heading = f"{divider}\n{heading}\n{divider}"
        print(f"{BLUE_START}{heading}{BLUE_END}")

        #
        now = datetime.today()
        date_string = f"Date: {now.date()}"
        user_string = f"Cahier: {logged_in_user['username']}"
        date_user_text = f"{date_string.ljust(20)}{user_string.rjust(25)}"
        print(date_user_text)

        divider_two = "------------------------------------------------"
        print(divider_two)

        sub_heading_string = (
            f"{'Item'.ljust(15)}   {'Qty'.ljust(6)}   {'Price'.ljust(9)}   {'Subtotal'}"
        )

        print(sub_heading_string)

        for item in self.cart:

            name = item["product_name"]
            quantity = item["req_quantity"]
            price = item["price"]
            subtotal = quantity * price

            fmt_name = name[:13].ljust(13)

            fmt_quantity = str(quantity).rjust(4)

            f_price = f"{price:.2f}"
            fmt_price = str(f_price).rjust(9)

            f_subtotal = f"{subtotal:.2f}"
            fmt_subtotal = str(f_subtotal).rjust(12)

            line = f"{fmt_name}   {fmt_quantity}   {fmt_price}   {fmt_subtotal}"
            print(line)

        print(divider_two)

        bill = self.get_bill_object()

        f_total_subtotal = f"{bill["subtotal"]:.2f}"
        pad_f_total_subtotal = f_total_subtotal.rjust(38)
        subtotal = f"{'Subtotal:'}{pad_f_total_subtotal}"
        print(subtotal)

        f_discount_amt = f"-{bill["discount"]:.2f}"
        discount_type = bill["discount_type"]
        print(f"Discount ({discount_type}%):{f_discount_amt.rjust(32)}")

        f_gst_amt = f"{bill["gst"]:.2f}"
        print(f"GST (18%):{f_gst_amt.rjust(37)}")

        f_grand_total = f"{bill["grand_total"]:.2f}"
        # print(f_grand_total)
        print(f"GRAND TOTAL:{f_grand_total.rjust(35)}")

        print(divider)

    def remove_from_cart(self, product_id):
        print("remove form caft")

        cart_item = list(filter(lambda p: p["product_id"] == product_id, self.cart))

        if len(cart_item) == 0:
            msg = "Item ID not found in cart."
            print(f"{RED_START}{msg}{RED_END}")
        else:
            filtered_cart_list = list(
                filter(lambda p: p["product_id"] != product_id, self.cart)
            )
            self.cart = filtered_cart_list
            self.save_list(self.cart_file_name, self.cart)
            msg = f"{product_id} item removed."
            print(f"{RED_START}{msg}{RED_END}")
