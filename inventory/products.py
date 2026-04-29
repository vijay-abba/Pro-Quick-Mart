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


class GeneralProducts:
    count = 0

    def __init__(self):

        self.file_path = Path("data")
        self.file_name = self.file_path / f"products.txt"
        self.products = []
        self.fetch_product_list()

        if len(self.product_list) != 0:
            new_count = self.product_list[-1]["product_id"].split("-")[1]
            GeneralProducts.count = int(new_count) + 1

    def fetch_product_list(self):
        # if no file create empty
        if not self.file_name.is_file():
            with open(self.file_name, "w") as f:
                f.write(json.dumps([]))

        with open(self.file_name, "r") as f:
            str_product_list = f.readline()
            product_list = json.loads(str_product_list)
            self.product_list = product_list

    def save_product_list(self):
        str_product_list = json.dumps(self.product_list)
        with open(self.file_name, "w") as f:
            f.write(str_product_list)
        # self.fetch_product_list()

    def add_product(self, product_name, quantity, price):

        is_product_exists = list(
            filter(lambda p: p["product_name"] == product_name, self.product_list)
        )

        if len(is_product_exists) >= 1:
            msg = "This product name is already in use"
            print(f"{RED_START}{msg}{RED_END}")
            return False
        else:
            if quantity.isdigit() and price.isdigit():
                product_id = f"PRD-{GeneralProducts.count:04d}"
                GeneralProducts.count += 1
                new_product_obj = {
                    "product_id": product_id,
                    "product_name": product_name,
                    "quantity": int(quantity),
                    "price": int(price),
                    "product_type": 1,
                }
                self.product_list.append(new_product_obj)
                self.save_product_list()
                msg = f"ADDED! ID {product_id}"
                print(f"{GREEN_START}{msg}{GREEN_END}")
                return True
            else:
                msg = "Please enter a valid number for price and quantity."
                print(f"{RED_START}{msg}{RED_END}")
                return False

    def update_product(self):
        pass

    def delete_product(self):
        pass

    def search_product(self):
        pass

    def view_all_product(self):
        pass
