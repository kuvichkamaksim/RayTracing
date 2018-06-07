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

for vertice in vertices:
    for i in range(2):
        vertice[i] = vertice[i]/maxLeng + 1
    pixels[scrX-(vertice[0]*scrX/2), scrY-(vertice[1]*scrY/2)] = color

img.show()
