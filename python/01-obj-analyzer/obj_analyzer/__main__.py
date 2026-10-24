# __main__.py

import argparse
import sys
import time

from parser import parse_obj_file
from obj_model import face_indices

import geometry
import geometry_np

STEEL_DENSITY = 7.850  # g/cm3
MM3_TO_CM3 = 1e-3
UNIT_TO_MM = {"mm": 1.0, "cm": 10.0, "dm": 100.0, "m": 1000.0}
CALC_ENGINE = {"python": geometry, "numpy": geometry_np}


def positive_density_float(value: str) -> float:
    try:
        fvalue = float(value)
        if fvalue <= 0:
            raise argparse.ArgumentTypeError("Density must be positive")
        return fvalue
    except ValueError:
        raise argparse.ArgumentTypeError("Density must be a float number")


def main() -> None:
    arg_parser = argparse.ArgumentParser(
        description="Calculate dimensions, surface area, volume and mass of an OBJ mesh."
    )
    arg_parser.add_argument("file_name", help="path to the .obj file")
    arg_parser.add_argument("-d", "--density", type=positive_density_float,
                            default=STEEL_DENSITY,
                            help="Density of opened object. Default value is density of steel: 7.85 g/cm3.")
    arg_parser.add_argument("-u", "--unit", choices=UNIT_TO_MM.keys(),
                            default="mm",
                            help="Unit of opened object. Default value is mm.")
    arg_parser.add_argument("--engine", choices=CALC_ENGINE.keys(),
                            default="python",
                            help="Type of calculation engine. Default value is python.")
    args = arg_parser.parse_args()

    file_name = args.file_name
    density = args.density
    scale_factor = UNIT_TO_MM[args.unit]
    try:
        time_start_parsing = time.perf_counter()
        opened_object = parse_obj_file(file_name)
        elapsed_parsing = time.perf_counter() - time_start_parsing
        print(f"Parse time: {elapsed_parsing * 1000:.1f} ms", file=sys.stderr)

        geom = CALC_ENGINE[args.engine]

        opened_object.v = geom.scale_vertices(opened_object.v, scale_factor)
        dx, dy, dz = geom.bounding_box_size(opened_object.v)

        print("Vertices:", len(opened_object.v))
        print("Texture vertices:", len(opened_object.vt))
        print("Normal vertices:", len(opened_object.vn))
        print(f"Dimensions: {dx:.2f} x {dy:.2f} x {dz:.2f} mm")
        print()

        total_area: float = 0.0
        total_volume: float = 0.0
        total_mass: float = 0.0

        time_start_calc = time.perf_counter()

        for mesh in opened_object.meshes:
            indices = face_indices(mesh.faces)
            area = geom.surface_area(opened_object.v, indices)
            volume = geom.object_volume(opened_object.v, indices)

            if volume < 0:
                print(
                    f"Warning: Volume value of {mesh.object_name} is negative, normals are probably inverted, value corrected",
                    file=sys.stderr)
                volume = -volume

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

        elapsed_cals = time.perf_counter() - time_start_calc
        print(f"Calculation time: {elapsed_cals * 1000:.1f} ms", file=sys.stderr)

    except FileNotFoundError:
        print(f"Error: File not found: {file_name}", file=sys.stderr)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)


if __name__ == "__main__":
    main()
