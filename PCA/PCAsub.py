from os import system as s
from subprocess import call
import sys #to receive arguments from PCAsubcontrol.py

header = """#!/bin/sh
#PBS -l nodes=1
#PBS -l walltime=5:00:00
#PBS -V
#PBS -M honey66clover@gmail.com
cd $PBS_O_WORKDIR
"""

bp=int(sys.argv[1]) #receive arguments from PCAsubcontrol.py

j = "/home/juanwei/PCAfiles/%(bp)i/job_PCA_%(bp)i" % locals()  #filename of the job file, each in different folder so that ref_frame don't mixed up
with open(j, "w") as x:
    x.write("%(header)s /home/juanwei/lib/python-2.7.5/bin/python /home/juanwei/PCAfiles/PCArunall.py %(bp)i\n " % locals()) #passing argument bp to PCArunall.py
s("qsub %(j)s" % locals())