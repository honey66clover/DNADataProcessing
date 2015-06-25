import csv

for i in ["1","2","3"]:
	with open("PCA%(i)sall_sqrt.dat" % locals(), 'rb') as rfile, open("PCA%(i)sdist_all_sqrt.dat" % locals(),'wb') as wfile:
		length=[0]*80
		for j in range(0,80): 
			length[j]=j #lengths in range(0,80)
		wfile.write("N(bp),"+str(length).strip('[]')+"\n")
		reader = csv.reader(rfile, delimiter=',')
		for row in reader: #for each chain length
			all=len(row)-1 # numbers of configurations, row[0]=bp
			count=[0]*80
			dist=[0]*80
			for i in range(1,all+1): #for each configuration
				r=int(round(float(row[i]))) #divide PCA values in groups every 200
				count[r]+=1 #count the numbers in each group, the index is the 
			for i in range(0,80): 
				dist[i]=float(count[i])/all
			wfile.write(row[0]+","+str(dist).strip('[]')+"\n") #row[0]=bp
