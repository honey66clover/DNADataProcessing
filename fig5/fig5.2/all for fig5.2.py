try:
    from pymol.cgo import *
    from pymol.cmd import *
except:
    print "Not using Pymol"
import os, glob, subprocess, random, string, sets
import numpy as np

devnull = os.devnull
#lac A1
load("JuanA1.pdb", "lacA1loop")
#lac P1
load("Protein-loop.pdb", "lacP1loop")#DNA
load("Protein-half1.pdb", "half1")#lac
load("Protein-half2.pdb", "half2")#lac
load("Protein-HUs.pdb","HUs")#HU
#gal P1
load("NoProtein-Gal-P1-loop.pdb", "galP1loop")#DNA
load("NoProtein-Gal-LacR.pdb", "galP1")#gal
load("galdna_repair.pdb","galP1dna")#galdna
#gal A1
load("Luke_GalR_99bp_1HU_DNA.pdb", "galA1loop")#DNA
load("Luke_GalR_99bp_1HU_GAL.pdb", "galA1")#gal
load("out.pdb", "galA1dna")#galdna
load("Luke_GalR_99bp_1HU_HU.pdb","HU1")#HU

select("dna", "resn a+g+t+c+da+dg+dt+dc")
select("hu", "HU*")
select("proteins", "!dna & !hu")

select("lacA1","lacA1loop & !dna")
select("lacP1","half* & !dna")

color("0xFFC1C1", "proteins")
color("0xFFC125", "hu")
color("0x6495ED", "dna")

align("o. galP1dna and c. A", "o. galP1 and c. A")

select("cap", "(o. lacA1loop & ((chain 'X' & resi 22-41) | (chain 'Y' & resi 73-92))) | (o. lacP1loop&((chain 'I' & resi 5-23) | (chain 'J' & resi 136-154))) | (o. galP1loop & ((c. G & i. 5-25)| (c. H & resi 182-202))) | (o. galA1loop & ((c. A & i. 5-25)| (c. B & resi 176-196)))")
color("blue","cap")
select("sites", "(o. lacA1loop & ((chain 'X' & resi 57-62+81-86) | (chain 'Y' & resi 52-57+28-33))) | (o. lacP1loop&((chain 'I' & resi 40-44+64-68) | (chain 'J' & resi 115-119+91-95))) | (o. galP1loop & ((c. G & resi 39-49) | (c. H & resi 158-168))) | (o. galA1loop &((c. A & resi 39-48) | (c. B & resi 153-162)))")
color("green","sites")

select("lacA1all","lacA1loop")
select("lacP1all","lacA1loop | half* |HUs")
select("galP1all","galP1*")
select("galA1all","galA1*")
deselect()

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

orient("lacA1")
