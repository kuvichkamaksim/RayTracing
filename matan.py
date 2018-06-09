import math

def normalize(v):
    x, y, z = v
    l = math.sqrt(x**2 + y**2 + z**2)
    return [x/l, y/l, z/l]

def facetCenter(facet):
    x1, y1, z1 = facet[0]
    x2, y2, z2 = facet[1]
    x3, y3, z3 = facet[2]
    return [ (x1+x2+x3)/3, (y1+y2+y3)/3, (z1+z2+z3)/3 ]

def makeVector(point1, point2):
    x = point2[0] - point1[0]
    y = point2[1] - point1[1]
    z = point2[2] - point1[2]
    return [x, y, z]

def cross(v1, v2):
    x = v1[1]*v2[2] - v2[1]*v1[2]
    y = v2[0]*v1[2] - v1[0]*v2[2]
    z = v1[0]*v2[1] - v2[0]*v1[1]
    return [x, y, z]

def scalarVectorMult(v1, v2):
    x = v1[0] * v2[0]
    y = v1[1] * v2[1]
    z = v1[2] * v2[2]
    return x + y + z

def facetIntersection(orig, dir, facet): #orig-ray start, dir-ray direction
    coef = 1e-8

    v0, v1, v2 = facet
    e1 = makeVector(v0, v1)
    e2 = makeVector(v0, v2)

    pvec = cross(dir, e2)
    det = scalarVectorMult(e1, pvec)

    if det < coef and det > -coef:
        return float('inf')

    tvec = makeVector(v0, orig)
    u = scalarVectorMult(tvec, pvec) / det
    if u < 0 or u > 1:
        return float('inf')

    qvec = cross(tvec, e1)
    v = scalarVectorMult(dir, qvec) / det
    if v < 0 or u+v > 1:
        return float('inf')

    return scalarVectorMult(e2, qvec) / det #distance

def cos(point1, point2, vector):
    x1, y1, z1 = vector
    x2, y2, z2 = makeVector(point1, point2)

    mod1 = math.sqrt(x1**2 + y1**2 + z1**2)
    mod2 = math.sqrt(x2**2 + y2**2 + z2**2)

    return abs(x1*x2 + y1*y2 + z1*z2) / (mod1*mod2)

def rayBoxIntersection(point1, point2, box):
    x0, y0, z0 = box[0]
    x1, y1, z1 = box[1]

    m, n, p = normalize(makeVector(point1, point2))
    x, y, z = point1

    Tnear, Tfar = -float('inf'), float('inf')
    if m == 0:
        if x > x1 or x < x0:
            return float('inf')
    else:
        Tnear = (x0 - x) / m
        Tfar = (x1 - x) / m
        if Tnear > Tfar: Tfar, Tnear = Tnear, Tfar

    if n == 0:
        if y > y1 or y < y0:
            return float('inf')
    else:
        T1y = (y0 - y) / n
        T2y = (y1 - y) / n

        if T1y > T2y: T2y, T1y = T1y, T2y

        if T1y > Tnear: Tnear = T1y
        if T2y < Tfar: Tfar = T2y

    if Tnear > Tfar or Tfar < 0:
        return float('inf')

    if p == 0:
        if z > z1 or z < z0:
            return float('inf')
    else:
        T1z = (z0 - z) / p
        T2z = (z1 - z) / p

        if T1z > T2z: T2z, T1z = T1z, T2z

        if T1z > Tnear: Tnear = T1z
        if T2z < Tfar: Tfar = T2z

    if Tnear > Tfar or Tfar == 0:
        return float('inf')

    return Tnear
