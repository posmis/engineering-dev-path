# geometry.py

def bounding_box(vertices: list[tuple[float, float, float]]) -> tuple[
    tuple[float, float, float], tuple[float, float, float]]:
    if not vertices:
        raise ValueError("Mesh has no vertices")

    xs, ys, zs = zip(*vertices)
    x_max, y_max, z_max = max(xs), max(ys), max(zs)
    x_min, y_min, z_min = min(xs), min(ys), min(zs)

    return (x_min, y_min, z_min), (x_max, y_max, z_max)

def bounding_box_size(vertices: list[tuple[float, float, float]]) -> tuple[float, float, float]:
    mins, maxs = bounding_box(vertices)
    return maxs[0] - mins[0], maxs[1] - mins[1], maxs[2] - mins[2]
