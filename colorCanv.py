import random
import tree as tr
import matan

def colorCanv(cameraPos, lightPos, imagePlane, tree):
    image = [[colorify(cameraPos, pixel, lightPos, tree)
                for pixel in row]
                    for row in imagePlane]

    return image

def colorify(cameraPos, pixel, lightPos, tree):
    px = (255, 255, 255)
    light = 200

    facet, normal = findIntersections(cameraPos, pixel, tree)

    # print( facet, normal )

    if facet:
        color = tuple(map(lambda x: (x+1)/2, normal))
        px = tuple(map(lambda x: int(x*255), color))
        # px = buildShadow(lightPos, facet, normal, tree)

    return px

def findIntersections(point1, point2, tree):
    distance, facet = tr.findIntersection(point1, point2, tree)
    # print (distance, facet)
    if distance == float('inf'): return None, None
    else: return facet.vertices, facet.normal

def colorifyTest(cameraPos, pixel, lightPos, tree):
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def render(cameraPos, lightPos, imagePlane, tree):
    image = [[colorifyTest(cameraPos, pixel, lightPos, tree)
                for pixel in row]
                    for row in imagePlane]

    return image
