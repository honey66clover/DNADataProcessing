
PCAconsub: makes folders for each chain length and copies PCAsub to each folder; exercise PCAsub.
PCAsub: submit jobs; exercise PCArunall
PCArunall: do PCA analysis for all chain length

PCAconsub_nProtein: separate 2HU and 3HU cases
PCAsub_nProtein
PCArunall_nProtein

readPCAall: put 3 PCA components in 3 files, one for all chain length.
readPCA2HU: for 2HU cases
readPCA3HU: for 3HU cases

readPCAdist_2HU:
readPCAdist_3HU:
readPCAdist_allHU:

sqrt: forget to take the square root in covariance matrix... fix that later...should fix PCArunall* and readPCAdist_*