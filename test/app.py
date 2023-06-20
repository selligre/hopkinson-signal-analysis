import data
import window


def main():
    d = data.Data()
    window.action(d)
    print(f"Data.add_data() called: {d.value}")


if __name__ == "__main__":
    main()
