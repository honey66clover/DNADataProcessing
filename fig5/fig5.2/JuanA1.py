try:
    from pymol.cgo import *
    from pymol.cmd import *
except:
    print "Not using Pymol"
import os, glob, subprocess, random, string, sets
import numpy as np

devnull = os.devnull

load("JuanA1.pdb", "A1loop")

select("dna", "resn a+g+t+c+da+dg+dt+dc")
select("lac", "!dna")

color("0xFFC1C1", "lac")
color("0x6495ED", "dna")

orient("lac")
zoom(complete=1)
viewport(1400,1400)

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

select("cap", "(chain 'X' & resi 22-41) | (chain 'Y' & resi 73-92)")
color("blue","cap")
select("sites", "(chain 'X' & resi 57-62+81-86) | (chain 'Y' & resi 52-57+28-33)")
color("green","sites")

deselect()
