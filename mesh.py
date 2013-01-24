# -*- coding: utf-8 -*-
p = mdb.models['Model-1'].parts['blank']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#10000000 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=tan, constraint=FINER)
p = mdb.models['Model-1'].parts['blank']
pickedEdges = e.getSequenceFromMask(mask=('[#8000000 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=r1, constraint=FINER)
pickedEdges = e.getSequenceFromMask(mask=('[#800 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=r2, constraint=FINER)
pickedEdges = e.getSequenceFromMask(mask=('[#10000 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=r3, constraint=FINER)
pickedEdges = e.getSequenceFromMask(mask=('[#80000000 ]', ), )
p.seedEdgeByNumber(edges=pickedEdges, number=di, constraint=FINER)
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, 
    kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
    hourglassControl=ENHANCED, distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
c = p.cells
cells = c.getSequenceFromMask(mask=('[#f ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
p.generateMesh()

