import csv

for bp in range(100,101):
	rfilename="protein_positions-minicircle_%(bp)i_HU+187.dat" % locals()
	wfilename="read_protein_positions-minicircle_%(bp)i_HU+187.dat" % locals()
	with open (rfilename, 'rb') as rfile:
		with open (wfilename, 'wb') as wfile:
			wfile.write("N(bp),nProtein,Seed1,Seed2,position\n")
			reader = csv.reader(rfile, delimiter=',')
			next(reader, None) #the header
			row=reader.next() #the first useful line of the data
			Seed1=row[4] 
			Seed2=row[5]
			nProtein=1
			position=[]
			position.append(int(row[6]))
			#initialize
			for row in reader:
				s1=row[4]
				s2=row[5] #read seeds
				if (s1==Seed1 and s2==Seed2):
					nProtein=nProtein+1
					position.append(int(row[6])) #read position
				else:
					wfile.write(str(bp)+","+str(nProtein)+","+str(Seed1)+","+str(Seed2)+","+str(position).strip('[]')+"\n")
					Seed1=s1
					Seed2=s2
					nProtein=1
					position=[]
					position.append(int(row[6]))
				