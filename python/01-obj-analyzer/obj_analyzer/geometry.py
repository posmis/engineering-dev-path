# geometry.py
import math

type Vec3 = tuple[float, float, float]

ORIGIN: Vec3 = (0.0, 0.0, 0.0)

def bounding_box(vertices: list[Vec3]) -> tuple[Vec3, Vec3]:
    if not vertices:
        raise ValueError("Mesh has no vertices")
    xs, ys, zs = zip(*vertices)
    x_max, y_max, z_max = max(xs), max(ys), max(zs)
    x_min, y_min, z_min = min(xs), min(ys), min(zs)
    return (x_min, y_min, z_min), (x_max, y_max, z_max)


def bounding_box_size(vertices: list[Vec3]) -> Vec3:
    mins, maxs = bounding_box(vertices)
    return maxs[0] - mins[0], maxs[1] - mins[1], maxs[2] - mins[2]


def vector_sub(a: Vec3, b: Vec3) -> Vec3:
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


def vector_cross(a: Vec3, b: Vec3) -> Vec3:
    return a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]


def vector_dot(a: Vec3, b: Vec3) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def vector_len(v: Vec3) -> float:
    return math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)


def triangle_area(a: Vec3, b: Vec3, c: Vec3) -> float:
    return vector_len(vector_cross(vector_sub(b, a), vector_sub(c, a))) / 2


def polygon_area(vertices: list[Vec3]) -> float:
    area: float = 0.0
    for i in range(len(vertices) - 2):
        area += triangle_area(vertices[0], vertices[i + 1], vertices[i + 2])
    return area


def surface_area(vertices: list[Vec3], faces: list[list[int]]) -> float:
    area: float = 0.0
    for face in faces:
        area += polygon_area([vertices[i] for i in face])
    return area


def tetrahedron_volume(a: Vec3, b: Vec3, c: Vec3, d: Vec3) -> float:
    return vector_dot(vector_sub(b, a), vector_cross(vector_sub(c, a), vector_sub(d, a))) / 6


def polygon_volume(vertices: list[Vec3]) -> float:
    volume: float = 0.0
    for i in range(len(vertices) - 2):
        volume += tetrahedron_volume(ORIGIN, vertices[0], vertices[i + 1], vertices[i + 2])
    return volume


def object_volume(vertices: list[Vec3], faces: list[list[int]]) -> float:
    volume: float = 0.0
    for face in faces:
        volume += polygon_volume([vertices[i] for i in face])
    return volume
