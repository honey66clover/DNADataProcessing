import numpy as np
import fnmatch
import os
import numpy.linalg as linalg

#for one bp first, later can be generalized to many
data=np.array([0]) 
for file in os.listdir('/home/juanwei/snapshots_105/'% locals()): #location of the read dat files
	if fnmatch.fnmatch(file, 'steps_105*.dat' % locals()):
		stepar=np.loadtxt(file,skiprows=4,usecols=(1,2,3,4,5,6)) # bp*6 matix, skip rows and first column
		stepar=np.reshape(stepar,-1) #matix to array=((bp1),(bp2),...,(bpn))   bpi=(1,...,6)
		if data.size==1: #reading first file
			data=stepar
		else:
			data=np.vstack((data,stepar)) #bind two columns, configurations*(bp*6) matix
mean=np.mean(data,axis=0) #column mean 1*(bp*6) row vector
std=np.std(data,axis=0) 
data=(data-mean)/std
data=data.T #(bp*6)*configurations matrix
cov=np.cov(data)
eigenValues,eigenVectors = linalg.eig(cov)
idx = eigenValues.argsort()  #small to large
idx=idx[::-1] #large to small
eigenValues = eigenValues[idx] #sorted eigenvalues and corresponding eigenvectors
header=np.append([0],eigenValues)
eigenVectors = eigenVectors[:,idx] #large to small
eigenVectors = eigenVectors.T #each row is a eigenvector
eigenVectors= std*eigenVectors+mean #because the algebra is on column
mean_eigen=np.vstack((mean,eigenVectors)) #for mean and eigen images
mean_eigen = mean_eigen.T #the columns are mean and eigenvectors
eigen=np.vstack((header.real,mean_eigen.real))
np.savetxt("normalmodes.dat",eigen)

for i in range(0,5): #convert mean and first four eigenvectors back into step files
	with open("normalmodes%(i)i.dat" % locals(), 'wb') as wfile:
		wfile.write(" 105 base-pairs\n 0  step parameters\n shift   slide    rise    tilt    roll   twist\nA-T 0.000 0.000 0.000 0.000 0.000 0.000\n")
		steps=eigen[1:,i]
		steps=np.reshape(steps,(-1,6))
		for j in range(0,steps.shape[0]):
			step=np.array_str(steps[j,:],precision=3)
			step=str(step).strip('[]')
			#step=" ".join(step)
			wfile.write("A-T "+step+"\n")