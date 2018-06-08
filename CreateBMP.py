from PIL import Image
from FillTriangles import fillTriangle
import math
import re

def CreateBMP(scrX, scrY, vertices, facets):
    img = Image.new( 'RGB', (scrX+1, scrY+1), "black")
    pixels = img.load()
    color = (255,255,255)

    for vertice in vertices:
        pixels[((vertice[0]+1)*scrX/2), scrY-((vertice[1]+1)*scrY/2)] = color

    # for facet in facets:
    #     fillTriangle(facet.vertices, pixels, scrX, scrY, facet.normal)

    img.show()
