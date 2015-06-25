import numpy as np

with open ("PCA1all_sqrt.dat", 'wb') as wfile1,open ("PCA2all_sqrt.dat", 'wb') as wfile2,open ("PCA3all_sqrt.dat", 'wb') as wfile3:
	for bp in range(100,150):
		pca=np.genfromtxt("PCA_%(bp)i_1HUper100.dat" % locals(),delimiter=',')# matrix with 3 cols for each PCA component
		pca1=pca[:,0].tolist() #first column, first PCA component		
		pca2=pca[:,1].tolist() 
		pca3=pca[:,2].tolist() 
		
		wfile1.write(str(bp)+","+str(pca1).strip('[]')+"\n") #PCA1all.dat each row is the first PCA component for one chain length
		wfile2.write(str(bp)+","+str(pca2).strip('[]')+"\n") #50 rows in all
		wfile3.write(str(bp)+","+str(pca3).strip('[]')+"\n")
