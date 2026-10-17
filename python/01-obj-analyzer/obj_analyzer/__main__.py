# main.py
import sys
from parser import parse_obj_file
from obj_model import ObjData

from geometry import bounding_box_size

def main() -> None:
    opened_object = parse_obj_file(sys.argv[1])
    print(len(opened_object.v))
    print(len(opened_object.vt))
    print(len(opened_object.vn))

    try:
        print(bounding_box_size(opened_object.v))
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
