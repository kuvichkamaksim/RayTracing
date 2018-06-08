import math
import re
import random
from PIL import Image


class Vertice(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def show(self, color = None):
        pixels[self.x, scrY-self.y] = color or (255, 255, 255)

    def copy(self):
        return Vertice(self.x, self.y, self.z)

    def copyPlus1(self):
        return Vertice(self.x+1, self.y+1, self.z+1)



scrX = 800
scrY = 800
someA = Vertice(0.3,-1,-1)
someB = Vertice(0,0,0)
someC = Vertice(1,1,1)

testArr = [someA, someB, someC]

img = Image.new( 'RGB', (scrX+1, scrY+1), "black")
pixels = img.load()
color = (255,255,255)

for vertice in testArr:
    pixels[((vertice.x+1)*scrX/2), scrY-((vertice.y+1)*scrY/2)] = color




def fillTriangle(verts, pixelArr, screenWidth, screenHeight):
    col = random.randint(0, 255)
    # for vert in verts:
    #     print (vert.x, vert.y)
    # print (screenHeight)
    v1, v2, v3 = sorted(verts, key = lambda v: v.y)
    print (v1.x, v1.y,";", v2.x, v2.y, ";", v3.x, v3.y)
    p1 = v1.copy()
    delta1 = (zeroDiv((v2.x - v1.x), (v2.y - v1.y)))
    delta2 = (zeroDiv((v1.x - v3.x), (v1.y - v3.y)))
    print (delta1, delta2)
    p2 = v2.copy()
    p3 = v3.copy()
    delta3 = (zeroDiv((v2.x - v3.x), (v3.y - v2.y)))
    delta4 = (zeroDiv((v1.x - v3.x), (v3.y - v1.y)))
    print (delta3, delta4)

    i = 0
    for y in range(int((p1.y+1)*screenHeight/2), int((v2.y+1)*screenHeight/2)):
        # print(int((p1.x+1)*screenWidth/2), int((p1.x+1 + i*delta1)*screenWidth/2))
        i +=1
        # pixelArr[int((p1.x+1)*screenWidth/2 + i*delta2), screenHeight-int(y)] = (255, 255, 255)
        for x in range(int((p1.x+1)*screenWidth/2 + i*delta1), int((p1.x+1 )*screenWidth/2+ i*delta2)):
            try:
                pixelArr[x, screenHeight-y] = (col, col, col)
            except :
                # print(int(x), y, screenHeight, screenHeight-y)
                print('eeeer')
    i = 0
    for y in reversed(range(int((v2.y+1)*screenHeight/2), int((v3.y+1)*screenHeight/2))):
        # print(int((p1.x+1)*screenWidth/2), int((p1.x+1 + i*delta1)*screenWidth/2))
        # print("cont")
        i +=1
        # for x in range(screenWidth):
        #     pixelArr[x, screenHeight-y] = (255, 255, 255)
        # pixelArr[int((v3.x+1)*screenWidth/2 + i*delta3), int((p2.x+1 )*screenWidth/2+ i*delta4)] = (255, 255, 255)
        for x in range(int((v3.x+1)*screenWidth/2 + i*delta3), int((p3.x+1 )*screenWidth/2+ i*delta4)):
            # print(int(x), int(y))
            try:
                pixelArr[x, screenHeight-y] = (col, col, col)
            except :
                print(int(x), screenHeight-y)
                print("eeeeer")


def zeroDiv(a, b):
    return (float(a)/b) if b != 0 else 0

fillTriangle(testArr, pixels, scrX, scrY)



img.show()
