import csv

wfilename_2="read_2protein_equilateral-minicircle_HU+37.dat" % locals()
wfilename_3="read_3protein_equilateral-minicircle_HU+37.dat" % locals()
with open (wfilename_2, 'wb') as wfile_2:
	with open (wfilename_3, 'wb') as wfile_3:

		for bp in range(80,150):
			
			rfilename_2="read_2protein_position_lengths-minicircle_%(bp)i_HU+37.dat" % locals()
			equi=protein2=0 #numbers of equilateral configurations and all configurations
			with open (rfilename_2, 'rb') as rfile:
				reader = csv.reader(rfile, delimiter=',')
				for row in reader:
					a1=float(row[4])
					a2=float(row[5])
					if a1/a2>0.95:
						equi=equi+1
					protein2=protein2+1
					ratio_equi=float(equi)/protein2
					other=1-ratio_equi
				wfile_2.write(str(bp)+","+str(ratio_equi)+","+str(other)+"\n")
			
			rfilename_3="read_3protein_position_lengths-minicircle_%(bp)i_HU+37.dat" % locals()
			equi=isosc=protein3=0 #numbers of equilateral configurations and all configurations
			with open (rfilename_3, 'rb') as rfile:
				reader = csv.reader(rfile, delimiter=',')
				for row in reader:
					a1=float(row[4])
					a2=float(row[5])
					a3=float(row[6])
					if (a1/a2>0.95 and a2/a3>0.95):#equilateral
						equi=equi+1
					elif (a1/a2 >0.95 or a2/a3>0.95):#isosceles
						isosc=isosc+1
					protein3=protein3+1
					ratio_equi=float(equi)/protein3
					ratio_isosc=float(isosc)/protein3
					other=1-ratio_equi-ratio_isosc
				wfile_3.write(str(bp)+","+str(ratio_equi)+","+str(ratio_isosc)+","+str(other)+"\n")
				