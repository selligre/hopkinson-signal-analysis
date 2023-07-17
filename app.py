import controllers.CalculusController as CalculusController
import views.GUImain as GUImain


def main():
    calc = CalculusController.CalculusController()
    GUImain.run(calc)


if __name__ == "__main__":
    main()
