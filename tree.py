from matan import facetCenter, facetDist, rayBoxIntersection

# class Node:
#     def __init__(self):
#         self.min = []
#         self.max = []
#         self.current = []
#         self.left = None
#         self.right = None

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

    return [xMin, yMin, zMin], [xMax, yMax, zMax]

def boundingBox(facets):
    xSorted = list(map(lambda facet:
        sorted(facet.vertices, key = lambda point: point[0]), facets))
    ySorted = list(map(lambda facet:
        sorted(facet.vertices, key = lambda point: point[1]), facets))
    zSorted = list(map(lambda facet:
        sorted(facet.vertices, key = lambda point: point[2]), facets))

    xmin = min(xSorted, key = lambda f: f[0][0])[0][0]
    ymin = min(ySorted, key = lambda f: f[0][1])[0][1]
    zmin = min(zSorted, key = lambda f: f[0][2])[0][2]
    xmax = max(xSorted, key = lambda f: f[2][0])[2][0]
    ymax = max(ySorted, key = lambda f: f[2][1])[2][1]
    zmax = max(zSorted, key = lambda f: f[2][2])[2][2]

    return (xmin, ymin, zmin), (xmax, ymax, zmax)

# def buildTree(facets, level = 0):
#     if len(facets) <= 0:
#         return None
#
#     axis = level % 3
#     sortedFacets, midEl = findMedian(facets, axis)
#     left = sortedFacets[0:midEl]
#     right = sortedFacets[midEl+1:]
#
#     min, max = boundingBox(facets)
#
#     currNode = Node()
#     currNode.current = facets[midEl]
#     currNode.min = min
#     currNode.max = max
#
#     if len(facets) == 1:
#         return currNode
#
#     currNode.left = buildTree(left, level+1)
#     currNode.right = buildTree(right, level+1)
#
#     return currNode

def buildTree(facets, depth = 0):
    n = len(facets)

    if n <= 0:
        return None

    axis = depth % 3
    ordered = sorted(facets, key = lambda f: f.vertices[axis])
    left = ordered[:int(n / 2)]
    right = ordered[int(n / 2) + 1:]
    splitPoint = ordered[int(n / 2)]
    minPoint, maxPoint = boundingBox(facets)

    node = {
        'min': minPoint,
        'max': maxPoint,
        'split': splitPoint
    }

    if n == 1:
        return node

    node['left'] = buildTree(left, depth + 1)
    node['right'] = buildTree(right, depth + 1)

    return node

# def findInter(camPos, facetCenter, tree):
#     dist = rayBoxIntersection(camPos, facetCenter, [tree.min, tree.max])
#     if dist == float('inf'):
#         return dist, None
#
#     if not ('left' in tree.__dict__ and 'right' in tree.__dict__):
#         dist = facetDist(camPos, facetCenter, tree.current.vertices)
#         return dist, tree.current.vertices
#
#     if tree.left != None:
#         leftDist = rayBoxIntersection(camPos, facetCenter, [tree.left.min, tree.left.max])
#
#     if tree.right != None:
#         rightDist = rayBoxIntersection(camPos, facetCenter, [tree.right.min, tree.right.max])
#
#     leftDist, rightDist = float('inf'), float('inf')
#
#     if leftDist > rightDist:
#         closeDist = rightDist
#         farDist = leftDist
#     else:
#         closeDist = leftDist
#         farDist = rightDist
#
#     closeVert, farVert = (), ()
#
#     if closeDist != float('inf'):
#         if closeDist == leftDist:
#             direction = tree.left
#         else:
#             direction = tree.right
#         closeDist, closeVert = findInter(camPos, facetCenter, direction)
#
#     if farDist != float('inf'):
#         if farDist == leftDist:
#             direction = tree.left
#         else:
#             direction = tree.right
#         farDist, farVert = findInter(camPos, facetCenter, direction)
#
#     currNodeDist = facetDist(camPos, facetCenter, tree.current.vertices)
#
#     return min(
#         [[currNodeDist, tree.current], [closeDist, closeVert], [farDist, farVert]],
#         key = lambda elem: elem[0]
#     )

def findIntersection(point1, point2, tree):
    intersect = rayBoxIntersection(
        point1, point2, (tree['min'], tree['max'])
    )

    if intersect == float('inf'): return float('inf'), None

    if not 'left' in tree and not 'right' in tree:
        facet = tree['split']
        distance = facetDist(point1, point2, facet.vertices)
        return distance, facet

    triangle = tree['split'].vertices
    distance = facetDist(point1, point2, triangle)

    intersectLeft = float('inf')
    intersectRight = float('inf')

    if tree['left'] != None:
        intersectLeft = rayBoxIntersection(
            point1, point2, (tree['left']['min'], tree['left']['max'])
        )

    if tree['right'] != None:
        intersectRight = rayBoxIntersection(
            point1, point2, (tree['right']['min'], tree['right']['max'])
        )

    closest = {
        'dist': float('inf'),
        'dir': None
    }

    further = {
        'dist': float('inf'),
        'dir': None
    }

    if intersectLeft > intersectRight:
        closest['dist'] = intersectRight
        further['dist'] = intersectLeft
        closest['dir'] = 'right'
        further['dir'] = 'left'
    else:
        closest['dist'] = intersectLeft
        further['dist'] = intersectRight
        closest['dir'] = 'left'
        further['dir'] = 'right'

    distC, triangleC = float('inf'), ()
    distF, triangleF = float('inf'), ()

    if closest['dist'] != float('inf'):
        distC, triangleC = findIntersection(point1, point2, tree[closest['dir']])

    if further['dist'] != float('inf'):
        distF, triangleF = findIntersection(point1, point2, tree[further['dir']])

    distances = [
        (distance, tree['split']),
        (distC, triangleC),
        (distF, triangleF)
    ]

    return min(distances, key = lambda x: x[0])
