try:
    from pymol.cgo import *
    from pymol.cmd import *
except:
    print "Not using Pymol"
import os, glob, subprocess, random, string, sets
import numpy as np

devnull = os.devnull

load("Protein-loop.pdb", "steps")
load("Protein-half1.pdb", "half1")
load("Protein-half2.pdb", "half2")
load("Protein-HUs.pdb","proteins")
#load("Protein-HU2.pdb","HU2")
select("dna", "resn a+g+t+c+da+dg+dt+dc")
select("lac", "half* & !dna")
select("hu", "proteins*")

color("0xFFC1C1", "lac")
color("0x6495ED", "dna")
color("0xFFC125", "hu")

# some chains in half1/2/steps are the same, need to rename them to
# different names, or else PyMol gets really confused when aligning
# and displaying as cartoon


create("everything", "all")
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

select("cap", "(chain 'I' & resi 5-23) | (chain 'J' & resi 136-154)")
color("blue","cap")
select("sites", "(chain 'I' & resi 40-44+64-68) | (chain 'J' & resi 115-119+91-95)")
color("green","sites")

deselect()
