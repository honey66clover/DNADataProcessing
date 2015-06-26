import csv, itertools
bps = range(80,150)
concentrations = [187]
products = itertools.product(bps, concentrations)
writefile = "protein_bound_probabilities_1per200.dat"
with open (writefile, 'w+') as wfile:
	wfile.write("N(bp),0HU,1HU,2HU,3HU,4HU,5HU,6HU,7HU,8HU,9HU,10HU,11HU\n")
#	writer = csv.writer(wfile)
#	writer.writerow("N(bp),0HU,1HU,2HU,3HU,4HU,5HU,6HU,7HU,8HU,9HU,10HU,11HU")
for i, (bp, concentration) in enumerate (products):
	filename = "loops-minicircle_%(bp)i_HU+%(concentration)i.dat" % locals()
	#print filename,
	#loops-minicircle_100_HU+87.dat loops-minicircle_100_HU+187.dat ... loops-minicircle_105_HU+187.dat
	pro_bound = []
	counts = [0]*12
	prob = [0]*12
#	prob[0] = bp
	all = 0
	with open (filename, 'r') as file:
		reader = csv.reader(file, delimiter=',')
		for row in reader:
			pro_bound.append(row[7])#read the numbers of protein bound into list pro_bound
#	print(pro_bound)
	for i in range(0,12):
		counts[i] = pro_bound.count(str(i)) #count how many times i proteins are bound
		all = all+counts[i] #all counts
	for i in range(0,12):
		prob[i]=float(counts[i])/all #probabilities
	with open (writefile, 'a') as wfile:
#		writer = csv.writer(wfile, delimiter=',')
#		writer.writerow([bp,prob])
		wfile.write(str(bp)+','+str(prob).strip('[]')+'\n')
