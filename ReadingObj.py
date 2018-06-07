from PIL import Image
import math
import re

scrX = 800
scrY = 800

img = Image.new( 'RGB', (scrX+1, scrY+1), "black")
pixels = img.load()
color = (255,255,255)

f = open("./data/Patricio.obj", 'r')
# f = open("./data/legoman.obj", 'r')
lines = f.read()

class Vertice(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self, color = None):
        pixels[self.x, scrY-self.y] = color or (255, 255, 255)

    def copy(self):
        return Vertice(self.x, self.y)

def fillTriangle(coords):
    v1, v2, v3 = sorted(coords, key = lambda v: v.y)
    p1 = v1.copy()
    delta1 = float(b.x - a.x)/(b.y - a.y)
    p2 = v2.copy()
    delta2 = float(c.x - b.x)/(c.y - b.y)
    for y in (b.y, c.y):
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
        delta1 = float(c.x - b.x)/(c.y - b.y)


maxLeng = 0.0
vertices = []
facets = []
verticesNorm = []
for line in lines.split('\n'):

    indent = line.split(' ')[0]
    if indent == 'v':
        v, x, y, z = re.split('\s+', line)
        x = float(x)
        y = float(y)
        z = float(z)
        vertices.append( [x,y,z] )
        leng = math.sqrt(x**2 + y**2 + z**2)
        if leng > maxLeng:
            maxLeng = leng

    if indent == 'f':
        if len(re.split('\s+', line)) == 5:
            f, v1, v2, v3, v4 = re.split('\s+', line)
        else:
            f, v1, v2, v3 = re.split('\s+', line)


for vertice in vertices:
    for i in range(2):
        vertice[i] = vertice[i]/maxLeng + 1
    pixels[int(vertice[0]*scrX/2), int(scrY-(vertice[1]*scrY/2))] = color

img.show()
