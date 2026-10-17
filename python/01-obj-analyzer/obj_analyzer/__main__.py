# main.py
import sys
import obj_model


def main() -> None:
    with open(sys.argv[1], "r", encoding="UTF-8") as file:
        for line in file:
            print(line.strip())


if __name__ == "__main__":
    main()
