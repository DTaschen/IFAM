# -*- coding: utf-8 -*-
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['blank']
a.Instance(name='blank-1', part=p, dependent=ON)
p = mdb.models['Model-1'].parts['blankholder']
a.Instance(name='blankholder-1', part=p, dependent=ON)
p = mdb.models['Model-1'].parts['die']
a.Instance(name='die-1', part=p, dependent=ON)
p = mdb.models['Model-1'].parts['punch']
a.Instance(name='punch-1', part=p, dependent=ON)
a.translate(instanceList=('die-1', ), vector=(0.0, dicke-5.0, 0.0))
#-----------------------------------------------------------------
# vector=(55,1,0)-(55,5,0)
#-----------------------------------------------------------------