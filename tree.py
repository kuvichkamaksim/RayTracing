from matan import facetCenter, facetIntersection, rayBoxIntersection

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
