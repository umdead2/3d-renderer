from renderer.vector3 import Vector3

def calculate_lighting(normal, light_dir, ambient):
    n = Vector3.normalize(normal)
    l = Vector3.normalize(light_dir)

    d = max(0,Vector3.dot(n,l))

    i = ambient + (1-ambient) * d

    return i