import math
def fillTriangle(verts, pixelArr, screenWidth, screenHeight):
    # for vert in verts:
    #     print (vert.x, vert.y)
    v1, v2, v3 = sorted(verts, key = lambda v: v.y)
    p1 = v1.copy()
    delta1 = zeroDiv((v2.x - v1.x), (v2.y - v1.y))
    p2 = v1.copy()
    delta2 = zeroDiv((v3.x - v1.x), (v3.y - v1.y))
    for y in (v2.y, v3.y):
        while p1.y < y:
            if p1.x > p2.x:
                p3 = p2.copy()
                x = p1.x
            else:
                p3 = p1.copy()
                x = p2.x
            while p3.x < x:
                # print((p3.x+1)*screenWidth/2, screenHeight-((p3.y+1)*screenHeight/2))
                # print (p3.x, p3.y)
                pixelArr[p3.x, screenHeight-p3.y] = (255, 255, 255)
                # try:
                # pixelArr[(p3.x+1)*screenWidth/2, screenHeight-((p3.y+1)*screenHeight/2)] = (255, 255, 255)
                # except:
                #     print()
                p3.x += 1
            p1.y += 1
            p1.x += delta1
            p2.y += 1
            p2.x += delta2
        delta1 = zeroDiv((v3.x - v2.x), (v3.y - v2.y))
        p1 = v2.copy()

def zeroDiv(a, b):
    return math.fabs(float(a)/b) if b != 0 else 0
