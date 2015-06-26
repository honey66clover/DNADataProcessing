import numpy as np
import csv
from matplotlib.pyplot import *
import matplotlib.colors as colors
import matplotlib.gridspec as gridspec

gs=gridspec.GridSpec(6,10,wspace=0.1, hspace=0.0)
bx1=subplot(gs[0,0:7])
bx2=subplot(gs[1:,0:7])
bx3=subplot(gs[1:,7])
bx4=subplot(gs[1:,8:10])

filename="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\\figs\\fig1\\105profile_1000.csv" 
with open(filename,'rb') as rfile:
    reader = csv.reader(rfile, delimiter=',')
    next(reader, None) #the header
    config=0 #index of configuration
    posi2=[]
    posi3=[]
    posi4=[]
    for row in reader:
        config+=1
	Seed1=row[1] 
	Seed2=row[2]
	nProtein=int(row[3])
        pca1=float(row[4])
        pca2=float(row[5])
        pca3=float(row[6])
        positions=[0]*nProtein
        linestyle=str(1-2*float(nProtein)/10)
        
        x3=[nProtein,nProtein+1]
        y3=[config]*len(x3)
        bx3.plot(x3,y3,linestyle)
        
        
        x41=[pca1,pca1+1]
        y41=[config]*len(x41)
        bx4.plot(x41,y41,linestyle)
        x42=[pca2,pca2+1]
        y42=[config]*len(x42)
        bx4.plot(x42,y42,linestyle)
       
        for i in range(0,nProtein):
            positions[i]=int(row[7+i])
            x2=range(positions[i],positions[i]+14)
            y2=[config]*len(x2)
            bx2.plot(x2,y2,linestyle)
        if nProtein==2:
            posi2.append(positions)
        if nProtein==3:
            posi3.append(positions)
        if nProtein==4:
            posi4.append(positions)
posi2=np.array(posi2).flatten()
posi3=np.array(posi3)
posi4=np.array(posi4)
arraylen=max(posi2.size,posi3.size,posi4.size)
if posi2.size<arraylen:
        posi2=np.append(posi2,[200]*(arraylen-posi2.size))
if posi3.size<arraylen:
        posi3=np.append(posi3,[200]*(arraylen-posi3.size))
if posi4.size<arraylen:
        posi4=np.append(posi4,[200]*(arraylen-posi4.size))
posi=np.vstack((posi2,posi3))
posi=np.vstack((posi,posi4))
posi=np.transpose(posi)
# now determine nice limits by hand:
binwidth = 5
lim = 105
bins = np.arange(0, lim, binwidth)
bx1.hist(posi,bins=bins,normed=1, histtype='bar',color=['1','0.6','0.2'],label=['2HU','3HU','4HU'])

# make some labels invisible
setp(bx3.get_yticklabels() + bx4.get_yticklabels(),visible=False)
show()