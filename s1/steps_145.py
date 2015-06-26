try:
    from pymol.cgo import *
    from pymol.cmd import *
except:
    print "Not using Pymol"
import os, glob, subprocess, random, string, sets,fnmatch
import numpy as np

devnull = os.devnull

for file in os.listdir('.'):
	if fnmatch.fnmatch(file, "steps*990073,141808*.pdb"):
		load(file, "steps")
	if fnmatch.fnmatch(file, "HU*990073,141808*.pdb"):
		load(file, file)

select("dna", "resn a+g+t+c+da+dg+dt+dc")
select("lac", "half* & !dna")
select("hu", "HU*")

color("0xFFC1C1", "lac")
color("0x6495ED", "dna")
color("0xFFC125", "hu")

hide("lines")
show("cartoon")
cartoon("rect")
set("cartoon_tube_radius", "0.8")
set("cartoon_ring_mode", "3")
set("cartoon_ring_transparency", "0.5")
set("cartoon_ring_finder", "1")
set("ray_trace_fog", "off")
set("ray_opaque_background", "off")
set("ray_trace_frames", "on")
set("hash_max", "50")
bg_color("white") 

orient("steps")
turn("z","90")
zoom("steps","50")
#orient("HU1")
#zoom("HU1","50")
#move("x","50")

deselect()