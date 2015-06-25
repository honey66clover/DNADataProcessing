#!/usr/bin/python

import sys
from subprocess import call
import fnmatch
import os
import csv
import numpy as np
from scipy import linalg as LA

bp=105 #pass argument from jobfile
pca2=[] #to store PCA analysis for 2HU cases
pca3=[] #to store PCA analysis for 3HU cases

rloopfile='/home/juanwei/snapshots/105/loops-minicircle_105_HU+87.dat' % locals() #read loop*.dat files to look for nProteins and the two Seeds
with open (rloopfile, 'rb') as rfile:
	reader = csv.reader(rfile, delimiter=',')
	next(reader, None) #the header
	row=reader.next() #the first useful line of the data
	for row in reader:
		Seed1=row[4] 
		Seed2=row[5]
		nProtein=int(row[7])

		for file in os.listdir('.'): #location of the read dat files
			if fnmatch.fnmatch(file, 'steps_105,minicircle,HU+87,MC,%(Seed1)s,%(Seed2)s.dat' % locals()): 
				call(["x3dna_utils","cp_std","BDNA"])
				call(["rebuild","-atomic",file,"/home/juanwei/snapshots/pdbfile.pdb"]) #location of the output pbd files
				rfilename="ref_frames.dat"
				data=np.genfromtxt(rfilename,skip_header=1,comments='...') #skip 1 line at the beginning of the file and all the lines start with ...
				positions=data[::4] #only need the positions, the other three lines are the axes
				corr=np.cov(positions,rowvar=0)
				e_vals, e_vecs = LA.eig(corr)
				e_vals = np.sort(e_vals) #sort
				e_vals = e_vals[::-1] #reverse the order
				e_vals = e_vals.real #to get the real part ***, stupid python gives me complex number as (***+***j)
				if (nProtein==2):
					pca2=np.append(pca2,e_vals)
				if (nProtein==3):
					pca3=np.append(pca3,e_vals)
#pca=np.sort(pca)
#pca=pca[::-1]
pca2=np.reshape(pca2,(-1,3))
pca3=np.reshape(pca3,(-1,3))
#print pca		#since we are dealing only the center of the base pair, the result is a bit different
wfilename2="/home/juanwei/snapshots/PCA_105_HUper100_2HU.dat" % locals()
wfilename3="/home/juanwei/snapshots/PCA_105_HUper100_3HU.dat" % locals()
np.savetxt(wfilename2, pca2, fmt='%.10e', delimiter=',')
np.savetxt(wfilename3, pca3, fmt='%.10e', delimiter=',')
#x3dna_utils cp_std BDNA
#rebuild -atomic /home/juanwei/snapshots/steps_105,minicircle,HU+87,MC,112966,25008.dat test.pdb //test.pdb file can be directed to a path, but other files are under current directory
#call(["rebuild","-atomic","/home/juanwei/snapshots/steps_105,minicircle,HU+87,MC,112966,25008.dat","/home/juanwei/pdbfiles/pdbfile.pdb"])