from PIL import Image
import math
import re
import matan

class Facet:
    def __init__(self):
        self.vertices = []
        self.normal = []
        self.center = []

    def show(self):
        for vert in self.vertices:
            print (vert[0], vert[1], vert[2])
        for norm in self.normal:
            print (norm)

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
            vertices.append( [x, y, z] )
            leng = math.sqrt(x**2 + y**2 + z**2)
            if leng > maxLeng:
                maxLeng = leng

        if indent == 'vn':
            vn, x, y, z = re.split('\s+', line)
            x = float(x)
            y = float(y)
            z = float(z)
            verticesNorm.append( [x, y, z] )

        if indent == 'f':
            tempArr = line.split(' ')
            tempArr.pop(0)
            resObj = Facet()
            for vert in tempArr:
                tempEl = list(map(lambda el: int(el) if len(el) else 0 , vert.split('/')))

                if (len(tempEl) == 3):
                    resObj.vertices.append(vertices[tempEl[0]-1])
                    resObj.normal.append(verticesNorm[tempEl[2]-1])
                else:
                    resObj.vertices.append(vertices[tempEl[0]-1])
                    try:
                        resObj.normal.append(verticesNorm[tempEl[1]-1])
                    except:
                        pass

            # print (resObj.vertices)
            # data = map(lambda dataRow: map(lambda someString: int(someString), dataRow), dataArr)
            resObj.center = matan.facetCenter(resObj.vertices)
            a = b = c = 0
            for norm in resObj.normal:
                a += norm[0]
                b += norm[1]
                c += norm[2]
            resObj.normal = matan.normalize([a, b, c])
            # print (resObj.normal)

            facets.append(resObj)

    for vertice in vertices:
        vertice[0] = vertice[0]/maxLeng
        vertice[1] = vertice[1]/maxLeng
        vertice[2] = vertice[2]/maxLeng

    # for facet in facets:
    #     facet.show()

    return vertices, facets, verticesNorm
