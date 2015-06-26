import csv, itertools
bps = range(80,126)
concentrations = [37,87,187]
products = itertools.product(concentrations,bps) #37_80,...37_126,87_80,...87_126,...
writefile = "protein_bound_probabilities.dat"
with open (writefile, 'w+') as wfile:
	wfile.write("N(bp),0HU,1HU,2HU,3HU,4HU,5HU,6HU,7HU,8HU,9HU,10HU,11HU, ,N(bp),0HU,1HU,2HU,3HU,4HU,5HU,6HU,7HU,8HU,9HU,10HU,11HU, ,N(bp),0HU,1HU,2HU,3HU,4HU,5HU,6HU,7HU,8HU,9HU,10HU,11HU\n")
#	writer = csv.writer(wfile)
#	writer.writerow("N(bp),0HU,1HU,2HU,3HU,4HU,5HU,6HU,7HU,8HU,9HU,10HU,11HU")
for i, (concentration,bp) in enumerate (products):
	filename = "loops-minicircle_%(bp)i_HU+%(concentration)i.dat" % locals()
	#print filename,
	#loops-minicircle_100_HU+87.dat loops-minicircle_100_HU+187.dat ... loops-minicircle_105_HU+187.dat
	#npro = [] #numbers of protein bound
	counts = [0]*12
	prob = [0]*12
#	prob[0] = bp
	all = 0
	with open (filename, 'r') as file:
		reader = csv.reader(file, delimiter=',')
		for row in reader:
			counts[int(row[7])]=counts[int(row[7])]+1 
			all=all+1
	for i in range(0,12):
		prob[i]=float(counts[i])/all
	with open (writefile, 'a') as wfile:
		wfile.write(str(bp)+','+str(prob).strip('[]')+'\n')
			
			
			
			
			npro.append(row[7])#read the numbers of protein bound into list npro
#	print(npro)
	for i in range(0,12):
		counts[i] = npro.count(str(i)) #count how many times i proteins are bound
		all = all+counts[i] #all counts
	for i in range(0,12):
		prob[i]=float(counts[i])/all #probabilities
	with open (writefile, 'a') as wfile:
#		writer = csv.writer(wfile, delimiter=',')
#		writer.writerow([bp,prob])
		wfile.write(str(bp)+','+str(prob).strip('[]')+'\n')
