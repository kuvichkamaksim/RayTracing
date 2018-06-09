import random
import tree
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
        color = gm.multiplyVector(gm.vectorSum(normal, gm.ones()), 0.5)
        px = gm.multiplyVector(color, 255)
        # px = buildShadow(lightPos, facet, normal, tree)

    return px

def findIntersections(point1, point2, tree):
    distance, facet = tree.findInter(point1, point2, tree)
    if distance == float('inf'): return None, None
else: return facet.vertices, facet.normal

def colorifyTest(cameraPos, pixel, lightPos, tree):
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def render(cameraPos, lightPos, imagePlane, tree):
    image = [[colorifyTest(cameraPos, pixel, lightPos, tree)
                for pixel in row]
                    for row in imagePlane]

    return image
