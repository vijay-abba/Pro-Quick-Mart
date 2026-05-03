# colors.py

RED_START = "\033[91m"
RED_END = "\033[0m"

GREEN_START = "\033[92m"
GREEN_END = "\033[0m"

BLUE_START = "\033[94m"
BLUE_END = "\033[0m"

YELLOW_START = "\033[93m"
YELLOW_END = "\033[0m"

CYAN_START = "\033[96m"
CYAN_END = "\033[0m"


class ColorPrint:

    @classmethod
    def red(cls, data):
        print(f"{RED_START}{data}{RED_END}")

    @classmethod
    def green(cls, data):
        print(f"{GREEN_START}{data}{GREEN_END}")

    @classmethod
    def blue(cls, data):
        print(f"{BLUE_START}{data}{BLUE_END}")

    @classmethod
    def yellow(cls, data):
        print(f"{YELLOW_START}{data}{YELLOW_END}")

    @classmethod
    def cyan(cls, data):
        print(f"{CYAN_START}{data}{CYAN_END}")


# ColorPrint.red("OK")
# ColorPrint.green("OK")
# ColorPrint.blue("OK")
# ColorPrint.yellow("OK")
# ColorPrint.cyan("OK")
