from CreateBMP import CreateBMP
from ReadingObj import ReadingObj

scrX = 800
scrY = 800

f = open("./data/Patricio.obj", 'r')

vertices, facets, verticesNorm = ReadingObj(f)
CreateBMP = CreateBMP(scrX, scrY, vertices)
