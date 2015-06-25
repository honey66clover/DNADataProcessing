import numpy as np

with open ("PCA12HU.dat", 'wb') as wfile1,open ("PCA22HU.dat", 'wb') as wfile2,open ("PCA32HU.dat", 'wb') as wfile3:
	for bp in range(100,150):
		pca=np.genfromtxt("PCA_%(bp)i_1HUper100_2HU.dat" % locals(),delimiter=',')# matrix with 3 cols for each PCA component
		pca1=pca[:,0].tolist() #first column, first PCA component		
		pca2=pca[:,1].tolist() 
		pca3=pca[:,2].tolist() 
		
		wfile1.write(str(bp)+","+str(pca1).strip('[]')+"\n") #PCA12HU.dat each row is the first PCA component for one chain length
		wfile2.write(str(bp)+","+str(pca2).strip('[]')+"\n") #50 rows in 2HU
		wfile3.write(str(bp)+","+str(pca3).strip('[]')+"\n")
