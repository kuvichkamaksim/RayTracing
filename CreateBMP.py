from PIL import Image
import math
import re
from FillTriangles import fillTriangle

def CreateBMP(scrX, scrY, vertices, facets):
    img = Image.new( 'RGB', (scrX+1, scrY+1), "black")
    pixels = img.load()
    color = (255,255,255)

    for vertice in vertices:
        # pixels[(vertice.x+1)*scrX/2, scrY-((vertice.y+1)*scrY/2)] = color
        # print (vertice.x, vertice.y)
        pixels[vertice.x, scrY-vertice.y] = color

    for facet in facets:
        if len(facet.vertices) == 3:
            fillTriangle(facet.vertices, pixels, scrX, scrY)
        elif len(facet.vertices) == 4:
            fillTriangle(facet.vertices[0:3], pixels, scrX, scrY)
            fillTriangle(facet.vertices[1:], pixels, scrX, scrY)
        else:
            print("idi nahui eblan")

    img.show()
