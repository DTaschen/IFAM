# -*- coding: utf-8 -*-
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s1.FixedConstraint(entity=g[2])
s1.ArcByCenterEnds(center=(r_blankholder, r_ab_b), point1=(r_blankholder, 0.0), point2=(r_blankholder-r_ab_b, r_ab_b), 
    direction=CLOCKWISE)
s1.Line(point1=(r_blankholder, 0.0), point2=(r_blankholder+h_blankholder, 0.0))
s1.HorizontalConstraint(entity=g[4], addUndoState=False)
p = mdb.models['Model-1'].Part(name='blankholder', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p.BaseShellRevolve(sketch=s1, angle=angle1, flipRevolveDirection=OFF)
s1.unsetPrimaryObject()
v, e, d, n = p.vertices, p.edges, p.datums, p.nodes
p.ReferencePoint(point=v[0])