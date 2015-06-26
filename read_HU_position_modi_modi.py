import csv
from operator import itemgetter
for bp in range(105,106):
	rfilename="protein_positions-minicircle_%(bp)i_HU+87.dat" % locals()
	wfilename="modi_read_protein_positions-minicircle_%(bp)i_HU+87.dat" % locals()
	wfilename_2="read_2protein_position_lengths-minicircle_%(bp)i_HU+87.dat" % locals()
	wfilename_3="read_3protein_position_lengths-minicircle_%(bp)i_HU+87.dat" % locals()
	with open (rfilename, 'rb') as rfile:
		with open (wfilename, 'wb') as wfile:
			wfile.write("N(bp),nProtein,Seed1,Seed2,position,configuration\n")
			reader = csv.reader(rfile, delimiter=',')
			next(reader, None)
			row=reader.next()
			Seed1=row[4] 
			Seed2=row[5]
			nProtein=1
			position=[]
			modiposi=[] #for shifted position
			lengths=[] #for lengths of the polygon
			position.append(int(row[6]))
			with open (wfilename_2, 'wb') as wfile_2:
				with open (wfilename_3, 'wb') as wfile_3:
					#initialize
					for row in reader:
						s1=row[4]
						s2=row[5] #read seeds
						if (s1==Seed1 and s2==Seed2):
							nProtein=nProtein+1
							position.append(int(row[6])) #read position
						else:
							if nProtein==1:
								modiposi=[0]
							if nProtein==2:
								lengths=[position[1]-position[0],bp-position[1]+position[0]]
								lengths.sort()
								modiposi=[-lengths[0]/2,lengths[0]/2]
								wfile_2.write(str(bp)+","+str(nProtein)+","+str(Seed1)+","+str(Seed2)+","+str(lengths).strip('[]')+"\n") 
							if nProtein==3:
								lengths=[position[1]-position[0],position[2]-position[1],bp-position[2]+position[0]]
								lengths.sort()
								modiposi=[-lengths[0],0,lengths[1]]
								wfile_3.write(str(bp)+","+str(nProtein)+","+str(Seed1)+","+str(Seed2)+","+str(lengths).strip('[]')+"\n") 
							if nProtein==4:
								lengths=[position[1]-position[0],position[2]-position[1],position[3]-position[2],bp-position[3]+position[0]]
								minid=min(enumerate(lengths), key=itemgetter(1))[0] #find out the index of the min element
								minlen=lengths[minid]
								if minid==0:
									seclen=min(lengths[3],lengths[1])
									thrlen=max(lengths[3],lengths[1])
								if minid==3:
									seclen=min(lengths[0],lengths[2])
									thrlen=max(lengths[0],lengths[2])
								else:
									seclen=min(lengths[minid-1],lengths[minid+1])
									thrlen=max(lengths[minid-1],lengths[minid+1])
								modiposi=[-seclen-minlen/2,-minlen/2,minlen/2,thrlen+minlen/2]
							wfile.write(str(bp)+","+str(nProtein)+","+str(Seed1)+","+str(Seed2)+","+str(modiposi).strip('[]')+"\n")
							Seed1=s1
							Seed2=s2
							nProtein=1
							position=[]
							position.append(int(row[6]))
				
