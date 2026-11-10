import pygame
import math

from renderer.framebuffer import Framebuffer
from renderer.primitives import create_cube
from renderer.vector3 import Vector3
from renderer.projection import project_vertex
from renderer.mesh import is_front_facing
from renderer.lighting import calculate_lighting


pygame.init()

width = 640
height = 480
fov = 90

screen = pygame.display.set_mode((width, height))

framebuffer = Framebuffer(width,height)

running = True

cube = create_cube()
angle = 0

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

while running:
    angle += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    framebuffer.clear((15, 15, 20))
    values = []
    transformed_vertices = []
    for i in range(len(cube.vertices)):
        rotated = cube.vertices[i].rotate_y(math.radians(angle))
        v = rotated + Vector3(0,0,5)
        
        projected = project_vertex(v, width, height, fov)
        values.append((projected[0], projected[1], v.z))
        transformed_vertices.append(v)
    for a, b, c in cube.triangles:
        v1 = values[a]
        v2 = values[b]
        v3 = values[c]

        tv1 = transformed_vertices[a]
        tv2 = transformed_vertices[b]
        tv3 = transformed_vertices[c]

        x1, y1, z1 = round(v1[0]), round(v1[1]), v1[2]
        x2, y2, z2 = round(v2[0]), round(v2[1]), v2[2]
        x3, y3, z3 = round(v3[0]), round(v3[1]), v3[2]

        if (is_front_facing(tv1,tv2,tv3, Vector3(0,0,0)) == False): continue

        ab = tv2 - tv1
        ac = tv3 - tv1

        n = Vector3.cross(ab, ac)

        i = calculate_lighting(n, Vector3(0,1,-5), 0.15)

        color = (round(255*i), round(50*i), round(50*i))
        framebuffer.draw_filled_triangle(x1, y1, z1, x2, y2, z2, x3, y3, z3, color)
    image = pygame.image.frombuffer(framebuffer.pixels, (width, height), "RGB")

    screen.blit(image, (0, 0))
    clock.tick()
    fps_text = font.render(f"FPS: {clock.get_fps():.1f}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))
    pygame.display.flip()
    

pygame.quit()