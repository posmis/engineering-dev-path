# main.py
import sys
from parser import parse_obj_file

from geometry import bounding_box_size, surface_area, object_volume
from obj_model import face_indices

STEEL_DENSITY = 7.850  # g/sm3


def main() -> None:
    file_name = sys.argv[1]
    try:
        opened_object = parse_obj_file(file_name)

        print("Vertices:", len(opened_object.v))
        print("Texture vertices:", len(opened_object.vt))
        print("Normal vertices:", len(opened_object.vn))
        print("Dimensions:", " x ".join(map(str, bounding_box_size(opened_object.v))), "mm")
        print()

        for mesh in opened_object.meshes:
            indices = face_indices(mesh.faces)
            area = surface_area(opened_object.v, indices)
            volume = object_volume(opened_object.v, indices)
            mass = volume * STEEL_DENSITY / 1000

            print(f"Surface area of {mesh.object_name}: {area:.2f} mm^2")
            print(f"Volume of {mesh.object_name}: {volume:.2f} mm^3")
            print(f"Mass of {mesh.object_name}: {mass:.2f} g")
            print()


    except FileNotFoundError:
        print(f"Error: file not found: {file_name}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
