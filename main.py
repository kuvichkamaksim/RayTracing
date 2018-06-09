from CreateBMP import CreateBMP
from ReadingObj import ReadingObj
from CreateCanv import createCanv
import colorCanv
import tree

scrX = 100
scrY = 100
camera = (0.25, -1, 0.3)
direction = (0, 1, 0)
lightPos = (10, -10, 10)
distance = 0.5

f = open("./data/cow.obj", 'r')

vertices, facets, verticesNorm = ReadingObj(f)
imageMatrixCoord = createCanv(camera, scrX, scrY, direction, distance)
KDtree = tree.buildTree(facets)
resultMatrix = colorCanv.colorCanv(camera, lightPos, imageMatrixCoord, KDtree)
# print (resultMatrix)
CreateBMP = CreateBMP(resultMatrix, scrX, scrY)

KDtree = tree.buildTree(facets)
