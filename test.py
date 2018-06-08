import math
from PIL import Image

img = Image.new( 'RGB', (801, 801), "black")
pixels = img.load()
color = (255,255,255)

class Vertice:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def show(self, color = None):
        pixels[self.x, 800-self.y] = color or (255, 255, 255)

    def copy(self):
        return Vertice(self.x, self.y, self.z)

def fillTriangle(verts):
    v1, v2, v3 = sorted(verts, key = lambda v: v.y)
    p1 = v1.copy()
    delta1 = zeroDiv((v2.x - v1.x), (v2.y - v1.y))
    # delta1 = float((v2.x-v1.x)/(v2.y-v1.y))
    p2 = v1.copy()
    delta2 = zeroDiv((v3.x - v1.x), (v3.y - v1.y))
    # delta2 = float((v3.x-v1.x)/(v3.y-v1.y))
    for y in (v2.y, v3.y):
        while p1.y < y:
            if p1.x > p2.x:
                p3 = p2.copy()
                x = p1.x
            else:
                p3 = p1.copy()
                x = p2.x
            while p3.x < x:
                p3.show()
                p3.x += 1
            p1.y += 1
            p1.x += delta1
            p2.y += 1
            p2.x += delta2
        delta1 = zeroDiv((v3.x - v2.x), (v3.y - v2.y))
        # delta1 = float((v3.x-v2.x)/(v3.y-v2.y))
        # p1 = v2.copy()

def zeroDiv(a, b):
    return math.fabs(float(a)/b) if b != 0 else 0

pix =[Vertice(30,40,0), Vertice(300, 300, 0), Vertice(200, 70, 0)]
fillTriangle(pix)
img.show()
