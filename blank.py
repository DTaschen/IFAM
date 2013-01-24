# -*- coding: utf-8 -*-
#----------------------------------------------------------------------
#Blech
#----------------------------------------------------------------------
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s.FixedConstraint(entity=g[2])
s.rectangle(point1=(0.0, 0.0), point2=(r_B, dicke))
p = mdb.models['Model-1'].Part(name='blank', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p.BaseSolidRevolve(sketch=s, angle=angle2, flipRevolveDirection=OFF)
s.unsetPrimaryObject()
f1, e1, d2 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f1[0], sketchUpEdge=e1[2], 
    sketchPlaneSide=SIDE1, origin=(21.220659, 1.0, 21.220659))
#----------------------------------------------------------------------
#Partition
#----------------------------------------------------------------------
p = mdb.models['Model-1'].parts['blank']
f1, e, d2 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f1[0], sketchUpEdge=e[2], 
    sketchPlaneSide=SIDE1, origin=(0.0, 1.0, 0.0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=141.43, gridSpacing=3.53, transform=t)
g, v1, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.0, p1), point2=(p1, 0.0), 
    direction=CLOCKWISE)
s.Line(point1=(0.0, p1), point2=(0.0, 0.0))
s.VerticalConstraint(entity=g[6], addUndoState=False)
s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
s.Line(point1=(0.0, 0.0), point2=(p1, 0.0))
s.HorizontalConstraint(entity=g[7], addUndoState=False)
s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
f, e1, d1 = p.faces, p.edges, p.datums
p.PartitionCellBySketch(sketchPlane=f[0], sketchUpEdge=e1[2], 
    cells=pickedCells, sketch=s)
s.unsetPrimaryObject()
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e = p.edges
pickedEdges =(e[0], )
p.PartitionCellBySweepEdge(sweepPath=e[6], cells=pickedCells, 
    edges=pickedEdges)
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[4], sketchUpEdge=e[6], 
    sketchPlaneSide=SIDE1, origin=(0.0, 1.0, 0.0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=50.91, gridSpacing=1.27, transform=t)
g, v1, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.Line(point1=(0.0, p2), point2=(p3, p3))
s.Line(point1=(p3, p3), point2=(p2, 0.0))
s.Line(point1=(p2, 0.0), point2=(0.0, 0.0))
s.HorizontalConstraint(entity=g[11], addUndoState=False)
s.Line(point1=(0.0, 0.0), point2=(0.0, p2))
s.VerticalConstraint(entity=g[12], addUndoState=False)
s.PerpendicularConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
f1, e1, d2 = p.faces, p.edges, p.datums
p.PartitionCellBySketch(sketchPlane=f1[4], sketchUpEdge=e1[6], 
    cells=pickedCells, sketch=s)
s.unsetPrimaryObject()
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e = p.edges
pickedEdges =(e[0], e[1])
p.PartitionCellBySweepEdge(sweepPath=e[12], cells=pickedCells, 
    edges=pickedEdges)
e, v2, d1 = p.edges, p.vertices, p.datums
p.PartitionEdgeByPoint(edge=e[16], point=p.InterestingPoint(edge=e[16], 
    rule=MIDDLE))
p = mdb.models['Model-1'].parts['blank']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#400 ]', ), )
v, e1, d2 = p.vertices, p.edges, p.datums
p.PartitionFaceByShortestPath(point1=v[11], point2=v[2], faces=pickedFaces)
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e = p.edges
pickedEdges =(e[0], )
p.PartitionCellBySweepEdge(sweepPath=e[23], cells=pickedCells, 
    edges=pickedEdges)