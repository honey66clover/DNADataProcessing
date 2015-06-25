import math
import csv

for bp in range(100,150):
	with open("PCA_%(bp)i_1HUper100_3HU.dat" % locals(),'rb') as rfile, open("/home/juanwei/PCAfiles/3HU_sqrt/PCA_%(bp)i_1HUper100_3HU.dat" % locals(),'wb') as wfile:
		reader = csv.reader(rfile, delimiter=',')
		for row in reader:
			PCA1=math.sqrt(float(row[0]))
			PCA2=math.sqrt(float(row[1]))
			PCA3=math.sqrt(float(row[2]))
			wfile.write(str(PCA1)+","+str(PCA2)+","+str(PCA3)+"\n")