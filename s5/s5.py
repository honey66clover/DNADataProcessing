import csv
import numpy as np
from matplotlib.pyplot import *
import matplotlib.gridspec as gridspec
import pandas as pd


fig=figure(figsize=(3.42,2.1),dpi=600) #is in control
#fig={'figsize':(3.42,5),'dpi':600} #is not in control
font = {'family':'Arial','weight':'normal','size':7} #family is in control for axis labels, size is in control for tick labels only
rc('font', **font)
#rc('figure',**fig)
gs1 = gridspec.GridSpec(4, 5)
gs1.update(left=0.1, right=0.53, wspace=0.08,hspace=0.05)
ax1=subplot(gs1[0:1, 0:3])
ax2=subplot(gs1[1:, 0:3])
ax3=subplot(gs1[1:, 3:4])
gs2 = gridspec.GridSpec(4, 5)
gs2.update(left=0.56, right=1., wspace=0.08, hspace=0.05)
bx1=subplot(gs2[0:1, 0:3])
bx2=subplot(gs2[1:, 0:3])
bx3=subplot(gs2[1:, 3:4])

with open("C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s5\modi_read_protein_positions-minicircle_105_HU+87_1125.csv",'rb') as afile2:
    reader = csv.reader(afile2, delimiter=',')
    config=0
    a3x=[0] #nProtein
    posicount=[0]*101
    for row in reader:
        config+=1
        nPro=int(row[1])
        a3x.append(nPro) #nProtein
        for i in range(0,nPro):
            positions=[0]*nPro
            positions[i]=int(row[4+i])
            x1=[positions[i]-7,positions[i]+7]
            y1=[config]*len(x1)
            if nPro==2:
                linestyle='0.8'
            if nPro==3:
                linestyle='0.'
            if nPro==4:
                linestyle='0.'
            ax2.plot(x1,y1,linestyle,linewidth=0.5)
            for j in range(positions[i]-7,positions[i]+7):
                posicount[j+50]+=1
ax1.bar(range(-50,51),posicount,color='0',linewidth=0)                    
ax3.plot(a3x[1:],range(1,1126),'k')
ax3.set_xlim((1,5))
ax3.set_xticks([2,4])
ax3.set_ylim((1,1125))

with open("C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s5\hbb.csv",'rb') as bfile2:
    reader = csv.reader(bfile2, delimiter=',')
    next(reader, None) #the header
    config=0
    for row in reader:
        nProtein=int(row[1])
        nConfig=int(row[0])
        positions=[0]*nProtein
        for i in range(0,nConfig):#index of configuration
            config+=1
            for j in range(0,nProtein): #index of protein
                positions[j]=int(row[2+j])
                x2=[positions[j]-7,positions[j]+7]
                y2=[config]*len(x2)
                if nProtein==2:
                    linestyle='0.8'
                if nProtein==3:
                    linestyle='0.'
                if nProtein==4:
                    linestyle='0.'
                bx2.plot(x2,y2,linestyle,linewidth=0.5)
bfile3="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s5\hbbpositioncount.csv"
df=pd.read_table(bfile3,sep=',')
count=[0]*101
for i in range(0,101):
    if df['count'][i]!=0:
        for j in range(-7,8):
            if i+j>=0 and i+j<=100:
                count[i+j]=df['count'][i]+count[i+j]
bx1.bar(df['N(bp)'],count,color='0.',linewidth=0)

x=[2]*1123+[3,4]
y=range(1,1126)
bx3.plot(x,y,'k')
bx3.set_xlim((1,5))
bx3.set_xticks([2,4])
bx3.set_ylim((1,1125))

ax1.set_xlim((-50,50))
bx1.set_xlim((-50,50))
ax2.set_xlim((-50,50))
bx2.set_xlim((-50,50))
ax2.set_ylim((0,1130))
bx2.set_ylim((0,1130))
#ax2.set_xticks([1000,1125])
setp(ax2.get_yticklabels(),visible=False)
savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s5\s5.1.png',dpi=600)