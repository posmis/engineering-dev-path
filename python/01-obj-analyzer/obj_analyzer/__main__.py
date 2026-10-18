# main.py
import argparse

from parser import parse_obj_file
from geometry import bounding_box_size, surface_area, object_volume
from obj_model import face_indices, scale_vertices

STEEL_DENSITY = 7.850  # g/cm3
MM3_TO_CM3 = 1e-3
UNIT_TO_MM = {"mm": 1.0, "cm": 10.0, "dm": 100.0, "m": 1000.0}


def positive_density_float(value: str) -> float:
    fvalue = float(value)
    if fvalue <= 0:
        raise argparse.ArgumentTypeError(f"Density must be positive")
    return fvalue


def main() -> None:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("file_name", type=str, help="file name")
    arg_parser.add_argument("-d", "--density", type=positive_density_float,
                            default=STEEL_DENSITY,
                            help="Density of opened object. Default value is density of steel: 7.85 g/cm3.")
    arg_parser.add_argument("-u", "--unit", choices=UNIT_TO_MM.keys(), type=str,
                            default="mm",
                            help="Unit of opened object. Default value is mm.")
    args = arg_parser.parse_args()

    file_name = args.file_name
    density = args.density
    scale_factor = UNIT_TO_MM[args.unit]
    try:
        opened_object = parse_obj_file(file_name)
        opened_object.v = scale_vertices(opened_object.v, scale_factor)

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
