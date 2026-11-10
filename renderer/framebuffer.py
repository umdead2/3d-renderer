import math

class Framebuffer:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.pixels = bytearray(width * height * 3)
        self.depth_buffer = [math.inf] * (width * height)

    def clear_depth(self):
        self.depth_buffer[:] = [math.inf] * (self.width * self.height)

    def clear(self, color):
        self.pixels[:] = [color[0], color[1], color[2]] * (self.width * self.height)
        self.clear_depth()


    def set_pixel(self, x, y, color):
        index = (y * self.width + x) * 3
        if x < 0 or x >= self.width: return
        if y < 0 or y >= self.height: return
        self.pixels[index] = color[0]
        self.pixels[index + 1] = color[1]
        self.pixels[index + 2] = color[2]

    def draw_line(self, x1, y1, x2, y2, color):
        dx = abs(x2-x1)
        dy = -abs(y2-y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        x = x1
        y = y1
        err = dx + dy
        while True:
            self.set_pixel(x, y, color)
            if x == x2 and y == y2: break
            e2 = err * 2
            if e2 >= dy:
                x += sx
                err += dy
            if e2 <= dx:
                y += sy
                err += dx

    def draw_triangle(self, x1, y1, x2, y2, x3, y3, color):
        self.draw_line(x1,y1,x2,y2,color)
        self.draw_line(x2,y2,x3,y3,color)
        self.draw_line(x3,y3,x1,y1,color)

    def draw_filled_triangle(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, color):
        smallestx = min(x1, x2, x3)
        biggestx = max(x1, x2, x3)
        smallesty = min(y1, y2, y3)
        biggesty = max(y1, y2, y3)

        for x in range(biggestx - smallestx + 1):
            for y in range(biggesty - smallesty + 1):
                pixel_x = smallestx + x
                pixel_y = smallesty + y

                eab = (x2 - x1) * (pixel_y - y1) - (y2 - y1) * (pixel_x - x1)
                ebc = (x3 - x2) * (pixel_y - y2) - (y3 - y2) * (pixel_x - x2)
                eca = (x1 - x3) * (pixel_y - y3) - (y1 - y3) * (pixel_x - x3)

                inside = ((eab >= 0 and ebc >= 0 and eca >= 0) or (eab <= 0 and ebc <= 0 and eca <= 0))

                if not inside: continue

                area = eab + ebc + eca

                if area == 0: return

                la = ebc / area
                lb = eca / area
                lc = eab / area

                q = la / z1 + lb / z2 + lc / z3
                z_pixel = 1 / q

                index = pixel_y * self.width + pixel_x

                if z_pixel < self.depth_buffer[index]:
                    self.depth_buffer[index] = z_pixel
                    self.set_pixel(pixel_x, pixel_y, color)
