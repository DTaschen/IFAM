# -*- coding: utf-8 -*-
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s.FixedConstraint(entity=g[2])
s.ArcByCenterEnds(center=(r_die, 0.0), point1=(r_die, r_ab_d), point2=(r_die-r_ab_d, 0.0), 
    direction=COUNTERCLOCKWISE)
s.Line(point1=(r_die+h_die, r_ab_d), point2=(r_die, r_ab_d))
s.HorizontalConstraint(entity=g[4], addUndoState=False)
s.Line(point1=(r_die-r_ab_d, 0.0), point2=(r_die-r_ab_d, -(r_die+h_die)))
s.VerticalConstraint(entity=g[5], addUndoState=False)
p = mdb.models['Model-1'].Part(name='die', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p.BaseShellRevolve(sketch=s, angle=angle1, flipRevolveDirection=OFF)
s.unsetPrimaryObject()
v, e, d, n = p.vertices, p.edges, p.datums, p.nodes
p.ReferencePoint(point=v[3])