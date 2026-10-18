# main.py
import sys
import argparse

from parser import parse_obj_file
from geometry import bounding_box_size, surface_area, object_volume
from obj_model import face_indices

STEEL_DENSITY = 7.850  # g/cm3
MM3_TO_CM3 = 1e-3


def main() -> None:
    arg_parcer = argparse.ArgumentParser()
    arg_parcer.add_argument("file_name", type=str, help="file name")
    arg_parcer.add_argument("--density", type=float,
                            help="Density of opened object. Default value is density of steel: 7.85 g/cm3.",
                            default=STEEL_DENSITY)
    args = arg_parcer.parse_args()

    file_name = args.file_name
    density = args.density
    try:
        opened_object = parse_obj_file(file_name)

        print("Vertices:", len(opened_object.v))
        print("Texture vertices:", len(opened_object.vt))
        print("Normal vertices:", len(opened_object.vn))
        print("Dimensions:", " x ".join(map(str, bounding_box_size(opened_object.v))), "mm")
        print()

        total_area: float = 0.0
        total_volume: float = 0.0
        total_mass: float = 0.0
        for mesh in opened_object.meshes:
            indices = face_indices(mesh.faces)
            area = surface_area(opened_object.v, indices)
            volume = object_volume(opened_object.v, indices)
            mass = volume * MM3_TO_CM3 * density

            total_area += area
            total_volume += volume
            total_mass += mass

            print(f"Surface area of {mesh.object_name}: {area:.2f} mm^2")
            print(f"Volume of {mesh.object_name}: {volume:.2f} mm^3")
            print(f"Mass of {mesh.object_name}: {mass:.2f} g")
            print()

        print(f"Total surface area of {file_name}: {total_area:.2f} mm^2")
        print(f"Total volume of {file_name}: {total_volume:.2f} mm^3")
        print(f"Total mass of {file_name}: {total_mass:.2f} g")
        print()

    except FileNotFoundError:
        print(f"Error: file not found: {file_name}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
