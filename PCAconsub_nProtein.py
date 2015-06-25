from subprocess import call
import os
#import itertools

#concentrations= ["HU+87"]
#lacs = ["minicircle"]
bps = [109]

#methods = itertools.product(concentrations, lacs, bps)

for bp in bps: #make folders... each for one length
	call(["mkdir","/home/juanwei/PCAfiles/1HUper50/%(bp)i" % locals()]) #the folders are there #each different folder for each bp
	call(["cp","/home/juanwei/PCAfiles/PCAsub_nProtein.py","/home/juanwei/PCAfiles/1HUper50/%(bp)i/" % locals()]) #copy the PCAsub to different folders
	os.chdir("/home/juanwei/PCAfiles/1HUper50/%(bp)i/" % locals()) #have to go to each folder, otherwise it still submits the job in PCAfiles/
	call(["python","/home/juanwei/PCAfiles/1HUper50/%(bp)i/PCAsub_nProtein.py" % locals(),"%(bp)i" % locals()]) #execute each PCAsub, passing argument bp