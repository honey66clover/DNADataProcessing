from subprocess import call

import fnmatch
import os

import numpy as np
#import pandas as pd
from scipy import linalg as LA

for bp in range(100,150):
	pca=[]
	for file in os.listdir('/home/juanwei/snapshots/HUper100_step_par/'): #location of the read dat files
		if fnmatch.fnmatch(file, 'steps_%(bp)i*.dat' % locals()): 
			#print file
			call(["/home/juanwei/localsoftware/x3dna-v2.1/bin/x3dna_utils","cp_std","BDNA"])
			call(["/home/juanwei/localsoftware/x3dna-v2.1/bin/rebuild","-atomic","/home/juanwei/snapshots/HUper100_step_par/%(file)s" % locals(),"/home/juanwei/pdbfiles/%(bp)i_1per100.pdb"  % locals()]) #location of the output pbd files
			rfilename="/home/juanwei/PCAfiles/ref_frames.dat"
			data=np.genfromtxt(rfilename,skip_header=1,comments='...') #skip 1 line at the beginning of the file and all the lines start with ...
			positions=data[::4] #only need the positions, the other three lines are the axes
#print positions
			corr=np.cov(positions,rowvar=0)
#print corr
			e_vals, e_vecs = LA.eig(corr)
			e_vals = np.sort(e_vals) #sort
			e_vals = e_vals[::-1] #reverse the order
			e_vals = e_vals.real #to get the real part ***, stupid python gives me complex number as (***+***j)
			pca=np.append(pca,e_vals)
#pca=np.sort(pca)
#pca=pca[::-1]
	pca=np.reshape(pca,(-1,3))
#print pca		#since we are dealing only the center of the base pair, the result is a bit different
	wfilename="PCA_%(bp)i_HUper100.dat" % locals()
	np.savetxt(wfilename, pca, fmt='%.10e', delimiter=',')

#x3dna_utils cp_std BDNA
#rebuild -atomic /home/juanwei/snapshots/steps_105,minicircle,HU+87,MC,112966,25008.dat test.pdb //test.pdb file can be directed to a path, but other files are under current directory
#call(["rebuild","-atomic","/home/juanwei/snapshots/steps_105,minicircle,HU+87,MC,112966,25008.dat","/home/juanwei/pdbfiles/pdbfile.pdb"])