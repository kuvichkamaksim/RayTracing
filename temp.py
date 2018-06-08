import math
import re
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
someA = Vertice(-1,1,-1)
someB = Vertice(0,0,0)
someC = Vertice(1,1,1)

testArr = [someA, someB, someC]

img = Image.new( 'RGB', (scrX+1, scrY+1), "black")
pixels = img.load()
color = (255,255,255)

for vertice in testArr:
    pixels[((vertice.x+1)*scrX/2), scrY-((vertice.y+1)*scrY/2)] = color




def fillTriangle(verts, pixelArr, screenWidth, screenHeight):
    # for vert in verts:
    #     print (vert.x, vert.y)
    v1, v2, v3 = sorted(verts, key = lambda v: v.y)
    print (v1.x, v1.y,";", v2.x, v2.y, ";", v3.x, v3.y)
    p1 = v1.copy()
    delta1 = (zeroDiv((v2.x - v1.x), (v2.y - v1.y)))
    print (delta1)
    p2 = v2.copy()
    delta2 = (zeroDiv((v1.x - v3.x), (v1.y - v3.y)))
    print (delta2)
    i = 0
    for y in range(int((p1.y+1)*screenHeight/2), int((v3.y+1)*screenHeight/2)):
        # print(int((p1.x+1)*screenWidth/2), int((p1.x+1 + i*delta1)*screenWidth/2))
        i +=1
        pixelArr[int((p1.x+1)*screenWidth/2 + i*delta2), screenHeight-int(y)] = (255, 255, 255)
        for x in range(int((p1.x+1)*screenWidth/2 + i*delta1), int((p1.x+1 )*screenWidth/2+ i*delta2)):
            print(int(x), int(y))
            try:
                pixelArr[int(x), screenHeight-int(y)] = (255, 255, 255)

            except :
                raise

    # print (delta2)
    # for y in (v2.y, v3.y):
    #     while p1.y < y:
    #         print (y)
    #         if p1.x > p2.x:
    #             p3 = p2.copy()
    #             x = p1.x
    #         else:
    #             p3 = p1.copy()
    #             x = p2.x
    #         while p3.x < x:
    #             # print((p3.x+1)*screenWidth/2, screenHeight-((p3.y+1)*screenHeight/2))
    #             try:
    #                 pixelArr[p3.x, screenHeight-p3.y] = (255, 255, 255)
    #             except:
    #                 print("ERr")
    #             # try:
    #                 # pixelArr[(p3.x+1)*screenWidth/2, screenHeight-((p3.y+1)*screenHeight/2)] = (255, 255, 255)
    #             # except:
    #             #     print()
    #             p3.x += 1
    #         if p1.y+1 <= screenHeight:
    #             p1.y += 1
    #         p1.x += delta1
    #         if p2.y+1 <= screenHeight:
    #             p2.y += 1
    #         p2.x += delta2
    #     delta1 = zeroDiv((v3.x - v2.x), (v3.y - v2.y))
    #     p1 = v2.copy()

def zeroDiv(a, b):
    return (float(a)/b) if b != 0 else 0

fillTriangle(testArr, pixels, scrX+1, scrY+1)



img.show()
