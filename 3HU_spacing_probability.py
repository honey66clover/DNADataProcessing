#this script is used for fig s2
import csv

wfilename="3HU_spacing_probability_HU+37.dat" % locals()
with open (wfilename, 'wb') as wfile:
	for bp in range (80,150):
		rfilename="read_3protein_position_lengths-minicircle_%(bp)i_HU+37.dat" % locals()
		with open (rfilename, 'rb') as rfile:
			reader = csv.reader(rfile, delimiter=',')
			count=0
			spacing=[0 for x in range(bp)] # a list, the index is the spacing and the value will be the probability
			for row in reader:
				spacing[int(row[4])]+=1 #increment
				spacing[int(row[5])]+=1 
				spacing[int(row[6])]+=1 #count in three HUs in one row, one configuration
				count+=3
			for i in range(0,bp-1):
				spacing[i]=float(spacing[i])/count
		wfile.write(str(bp)+","+str(spacing).strip('[]')+"\n")
			
			
	