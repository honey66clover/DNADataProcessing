import csv
import itertools
import numpy as np

concentrations= ["HU+37","HU+87","HU+187"]
for concen in concentrations:
	with open("WrLk%(concen)s.dat" % locals(),'wb') as wfile:
		wfile.write("N(bp),Wk,std_Wk,Wk2,std_Wk2,Wk3,std_Wk3,Lk,std_Lk,Lk2,std_Lk2,Lk3,std_Lk3\n")
		for bp in range (80,150):
			data=np.genfromtxt("loops-minicircle_%(bp)i_%(concen)s.dat" % locals(),delimiter=',',skip_header=1)
			nprotein=data[:,7].tolist()
			wr=data[:,9].tolist()
			lk=data[:,10].tolist()
			wr2=[]
			wr3=[]
			lk2=[]
			lk3=[]
			for i in range(0,len(nprotein)):
				if int(nprotein[i])==2:
					wr2.append(wr[i])
					lk2.append(lk[i])
				if int(nprotein[i])==3:
					wr3.append(wr[i])
					lk3.append(lk[i])
			wr=np.array(wr)
			wr2=np.array(wr2)
			wr3=np.array(wr3)
			lk=np.array(lk)
			lk2=np.array(lk2)
			lk3=np.array(lk3)
			wfile.write(str(bp)+","+str(np.mean(wr))+","+str(np.std(wr))+","+str(np.mean(wr2))+","+str(np.std(wr2))+","+str(np.mean(wr3))+","+str(np.std(wr3))+","+str(np.mean(lk))+","+str(np.std(lk))+","+str(np.mean(lk2))+","+str(np.std(lk2))+","+str(np.mean(lk3))+","+str(np.std(lk3))+"\n")