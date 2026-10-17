# parser.py

from obj_model import ObjData


def parse_obj_file(file_name: str) -> ObjData:
    vertices = []
    vertex_textures = []
    vertex_normals = []
    meshes = []

    with open(file_name, "r", encoding="UTF-8") as file:
        for line in file:
            parts = line.split()
            if not parts:
                continue
            elif parts[0] == "v":
                vertices.append(tuple(map(float, parts[1:4])))
            elif parts[0] == "vt":
                vertex_textures.append(tuple(map(float, parts[1:3])))
            elif parts[0] == "vn":
                vertex_normals.append(tuple(map(float, parts[1:4])))
            elif parts[0] == "o":
                pass


    return ObjData(file_name, vertices, vertex_textures, vertex_normals, meshes)

