# parser.py

from obj_model import FaceVertex, ObjMesh, ObjData


def parse_obj_file(file_name: str) -> ObjData:
    vertices = []
    vertex_textures = []
    vertex_normals = []

    current_mesh = ObjMesh(None, [])
    meshes = [current_mesh]

    with open(file_name, "r", encoding="UTF-8") as file:
        for line in file:
            parts = line.split()
            if not parts:
                continue
            elif parts[0] == "o":
                name = " ".join(parts[1:]) or None
                current_mesh = ObjMesh(name, [])
                meshes.append(current_mesh)
            elif parts[0] == "v":
                vertices.append(tuple(map(float, parts[1:4])))
            elif parts[0] == "vt":
                vertex_textures.append(tuple(map(float, parts[1:4])))
            elif parts[0] == "vn":
                vertex_normals.append(tuple(map(float, parts[1:4])))
            elif parts[0] == "f":
                current_mesh.faces.append(parse_face(parts[1:]))
    meshes = [mesh for mesh in meshes if mesh.faces]


    return ObjData(file_name, vertices, vertex_textures, vertex_normals, meshes)

def parse_face(parts: list[str]) -> list[FaceVertex]:
    face = []
    for part in parts:
        indices = list(map(parse_index, part.split('/')))
        for _ in range(3 - len(indices)):
            indices.append(None)

        v, vt, vn = indices

        face.append(FaceVertex(v, vt, vn))
    return face

def parse_index(text: str) -> int | None:
    if not text:
        return None
    return int(text) - 1
