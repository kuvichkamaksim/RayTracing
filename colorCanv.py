import random
import tree as tr
import matan

def colorCanv(cameraPos, lightPos, imagePlane, tree):
    image = [[colorify(cameraPos, pixel, lightPos, tree)
                for pixel in row]
                    for row in imagePlane]

    return image

def colorify(cameraPos, pixel, lightPos, tree):
    px = 255
    light = 200

    facet, normal = findIntersections(cameraPos, pixel, tree)

    if facet:
        color = tuple(map(lambda x: (x+1)/2, normal))
        # color = matan.multiplyVector(matan.vectorSum(normal, matan.ones()), 0.5)
        px = tuple(map(lambda x: x*255, color))
        # px = matan.multiplyVector(color, 255)
        # px = buildShadow(lightPos, facet, normal, tree)

    return px

def findIntersections(point1, point2, tree):
    distance, facet = tr.findInter(point1, point2, tree)
    if distance == float('inf'): return None, None
    else: return facet.vertices, facet.normal

def colorifyTest(cameraPos, pixel, lightPos, tree):
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def render(cameraPos, lightPos, imagePlane, tree):
    image = [[colorifyTest(cameraPos, pixel, lightPos, tree)
                for pixel in row]
                    for row in imagePlane]

    return image
