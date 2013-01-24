# -*- coding: utf-8 -*-
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s1.FixedConstraint(entity=g[2])
s1.ArcByCenterEnds(center=(r_punch-r_ab_p, r_ab_p), point1=(r_punch, r_ab_p), point2=(r_punch-r_ab_p, 0.0), 
    direction=CLOCKWISE)
s1.Line(point1=(0.0, 0.0), point2=(r_punch-r_ab_p, 0.0))
s1.HorizontalConstraint(entity=g[4], addUndoState=False)
s1.Line(point1=(r_punch, r_ab_p), point2=(r_punch, h_punch))
s1.VerticalConstraint(entity=g[5], addUndoState=False)
p = mdb.models['Model-1'].Part(name='punch', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p.BaseShellRevolve(sketch=s1, angle=angle1, flipRevolveDirection=OFF)
s1.unsetPrimaryObject()
v1, e1, d1, n1 = p.vertices, p.edges, p.datums, p.nodes
p.ReferencePoint(point=v1[0])