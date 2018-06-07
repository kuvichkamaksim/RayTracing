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
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def show(self, color = None):
        pixels[self.x, scrY-self.y] = color or (255, 255, 255)

    def copy(self):
        return Vertice(self.x, self.y)

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
        vertices.append(Vertice(x,y,z))
        leng = math.sqrt(x**2 + y**2 + z**2)
        if leng > maxLeng:
            maxLeng = leng

    if indent == 'f':
        if len(re.split('\s+', line)) == 5:
            f, v1, v2, v3, v4 = re.split('\s+', line)
        else:
            f, v1, v2, v3 = re.split('\s+', line)


for vertice in vertices:
    vertice.x = vertice.x/maxLeng + 1
    vertice.y = vertice.y/maxLeng + 1
    pixels[int(vertice.x*scrX/2), int(scrY-(vertice.y*scrY/2))] = color

img.show()
