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

    def fetch_product(self, product_id):

        filtered_product_list = list(
            filter(lambda p: p["product_id"] == product_id, self.product_list)
        )
        if len(filtered_product_list) == 1:
            return filtered_product_list[0]
        return False

    def update_product(self, product_id, product_name, quantity, price):

        if quantity.isdigit() and price.isdigit():
            new_product_obj = {
                "product_id": product_id,
                "product_name": product_name,
                "quantity": int(quantity),
                "price": int(price),
                "product_type": 1,
            }
            new_product_list = list(
                map(
                    lambda p: (
                        new_product_obj
                        if new_product_obj["product_id"] == p["product_id"]
                        else p
                    ),
                    self.product_list,
                )
            )

            self.product_list = new_product_list
            self.save_product_list()
            msg = f"UPDATED! ID {product_id}"
            print(f"{GREEN_START}{msg}{GREEN_END}")
            return True
        else:
            msg = "Please enter a valid number for price and quantity."
            print(f"{RED_START}{msg}{RED_END}")
            return False

    def delete_product(self, product_id):
        new_product_list = list(
            filter(
                lambda p: p["product_id"] != product_id,
                self.product_list,
            )
        )
        self.product_list = new_product_list
        self.save_product_list()
        msg = f"Deleted! ID {product_id}"
        print(f"{GREEN_START}{msg}{GREEN_END}")
        return True

    def search_product(self, product_name):
        # p["product_name"].lower().contains(product_name.lower()),

        search_products_list = list(
            filter(
                lambda p: product_name.lower() in p["product_name"].lower(),
                self.product_list,
            )
        )

        if len(search_products_list) > 0:
            msg = f"Found {len(search_products_list)} Results"
            print(f"{GREEN_START}{msg}{GREEN_END}")

            msg = f"{"Product ID".rjust(1)} | {"Product Name".ljust(20)} | {"Price".ljust(10)} | {"Quantity"}"
            print(f"{YELLOW_START}{msg}{YELLOW_END}")
            print("_________________________________________________________")

            list(
                map(
                    lambda p: print(
                        f"{p["product_id"].ljust(10)} | {p["product_name"][0:15].ljust(20)} | {str(p["price"]).ljust(10)} | {p["quantity"]}"
                    ),
                    search_products_list,
                )
            )
            return True
        return False

    def view_all_product(self):
        pass
