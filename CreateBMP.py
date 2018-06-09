from PIL import Image
from FillTriangles import fillTriangle
import math
import re

def CreateBMP(imageMatrix, srcX, srcY):
    img = Image.new( 'RGB', (srcX+1, srcY+1), "black")
    pixels = img.load()

    # color = (255,255,255)
    # print (imageMatrix)
    for y in range(srcY):
        for x in range(srcX):
            # print ( type(imageMatrix[x][y]) )
            # try:
            pixels[x, y] = imageMatrix[y][x]
            # except:
            #     pass
    # for facet in facets:
    #     fillTriangle(facet.vertices, pixels, scrX, scrY, facet.normal)

    img.show()
