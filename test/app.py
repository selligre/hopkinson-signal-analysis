import data
import os


# global d


def main():
    d = data.Data()
    print(f"data.Data() called: {d.value}")
    print(f"d.address = {d}")
    os.system("python ./test/window.py")
    return d


if __name__ == "__main__":
    main(d)
