from controllers.CalculusController import CalculusController
from views import *


def main():
    calc = CalculusController.CalculusController()
    GUImain.run(calc)


if __name__ == "__main__":
    main()
