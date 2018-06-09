from CreateBMP import CreateBMP
from ReadingObj import ReadingObj
from CreateCanv import createCanv
import colorCanv
import tree

scrX = 800
scrY = 800
camera = (0.25, -1, 0.3)
direction = (0, 1, 0)
lightPos = (10, -10, 10)
distance = 2

f = open("./data/cow.obj", 'r')

vertices, facets, verticesNorm = ReadingObj(f)
imageMatrixCoord = createCanv(camera, scrX, scrY, direction, distance)
KDtree = tree.buildTree(facets)
resultMatrix = colorCanv.render(camera, lightPos, imageMatrixCoord, KDtree)
CreateBMP = CreateBMP(resultMatrix, scrX, scrY)

KDtree = tree.buildTree(facets)
