import csv
import numpy as np
from matplotlib.pyplot import *
import matplotlib.gridspec as gridspec
import pandas as pd


fig=figure(figsize=(3.42,2.8),dpi=600) #is in control
#fig={'figsize':(3.42,5),'dpi':600} #is not in control
font = {'family':'Arial','weight':'normal','size':7} #family is in control for axis labels, size is in control for tick labels only
rc('font', **font)

rcParams.update({'font.size': 8,
			     'backend': 'pdf',
			     'axes.labelsize':  8,
			     'text.fontsize':   8,
			     'legend.fontsize': 8,
			     'xtick.labelsize': 8,
			     'ytick.major.pad': 2,
			     'xtick.major.pad': 2,
			     'ytick.labelsize': 8,
'axes.linewidth': .8,
			     'lines.linewidth': .1,
			     'mathtext.fontset': 'custom',
			     'mathtext.default': "regular",
			     'mathtext.rm': "Arial",
			     'mathtext.it': "Arial:italic",
			     'font.sans-serif': "Arial",
			     'font.family': "Arial",
			     'font.style': 'normal',
			     'text.usetex': False,
			     'savefig.dpi': 600,
			     'figure.dpi': 600})

#rc('figure',**fig)
gs1 = gridspec.GridSpec(4, 6)
gs1.update(top=0.95, bottom=0.13, left=-0.10, right=0.49, wspace=0.1,hspace=0.05)
ax1=subplot(gs1[0:1, 2:5])
ax2=subplot(gs1[1:, 2:5])
ax3=subplot(gs1[1:, 5:6])
#ax4=subplot(gs1[1:, 4:5])
#ax4.set_frame_on(False)
#ax4.axis('off')
gs2 = gridspec.GridSpec(4, 6)
gs2.update(top=0.95, bottom=0.13,left=0.55, right=1.14, wspace=0.1,hspace=0.05)
bx1=subplot(gs2[0:1, 0:3])
bx2=subplot(gs2[1:, 0:3])
bx3=subplot(gs2[1:, 3:4])
#bx4=subplot(gs2[1:, 4:5])
#bx4.set_frame_on(False)
#bx4.axis('off')
with open("C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s5\modi_read_protein_positions-minicircle_105_HU+87_1125.csv",'rb') as afile1:
    reader = csv.reader(afile1, delimiter=',')
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
            for j in range(positions[i]-7,positions[i]+7):
                posicount[j+50]+=1
            #posicount[(positions[i]-7)]+=1
for k in range(0,len(posicount)):
    posicount[k]=posicount[k]/float(2297*15)
ax1.bar(range(-50,51),posicount,width=1,color='0',linewidth=0)                    

with open("C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s5\\250\HU105position_250.csv",'rb') as afile2:
    reader = csv.reader(afile2, delimiter=',')
    config=0
    for row in reader:
        nPro=int(row[1])
        config+=1
        for i in range(0,nPro):
            positions=[0]*nPro
            positions[i]=int(row[2+i])
            x1=[positions[i]-7,positions[i]+7]
            y1=[config]*len(x1)
            if nPro==2:
                linestyle='0.8'
            if nPro==3:
                linestyle='0.'
            if nPro==4:
                linestyle='0.'
            ax2.plot(x1,y1,linestyle,linewidth=0.6)
               
ax3.plot([2]*236+[3]*12+[4]*2,range(1,251),'k',linewidth=0.5)


with open("C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s5\\250\hbb.csv",'rb') as bfile2:
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
                bx2.plot(x2,y2,linestyle,linewidth=0.6)
bfile3="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s5\hbbpositioncount.csv"
df=pd.read_table(bfile3,sep=',')
count=[0]*101
for i in range(0,101):
    if df['count'][i]!=0:
        for j in range(-7,8):
            if i+j>=0 and i+j<=100:
                count[i+j]=df['count'][i]+count[i+j]
for k in range(0,len(count)):
   count[k]=count[k]/float(2253*15)
bx1.bar(df['N(bp)'],count,width=1,color='0.',linewidth=0)

x=[2]*250
y=range(1,251)
bx3.plot(x,y,'k',linewidth=0.5)

ax1.set_xlim((-50,50))
bx1.set_xlim((-50,50))
ax2.set_xlim((-50,50))
bx2.set_xlim((-50,50))
ax2.set_ylim((0,253))
bx2.set_ylim((0,253))
ax3.set_xlim((1,5))
ax3.set_xticks([2,4])
ax3.set_ylim((1,253))
bx3.set_xlim((1,5))
bx3.set_xticks([2,4])
bx3.set_ylim((1,253))

ax1.yaxis.tick_right()
#ax1.set_yticks([0.1,0.3,0.5])
ax1.set_yticks([0.01,0.02,0.03])
ax1.set_ylabel(r'$\mathit{w}_\mathregular{HU}$',fontsize=8)
bx1.yaxis.tick_right()
#bx1.set_yticks([0.1,0.3,0.5])
bx1.set_yticks([0.01,0.02,0.03])
bx1.set_ylabel(r'$\mathit{w}_\mathregular{Hbb}$',fontsize=8)
ax2.yaxis.set_ticks_position('none')
bx2.yaxis.set_ticks_position('none')
ax3.yaxis.set_ticks_position('none')
bx3.yaxis.set_ticks_position('none')
ax2.xaxis.set_ticks_position('bottom')
bx2.xaxis.set_ticks_position('bottom')
ax3.xaxis.set_ticks_position('bottom')
bx3.xaxis.set_ticks_position('bottom')

ax2.set_ylabel('Sampled configurations',fontsize=8)
ax2.set_xlabel('Nucleotide position',fontsize=8)
bx2.set_xlabel('Nucleotide position',fontsize=8)
ax3.set_xlabel('HU #',fontsize=8)
bx3.set_xlabel('Hbb #',fontsize=8)
#ax2.set_xticks([1000,1125])
setp(ax2.get_yticklabels()+bx2.get_yticklabels()+ax3.get_yticklabels()+bx3.get_yticklabels(),visible=False)
savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s5\\250\s5.2.png',dpi=600)