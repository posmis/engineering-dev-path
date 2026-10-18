# parser.py

from obj_model import FaceVertex, ObjMesh, ObjData


def parse_obj_file(file_name: str) -> ObjData:
    vertices = []
    vertex_textures = []
    vertex_normals = []

    current_mesh = ObjMesh('unnamed', [])
    meshes = [current_mesh]

    with open(file_name, "r", encoding="UTF-8") as file:
        for line in file:
            parts = line.split()
            if not parts:
                continue
            elif parts[0] == "o":
                name = " ".join(parts[1:]) or "unnamed"
                current_mesh = ObjMesh(name, [])
                meshes.append(current_mesh)
            elif parts[0] == "v":
                coordinates_count = len(parts[1:])
                if coordinates_count < 3:
                    raise ValueError(f"Invalid vertex coordinates count: {coordinates_count}, must be 3")
                vertices.append(tuple(map(float, parts[1:4])))
            elif parts[0] == "vt":
                vt = list(map(float, parts[1:4]))
                vt += [0.0] * (3 - len(vt))
                vertex_textures.append(tuple(vt))
            elif parts[0] == "vn":
                coordinates_count = len(parts[1:])
                if coordinates_count < 3:
                    raise ValueError(f"Invalid normal vertex coordinates count: {coordinates_count}, must be 3")
                vertex_normals.append(tuple(map(float, parts[1:4])))
            elif parts[0] == "f":
                current_mesh.faces.append(
                    parse_face(parts[1:], (len(vertices), len(vertex_textures), len(vertex_normals))))
    meshes = [mesh for mesh in meshes if mesh.faces]

    return ObjData(file_name, vertices, vertex_textures, vertex_normals, meshes)


def parse_face(parts: list[str], counts: tuple[int, int, int]) -> list[FaceVertex]:
    face = []
    for part in parts:
        indices_text = part.split("/")
        indices_text += [""] * (3 - len(indices_text))
        if len(indices_text) > 3:
            raise ValueError(f"Invalid face vertex {part!r} (expected v, v/vt, v//vn or v/vt/vn)")

        v, vt, vn = (parse_index(index_text, count) for index_text, count in zip(indices_text, counts))

        face.append(FaceVertex(v, vt, vn))
    return face


def parse_index(index_text: str, count: int) -> int | None:
    if not index_text:
        return None
    index = int(index_text)
    if index == 0:
        raise ValueError("Face index 0 is invalid (OBJ indices start at 1)")
    if abs(index) > count:
        raise ValueError(f"Face index {index} is out of range (only {count} available)")
    if index < 0:
        return count + index
    return index - 1
