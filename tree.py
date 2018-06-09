from matan import facetCenter, facetDist, rayBoxIntersection

class Node:
    def __init__(self):
        self.min = []
        self.max = []
        self.current = []
        self.left = None
        self.right = None

def findMedian(array, axle):
    a = sorted(array, key = lambda x: x.center[axle])
    middleEl = a[ len(array)//2 ]
    return a, array.index(middleEl)

def makeBoundBox(facets):
    sortedFacets = list(map(lambda facet:
    sorted(facet.vertices, key = lambda vertice: vertice[0]), facets))
    xMin = min(sortedFacets, key = lambda facet: facet[0][0])[0][0]
    xMax = max(sortedFacets, key = lambda facet: facet[2][0])[2][0]

    sortedFacets = list(map(lambda facet:
    sorted(facet.vertices, key = lambda vertice: vertice[1]), facets))
    yMin = min(sortedFacets, key = lambda facet: facet[0][1])[0][1]
    yMax = max(sortedFacets, key = lambda facet: facet[2][1])[2][1]

    sortedFacets = list(map(lambda facet:
    sorted(facet.vertices, key = lambda vertice: vertice[2]), facets))
    zMin = min(sortedFacets, key = lambda facet: facet[0][2])[0][2]
    zMax = max(sortedFacets, key = lambda facet: facet[2][2])[2][2]
    # print (xMin, xMax, yMin, yMax, zMin, zMax)
    return [xMin, yMin, zMin], [xMax, yMax, zMax]

def buildTree(facets, level = 0):
    if len(facets) <= 0:
        return None

    axis = level % 3
    sortedFacets, midEl = findMedian(facets, axis)
    left = sortedFacets[0:midEl]
    right = sortedFacets[midEl+1:]

    min, max = makeBoundBox(facets)

    currNode = Node()
    currNode.current = midEl
    currNode.min = min
    currNode.max = max

    if len(facets) == 1:
        return currNode

    currNode.left = buildTree(left, level+1)
    currNode.right = buildTree(right, level+1)

    return currNode


def findInter(camPos, facetCenter, tree):
    dist = rayBoxIntersection(camPos, facetCenter, [tree.min, tree.max])
    if dist == float('inf'):
        return dist, None

    if tree.left == None and tree.right == None:
        dist = facetDist(camPos, facetCenter, tree.current.vertices)
        return dist, tree.current.vertices

    if tree.left != None:
        leftDist = rayBoxIntersection(camPos, facetCenter, [tree.left.min, tree.left.max])

    if tree.right != None:
        rightDist = rayBoxIntersection(camPos, facetCenter, [tree.right.min, tree.right.max])

    if leftDist > rightDist:
        closeDist = rightDist
        farDist = leftDist
    else:
        closeDist = leftDist
        farDist = rightDist

    if farDist != float('inf'):
        if farDist == leftDist:
            direction = tree.left
        else:
            direction = tree.right
        farDist, farVert = findInter(camPos, facetCenter, direction)

    if closeDist != float('inf'):
        if closeDist == leftDist:
            direction = tree.left
        else:
            direction = tree.right
        closeDist, closeVert = findInter(camPos, facetCenter, direction)

    currNodeDist = facetDist(camPos, facetCenter, tree.current.vertices)

    return min(
        [[currNodeDist, tree.current], [closeDist, closeVert], [farDist, farVert]],
        key = lambda elem: elem[0]
    )
