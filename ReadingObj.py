from PIL import Image
import math
import re

class Facet:
    def __init__(self):
        self.vertices = []
        self.texture = []
        self.normal = []

def ReadingObj(f):
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

        if indent == 'vn':
            verticesNorm.append(line.strip('\n').split(' '))

        if indent == 'f':
            tempArr = line.strip().split(' ')
            tempArr.pop(0)
            resObj = Facet()
            for vert in tempArr:
                tempEl = list(map(lambda el: int(el) if len(el) else 0 , vert.split('/')))
                resObj.vertices.append(vertices[tempEl[0]-1])
                resObj.texture.append(tempEl[1])
                resObj.normal.append(verticesNorm[tempEl[2]-1])
            # print (resObj.vertices)
            # data = map(lambda dataRow: map(lambda someString: int(someString), dataRow), dataArr)
            resObj.vertices
            facets.append(resObj)
    for vertice in vertices:
        for i in range(2):
            vertice[i] = vertice[i]/maxLeng
    return vertices, facets, verticesNorm
    # pixels[scrX-(vertice[0]*scrX/2), scrY-(vertice[1]*scrY/2)] = color
