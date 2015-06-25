import csv
import numpy as np
with open("read100example.dat", 'wb') as wfile:
	wfile.write(",,")
	for bp in range(100,149):
		wfile.write(str(bp)+",,,")
	wfile.write(str(bp+1)+"\n")
	
	wfile.write("config,")
	for i in range(0,50):
		wfile.write("PA1,PA2,PA3,")
	wfile.write("\n")
	
	for i in range(0,100):
		wfile.write(str(i+1).strip('[]')+",")
		for bp in range(100,149):
			pca=np.genfromtxt("PCA_%(bp)i_1HUper100_2HU.dat" % locals(),skip_header=0,delimiter=",")
			wfile.write(str(pca[i,:].tolist()).strip('[]')+",")
		pca=np.genfromtxt("PCA_149_1HUper100_2HU.dat" % locals(),skip_header=0,delimiter=",")
		wfile.write(str(pca[i,:].tolist()).strip('[]')+"\n")