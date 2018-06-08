import math
import re
import random
from PIL import Image

def fillTriangle(verts, pixelArr, screenWidth, screenHeight, normals):
    col = random.randint(0, 255)
    if (len(verts) != 3):
        fillTriangle(verts[0:3], pixelArr, screenWidth, screenHeight, normals[0:3])
        fillTriangle(verts[1:4], pixelArr, screenWidth, screenHeight, normals[1:4])
    else:
        # for vert in verts:
        #     print (vert.x, vert.y)
        # print (screenHeight)
        v1, v2, v3 = sorted(verts, key = lambda v: v.y)
        # print (v1.x, v1.y,";", v2.x, v2.y, ";", v3.x, v3.y)
        p1 = v1.copy()
        delta1 = (zeroDiv((v2.x - v1.x), (v2.y - v1.y)))
        delta2 = (zeroDiv((v1.x - v3.x), (v1.y - v3.y)))
        # print (delta1, delta2)
        p2 = v2.copy()
        p3 = v3.copy()
        delta3 = (zeroDiv((v2.x - v3.x), (v3.y - v2.y)))
        delta4 = (zeroDiv((v1.x - v3.x), (v3.y - v1.y)))
        # print (delta3, delta4)

        i = 0
        for y in range(int((p1.y+1)*screenHeight/2), int((v2.y+1)*screenHeight/2)):
            # print(int((p1.x+1)*screenWidth/2), int((p1.x+1 + i*delta1)*screenWidth/2))
            i +=1
            # pixelArr[int((p1.x+1)*screenWidth/2 + i*delta2), screenHeight-int(y)] = (255, 255, 255)
            for x in range(int((p1.x+1)*screenWidth/2 + i*delta1), int((p1.x+1 )*screenWidth/2+ i*delta2)):
                try:
                    pixelArr[x, screenHeight-y] = (col, col, col)
                except :
                    # print(int(x), screenHeight-y)
                    # print('eeeer1')
                    pass
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
                    # print(v1.x, v1.y, v2.x, v2.y, v3.x, v3.y)
                    # print(int(x), screenHeight-y)
                    # print("eeeeer2")
                    pass


def zeroDiv(a, b):
    return (float(a)/b) if b != 0 else 0
