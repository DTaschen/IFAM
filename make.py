# -*- coding: utf-8 -*-
from abaqus import *
from abaqusConstants import *
import __main__
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior
from decimal import *
import math
execfile("/home/reza/Local/Projekt/Deepdrawing/parameter.py")
execfile("/home/reza/Local/Projekt/Deepdrawing/blank.py")
execfile("/home/reza/Local/Projekt/Deepdrawing/blankholder.py")
execfile("/home/reza/Local/Projekt/Deepdrawing/die.py")
execfile("/home/reza/Local/Projekt/Deepdrawing/punch.py")
execfile("/home/reza/Local/Projekt/Deepdrawing/assembly.py")
execfile("/home/reza/Local/Projekt/Deepdrawing/mesh.py")