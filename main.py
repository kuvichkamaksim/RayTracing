from CreateBMP import CreateBMP
from ReadingObj import ReadingObj
import tree

scrX = 800
scrY = 800
camera = (0.25, -1, 0.3)
direction = (0, 1, 0)
lightPos = (10, -10, 10)

f = open("./data/cow.obj", 'r')

vertices, facets, verticesNorm = ReadingObj(f)
# CreateBMP = CreateBMP(scrX, scrY, vertices, facets)

KDtree = tree.buildTree(facets)
