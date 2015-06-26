try:
    from pymol.cgo import *
    from pymol.cmd import *
except:
    print "Not using Pymol"
import os, glob, subprocess, random, string, sets
import numpy as np

devnull = os.devnull

load("NoProtein-Gal-P1-loop.pdb", "steps")
load("NoProtein-Gal-LacR.pdb", "gal-lacr")
load("galdna_repair.pdb","galdna")
align("o. galdna and c. A", "o. gal-lacr and c. A")

select("dna", "resn a+g+t+c+da+dg+dt+dc")
select("gal", "gal-lacr & !dna")
#select("hu", "pro*")

color("0xFFC1C1", "gal")
color("0x6495ED", "dna")
#color("0xFFC125", "hu")

# some chains in half1/2/steps are the same, need to rename them to
# different names, or else PyMol gets really confused when aligning
# and displaying as cartoon

orient("gal")

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

select("cap", "o. steps & ((c. G & i. 5-25)| (c. H & resi 182-202))")
color("blue","cap")
select("sites", "o. steps &(c. G & resi 39-49) | (c. H & resi 158-168)")
color("green","sites")
deselect()
