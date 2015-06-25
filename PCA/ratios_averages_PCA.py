import csv
import numpy as np

with open("PCA_1HUper50_2HU.dat" % locals(),'wb') as wfile:
	wfile.write("N(bp),PA1,std_PA1,PA2,std_PA2,PA3,std_PA3,PA1/PA2,std_PA1/PA2,PA1/PA3,std_PA1/PA3,PA2/PA3,std_PA2/PA3\n")
	for bp in range(100,130):
		data=np.genfromtxt("PCA_%(bp)i_1HUper50_2HU.dat" % locals(),delimiter=',',skip_header=0)
		pa1=data[:,0]
		pa2=data[:,1]
		pa3=data[:,2]
		wfile.write(str(bp)+","+str(np.mean(pa1))+","+str(np.std(pa1))+","+str(np.mean(pa2))+","+str(np.std(pa2))+","+str(np.mean(pa3))+","+str(np.std(pa3))+","+str(np.mean(pa1/pa2))+","+str(np.std(pa1/pa2))+","+str(np.mean(pa1/pa3))+","+str(np.std(pa1/pa3))+","+str(np.mean(pa2/pa3))+","+str(np.std(pa2/pa3))+"\n")