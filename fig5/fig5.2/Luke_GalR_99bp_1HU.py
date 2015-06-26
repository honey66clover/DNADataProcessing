try:
    from pymol.cgo import *
    from pymol.cmd import *
except:
    print "Not using Pymol"
import os, glob, subprocess, random, string, sets
import numpy as np

devnull = os.devnull

load("Luke_GalR_99bp_1HU_DNA.pdb", "steps")
load("Luke_GalR_99bp_1HU_GAL.pdb", "gal-lacr")
load("out.pdb", "galdna")
#load("galdna_repair.pdb","galdna")
load("Luke_GalR_99bp_1HU_HU.pdb","HU1")
#align("o. galdna and c. A", "o. gal-lacr and c. A")

select("dna", "resn a+g+t+c+da+dg+dt+dc")
select("gal", "gal-lacr & !dna")
select("hu", "HU*")

color("0xFFC1C1", "gal")
color("0x6495ED", "dna")
color("0xFFC125", "hu")

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

select("cap", "o. steps & ((c. A & i. 5-25)| (c. B & resi 176-196))")
color("blue","cap")
select("sites", "o. steps &(c. A & resi 39-48) | (c. B & resi 153-162)")
color("green","sites")
deselect()
