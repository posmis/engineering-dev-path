# geometry_np.py

import numpy as np

from vector import Vec3


def scale_vertices(vertices: list[Vec3], factor: float) -> list[Vec3]:
    np_vertices = np.array(vertices) * factor

    return [(x, y, z) for x, y, z in np_vertices.tolist()]


def bounding_box(vertices: list[Vec3]) -> tuple[Vec3, Vec3]:
    if not vertices:
        raise ValueError("Mesh has no vertices")

    np_vertices = np.array(vertices)
    x_min, y_min, z_min = np_vertices.min(axis=0)
    x_max, y_max, z_max = np_vertices.max(axis=0)

    return (float(x_min), float(y_min), float(z_min)), (float(x_max), float(y_max), float(z_max))


def bounding_box_size(vertices: list[Vec3]) -> Vec3:
    if not vertices:
        raise ValueError("Mesh has no vertices")

    np_vertices = np.array(vertices)
    size_x, size_y, size_z = np_vertices.max(axis=0) - np_vertices.min(axis=0)

    return float(size_x), float(size_y), float(size_z)

# def triangle_area(a: Vec3, b: Vec3, c: Vec3) -> float:
#
#
# def polygon_area(vertices: list[Vec3]) -> float:
#
#
# def surface_area(vertices: list[Vec3], faces: list[list[int]]) -> float:
#
#
# def tetrahedron_volume(a: Vec3, b: Vec3, c: Vec3, d: Vec3) -> float:
#
#
# def polygon_volume(vertices: list[Vec3]) -> float:
#
#
# def object_volume(vertices: list[Vec3], faces: list[list[int]]) -> float:
