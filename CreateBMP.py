from PIL import Image
import math
import re


def CreateBMP(scrX, scrY, vertices):
    img = Image.new( 'RGB', (scrX+1, scrY+1), "black")
    pixels = img.load()
    color = (255,255,255)

    for vertice in vertices:
        pixels[scrX-((vertice[0]+1)*scrX/2), scrY-((vertice[1]+1)*scrY/2)] = color

    img.show()
