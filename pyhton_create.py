import segno
import numpy as np
from shapely.geometry import Polygon
from shapely.ops import unary_union
from trimesh.creation import extrude_polygon
import trimesh
import sys

# Get tracker code from command line
if len(sys.argv) < 2:
    print("Usage: python qr_generator.py TRACKER_CODE")
    sys.exit(1)

tracker_code = sys.argv[1]
# Settings
data = f"geo.co/{tracker_code}"
module_size = 1.2
depth = 1.2
quiet_zone = 1
qr = segno.make(data, error='L', micro=False)
matrix = np.array([[int(cell) for cell in row] for row in qr.matrix])
size = matrix.shape[0]

polys = []
for y in range(-quiet_zone, size + quiet_zone):
    for x in range(-quiet_zone, size + quiet_zone):
        if y < 0 or y >= size or x < 0 or x >= size or matrix[y, x] == 0:
            square = Polygon([
                (x * module_size, -y * module_size),
                ((x + 1) * module_size, -y * module_size),
                ((x + 1) * module_size, -(y + 1) * module_size),
                (x * module_size, -(y + 1) * module_size)
            ])
            polys.append(square)
merged = unary_union(polys)
# Ensure merged is always a list of polygons
if isinstance(merged, Polygon):
    polys = [merged]
elif hasattr(merged, 'geoms'):
    polys = list(merged.geoms)
else:
    raise ValueError("Unexpected geometry type: {}".format(type(merged)))

mesh = trimesh.util.concatenate([extrude_polygon(p, height=depth) for p in polys])
mesh.export(f"{tracker_code}_qr_inverse_easyprint.stl")
