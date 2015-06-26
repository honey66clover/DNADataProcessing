import csv
import itertools

concentrations= ["HU+37","HU+87","HU+187"]
for concen in concentrations:
	with open("Lkdist%(concen)s.dat" % locals(),'wb') as wlk, open("Lkdist%(concen)s_2HU.dat" % locals(),'wb') as wlk2, open("Lkdist%(concen)s_3HU.dat" % locals(),'wb') as wlk3, open("Wrdist%(concen)s_0.1.dat" % locals(),'wb') as wwr,open("Wrdist%(concen)s_2HU_0.1.dat" % locals(),'wb') as wwr2, open("Wrdist%(concen)s_3HU_0.1.dat" % locals(),'wb') as wwr3:
		############headers##############################################
		wrrange=[-1.0]
		for i in range(0,21):#wr range[-1.0,1.0], step 0.1 wr[10]=0
			wrrange.append(wrrange[i]+0.1)
		wwr.write("N(bp),"+str(wrrange).strip('[]')+"\n")
		wwr2.write("N(bp),"+str(wrrange).strip('[]')+"\n")
		wwr3.write("N(bp),"+str(wrrange).strip('[]')+"\n")
		lkrange=[0] #lkrange starts from 0
		for i in range(0,20):
			lkrange.append(lkrange[i]+1)
		wlk.write("N(bp),"+str(lkrange).strip('[]')+"\n")
		wlk2.write("N(bp),"+str(lkrange).strip('[]')+"\n")
		wlk3.write("N(bp),"+str(lkrange).strip('[]')+"\n")
		###########################################
		for bp in range(80,150):
			wr=[0]*21 #index:(0 ~ 200), value(-1.0 ~ 1.0)
			wr2=[0]*21
			wr3=[0]*21
			lk=[0]*20 
			lk2=[0]*20
			lk3=[0]*20	
			count=0
			count2=0
			count3=0 #to count numbers of configurations
			with open("loops-minicircle_%(bp)i_%(concen)s.dat" % locals(), 'rb') as rfile:
				reader = csv.reader(rfile, delimiter=',')
				next(reader, None)  # skip the headers
				for row in reader:
					nProtein=int(row[7])
					wrid=int(round(float(row[9])/0.1))+10 #index, step 0.01, numbers of wr=0 will be stored in wr[100]
					lkid=int(float(row[10]))
					if wrid<21 and wrid>0:
						wr[wrid]+=1
					lk[lkid]+=1
					count+=1
					if nProtein==2:
						if wrid<21 and wrid>0:
							wr2[wrid]+=1
						lk2[lkid]+=1
						count2+=1
					if nProtein==3:
						if wrid<21 and wrid>0:
							wr3[wrid]+=1
						lk3[lkid]+=1
						count3+=1
				for i in range(0,21): #convert counts into distribution
					wr[i]=float(wr[i])/count
					if count2==0:
						wr2[i]="NA"
					else:
						wr2[i]=float(wr2[i])/count2
					if count3==0:
						wr3[i]="NA"
					else:				
						wr3[i]=float(wr3[i])/count3
				for i in range(0,20):
					lk[i]=float(lk[i])/count
					if count2==0:
						lk2[i]="NA"
					else:
						lk2[i]=float(lk2[i])/count2
					if count3==0:
						lk3[i]="NA"
					else:
						lk3[i]=float(lk3[i])/count3
				wwr2.write(str(bp)+","+str(wr2).strip('[]')+"\n")
				wwr3.write(str(bp)+","+str(wr3).strip('[]')+"\n")
				wwr.write(str(bp)+","+str(wr).strip('[]')+"\n")
				wlk2.write(str(bp)+","+str(lk2).strip('[]')+"\n")
				wlk3.write(str(bp)+","+str(lk3).strip('[]')+"\n")
				wlk.write(str(bp)+","+str(lk).strip('[]')+"\n")
				
					
					