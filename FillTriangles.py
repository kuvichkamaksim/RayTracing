def fillTriangle(verts):
    v1, v2, v3 = sorted(verts, key = lambda v: v.y)
    p1 = v1.copy()
    delta1 = float(v2.x - v1.x)/(v2.y - v1.y)
    p2 = v2.copy()
    delta2 = float(v3.x - v2.x)/(v3.y - v2.y)
    for y in (v2.y, v3.y):
        while p1.y < y:
            if p1.x > p2.x:
                p3 = p2.copy()
                x = p1.x
            else:
                p3 = p1.copy()
                x = p2.x
            while p3.x < x:
                p3.show()
                p3.x += 1
            p1.y += 1
            p1.x += delta1
            p2.y += 1
            p2.x += delta2
        delta1 = float(v3.x - v2.x)/(v3.y - v2.y)
        p1 = v2.copy
