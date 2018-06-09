scrX = 800
scrY = 800
camera = (0.25, -1, 0.3)
direction = (0, 1, 0)
lightPos = (10, -10, 10)
distance = 2

def vectorMult (camera, coef):
    return tuple(map(lambda x: x*coef, camera))

def sum3d(first, second):
    x = first[0] + second[0]
    y = first[1] + second[1]
    z = first[2] + second[2]
    return (x, y, z)



def createCanv(camera, scrX, scrY, direction, distance):

    viewVector = vectorMult(direction, distance)
    imPos = sum3d(camera, viewVector)

    const = tuple(filter(lambda x: x != 0, viewVector))[0]
    # print (list(filter(lambda x: x != 0, viewVector)))
    const = viewVector.index(const)

    pixel = [0, 0, 0]
    pixel[const] = imPos[const]
    # print(list(i for i, c in enumerate(viewVector) if c == 0))
    [colCoord, rowCoord] = [i for i, c in enumerate(viewVector) if c == 0]

    colMax = scrX / 2
    rowMax = scrY / 2


    imagePlane = []
    row = rowMax

    for i in range(scrY):
        col = -colMax
        pixel[rowCoord] = row / rowMax + camera[rowCoord]
        imagePlane.append([])
        for j in range(scrX):
            pixel[colCoord] = col / colMax + camera[colCoord]
            imagePlane[i].append(tuple(pixel))
            col += 1

        row -= 1

    # print (imagePlane)
    return imagePlane

createCanv(camera, scrX, scrY, direction, distance)
