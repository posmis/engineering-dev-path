# main.py
import sys
from parser import parse_obj_file

from geometry import bounding_box_size

def main() -> None:
    file_name = sys.argv[1]
    try:
        opened_object = parse_obj_file(file_name)

        print("Vertices:", len(opened_object.v))
        print("Texture vertices:", len(opened_object.vt))
        print("Normal vertices:", len(opened_object.vn))
        print("Dimensions:", " x ".join(map(str, bounding_box_size(opened_object.v))), "mm")
    except FileNotFoundError:
        print(f"Error: file not found: {file_name}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
