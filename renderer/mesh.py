from renderer.vector3 import Vector3

class Mesh:

    def __init__(self, vertices, triangles):
        self.vertices = vertices
        self.triangles = triangles

def is_front_facing(a, b, c, cam_pos):
    ab = b - a
    ac = c - a

    n = Vector3.cross(ab,ac)
    v = cam_pos - a

    d = Vector3.dot(n,v)
    if d > 0: return True
    else: return False