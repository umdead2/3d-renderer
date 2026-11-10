from renderer.vector3 import Vector3
from renderer.mesh import Mesh

def create_cube():
    vertices = [
        Vector3(-1, -1, -1),  # 0
        Vector3( 1, -1, -1),  # 1
        Vector3( 1,  1, -1),  # 2
        Vector3(-1,  1, -1),  # 3
        Vector3(-1, -1,  1),  # 4
        Vector3( 1, -1,  1),  # 5
        Vector3( 1,  1,  1),  # 6
        Vector3(-1,  1,  1)   # 7
    ]
    triangles = [
        (0, 2, 1), (0, 3, 2),  # Back
        (4, 5, 6), (4, 6, 7),  # Front
        (0, 1, 5), (0, 5, 4),  # Bottom
        (3, 7, 6), (3, 6, 2),  # Top
        (0, 4, 7), (0, 7, 3),  # Left
        (1, 2, 6), (1, 6, 5)   # Right
    ]

    return Mesh(vertices, triangles)