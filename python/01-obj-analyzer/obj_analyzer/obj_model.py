# obj_model.py

from dataclasses import dataclass
from typing import NamedTuple

from vector import Vec3


class FaceVertex(NamedTuple):
    v: int  # индекс в списке вершин (с 0)
    vt: int | None  # индекс текстурной координаты или None
    vn: int | None  # индекс нормали или None


@dataclass
class ObjMesh:
    object_name: str
    faces: list[list[FaceVertex]]


@dataclass
class ObjData:
    file_name: str
    v: list[Vec3]
    vt: list[Vec3]
    vn: list[Vec3]
    meshes: list[ObjMesh]


def face_indices(faces: list[list[FaceVertex]]) -> list[list[int]]:
    return [[face_vertex.v for face_vertex in face] for face in faces]
