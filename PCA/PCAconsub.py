from subprocess import call
import os
import itertools

concentrations= ["HU+87"]
lacs = ["minicircle"]
bps = range(105, 150)	

methods = itertools.product(concentrations, lacs, bps)

for bp in bps: #make folders... each for one length
	call(["mkdir","/home/juanwei/PCAfiles/%(bp)i" % locals()]) #each different folder for each bp
	call(["cp","/home/juanwei/PCAfiles/PCAsub.py","/home/juanwei/PCAfiles/%(bp)i/" % locals()]) #copy the PCAsub to different folders
	os.chdir("/home/juanwei/PCAfiles/%(bp)i/" % locals()) #have to go to each folder, otherwise it still submits the job in PCAfiles/
	call(["python","/home/juanwei/PCAfiles/%(bp)i/PCAsub.py" % locals(),"%(bp)i" % locals()]) #execute each PCAsub, passing argument bp