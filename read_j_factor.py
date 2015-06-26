import csv

writefile = "j_factors.dat"
with open (writefile, 'w+') as wfile:
	wfile.write("N(bp),J(1HU/50),J(1HU/100),J(1HU/200)\n")
for bp in range(80,126):
	with open (writefile, 'a') as wfile:
		wfile.write(str(bp)+',')
	for concentration in [37,87,187]:
		filename = "summary-minicircle_%(bp)i_HU+%(concentration)i.dat" % locals()
		with open (filename, 'r') as file:
			reader = csv.reader(file, delimiter=',')
			for row in reader:
				j=row[5] #read the j factors
		with open (writefile, 'a') as wfile:
			wfile.write(j+',')
	with open (writefile, 'a') as wfile:
		wfile.write('\n')
