import csv
import numpy as np
from operator import itemgetter
with open("C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s5\\250\HU105profile_250.csv",'rb') as rfile, open ("C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s5\\250\HU105position_250.csv",'wb') as wfile:
    reader = csv.reader(rfile, delimiter=',')
    next(reader, None) #the header
    for row in reader:
        if int(row[3])==2:
            a1=int(row[8])-int(row[7])
            a2=105-a1
            posit=[min(a1,a2)/2-min(a1,a2),min(a1,a2)/2]
            wfile.write("105,2,"+str(posit).strip('[]')+"\n")
        if int(row[3])==3:
            a1=int(row[8])-int(row[7])
            a2=int(row[9])-int(row[8])
            a3=105-a1-a2
            lengths=[a1,a2,a3]
            lengths.sort()
            posit=[-lengths[0],0,lengths[1]]           
            wfile.write("105,3,"+str(posit).strip('[]')+"\n")
        if int(row[3])==4:
            a1=int(row[8])-int(row[7])
            a2=int(row[9])-int(row[8])
            a3=int(row[10])-int(row[9])
            a4=105-a1-a2-a3
            lengths=[a1,a2,a3,a4]
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
            posit=[-seclen-minlen/2,-minlen/2,minlen/2,thrlen+minlen/2]
            wfile.write("105,4,"+str(posit).strip('[]')+"\n")
