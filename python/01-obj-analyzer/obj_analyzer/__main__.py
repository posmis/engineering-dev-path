# main.py
import sys
from parser import parse_obj_file
from obj_model import ObjData

def main() -> None:
    opened_object = parse_obj_file(sys.argv[1])
    print(len(opened_object.v))
    print(len(opened_object.vt))
    print(len(opened_object.vn))

    print(opened_object.vt)

    print(opened_object.meshes)

if __name__ == "__main__":
    main()
