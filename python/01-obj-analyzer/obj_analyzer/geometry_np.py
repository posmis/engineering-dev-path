# geometry_np.py

import numpy as np

from vector import Vec3, ORIGIN


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


def triangulate(faces: list[list[int]]) -> np.ndarray:
    triangulated_faces = []
    for face in faces:
        for i in range(len(face) - 2):
            triangulated_faces.append([face[0], face[i + 1], face[i + 2]])
    return np.array(triangulated_faces, dtype=int)


def surface_area(vertices: list[Vec3], faces: list[list[int]]) -> float:
    if not vertices:
        raise ValueError("Mesh has no vertices")

    np_vertices = np.array(vertices, dtype=float)
    triangles = triangulate(faces)
    points = np_vertices[triangles]

    a = points[:, 0]
    b = points[:, 1]
    c = points[:, 2]

    normals = np.cross(b - a, c - a)
    areas = np.linalg.norm(normals, axis=1) / 2

    return float(areas.sum())


def object_volume(vertices: list[Vec3], faces: list[list[int]]) -> float:
    if not vertices:
        raise ValueError("Mesh has no vertices")

    np_vertices = np.array(vertices, dtype=float)
    triangles = triangulate(faces)
    points = np_vertices[triangles]

    b = points[:, 0]
    c = points[:, 1]
    d = points[:, 2]

    normals = np.cross(c, d)
    volumes = (b * normals).sum(axis=1) / 6

    return float(volumes.sum())
