# obj_model.py
from dataclasses import dataclass
from typing import NamedTuple


class FaceVertex(NamedTuple):
    v: int  # индекс в списке вершин (с 0)
    vt: int | None  # индекс текстурной координаты или None
    vn: int | None  # индекс нормали или None


@dataclass
class ObjMesh:
    object_name: str | None
    faces: list[list[FaceVertex]]


@dataclass
class ObjData:
    file_name: str
    v: list[tuple[float, float, float]]
    vt: list[tuple[float, float, float]]
    vn: list[tuple[float, float, float]]
    meshes: list[ObjMesh]
