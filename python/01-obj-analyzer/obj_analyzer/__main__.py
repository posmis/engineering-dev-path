# main.py
import sys
from parser import parse_obj_file

from geometry import bounding_box_size

def main() -> None:
    try:
        opened_object = parse_obj_file(sys.argv[1])

        print("Vertices:", len(opened_object.v))
        print("Texture vertices:", len(opened_object.vt))
        print("Normal vertices:", len(opened_object.vn))
        print("Dimensions:", " x ".join(map(str, bounding_box_size(opened_object.v))), "mm")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
