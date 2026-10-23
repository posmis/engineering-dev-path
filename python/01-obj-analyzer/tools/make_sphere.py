# make_sphere.py

import math
import argparse

type Vec3 = tuple[float, float, float]


def sphere_point(radius: float, theta: float, phi: float) -> Vec3:
    x: float = radius * math.sin(theta) * math.cos(phi)
    y: float = radius * math.sin(theta) * math.sin(phi)
    z: float = radius * math.cos(theta)

    return x, y, z


def sphere_vertices(radius: float, segments: int) -> list[Vec3]:
    points = [(0.0, 0.0, radius)]

    for i in range(1, segments):
        theta: float = math.pi * i / segments
        for j in range(segments):
            phi: float = 2 * math.pi * j / segments
            points.append(sphere_point(radius, theta, phi))
    points.append((0.0, 0.0, -radius))

    return points


def vertex_index(ring: int, position: int, segments: int) -> int:
    if ring == 0:
        return 0
    elif ring == segments:
        return segments * (segments - 1) + 1
    else:
        return (ring - 1) * segments + (position % segments) + 1


def sphere_faces(segments: int) -> list[list[int]]:
    faces = []

    for i in range(segments):
        faces.append([vertex_index(0, 0, segments), vertex_index(1, i, segments), vertex_index(1, i + 1, segments)])

    for i in range(2, segments):
        for j in range(segments):
            faces.append(
                [vertex_index(i - 1, j, segments), vertex_index(i, j, segments), vertex_index(i, j + 1, segments),
                 vertex_index(i - 1, j + 1, segments)])

    for i in range(segments):
        faces.append([vertex_index(segments - 1, i, segments), vertex_index(segments, 0, segments),
                      vertex_index(segments - 1, i + 1, segments)])

    return faces


def write_obj(path: str, name: str, vertices: list[Vec3], faces: list[list[int]]) -> None:
    with open(path, "w", encoding="UTF-8") as file:
        file.write(f"# Mesh of UV sphere with {len(vertices)} vertices and {len(faces)} faces.\n")
        file.write(f"o {name}\n\n")

        for vertex in vertices:
            line = " ".join(map(str, vertex))
            file.write(f"v {line}\n")

        file.write("\n")

        for face in faces:
            line = " ".join(str(f + 1) for f in face)
            file.write(f"f {line}\n")


def radius_value(value: str) -> float:
    try:
        fvalue = float(value)
        if fvalue <= 0.0:
            raise argparse.ArgumentTypeError("Radius must be more than 0")
        return fvalue
    except ValueError:
        raise argparse.ArgumentTypeError("Radius must be a float number")


def count_of_segments(value: str) -> int:
    try:
        value = int(value)
        if value < 3:
            raise argparse.ArgumentTypeError("Segments must be at least 3")
        return value
    except ValueError:
        raise argparse.ArgumentTypeError("Segments must be a integer number")


def main() -> None:
    arg_parser = argparse.ArgumentParser(
        description="Generate a UV sphere mesh and save it as a Wavefront .obj file."
    )
    arg_parser.add_argument("-r", "--radius", type=radius_value, default=1.0,
                            help="sphere radius in mm (default: %(default)s)")
    arg_parser.add_argument("-s", "--segments", type=count_of_segments, default=5,
                            help="number of divisions in latitude and longitude, at least 3; "
                                 "the mesh has segments^2 faces (default: %(default)s)")
    arg_parser.add_argument("-o", "--output", default="sphere.obj",
                            help="path to the output .obj file (default: %(default)s)")
    args = arg_parser.parse_args()

    vertices = sphere_vertices(args.radius, args.segments)
    faces = sphere_faces(args.segments)
    write_obj(args.output, "Sphere", vertices, faces)


if __name__ == "__main__":
    main()
