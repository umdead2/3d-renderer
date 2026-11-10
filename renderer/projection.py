import math
from renderer.vector3 import Vector3

def project_vertex(vector, width, height, fov):
    if vector.z <= 0: return
    f = (width/2)/ math.tan(math.radians(fov / 2))
    x_screen = (width/2) + (vector.x* (f/vector.z))
    y_screen = (height/2) - (vector.y* (f/vector.z))

    return (x_screen, y_screen)

vertex = Vector3(2, 3, 5)
result = project_vertex(vertex, 640, 480, 90)

print(result)