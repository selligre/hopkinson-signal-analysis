from controllers.CalculusController import CalculusController
from views.GUImain import GUImain


def main():
    calc = CalculusController.CalculusController()
    GUImain.run(calc)


if __name__ == "__main__":
    main()
