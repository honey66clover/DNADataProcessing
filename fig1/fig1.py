# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import csv
from matplotlib.pyplot import *
import matplotlib.colors as colors
import matplotlib.gridspec as gridspec

fig=figure(figsize=(3.42,2.8),dpi=600) #is in control
#fig={'figsize':(3.42,5),'dpi':600} #is not in control
font = {'family':'Arial','weight':'normal','size':7} #family is in control for axis labels, size is in control for tick labels only
rc('font', **font)
#rc('figure',**fig)
gs1 = gridspec.GridSpec(4, 1)
gs1.update(left=0.12, right=0.42, wspace=0.05,hspace=0.05)
ax1=subplot(gs1[0:1, :])
ax2=subplot(gs1[1:, :])
gs2 = gridspec.GridSpec(4, 6)
gs2.update(left=0.48, right=1., hspace=0.05)
bx1=subplot(gs2[0:1, 0:3])
bx2=subplot(gs2[1:, 0:3])
bx3=subplot(gs2[1:, 3:4])
bx4=subplot(gs2[1:, 4:5])

filea1="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig1\protein_bound_probabilities_1per100_80-149.dat" 
df1=pd.read_table(filea1,sep='\t')
#print df
df1['<HU>'] = df1['1HU'] + 2*df1['2HU']+3*df1['3HU']+4*df1['4HU']+5*df1['5HU']+6*df1['6HU']+7*df1['7HU']+8*df1['8HU']
df1['1HU/50']=df1['N(bp)']/float(50)
#print df['<HU>']
#print df['1HU/50']
x=df1['N(bp)']
#print x
p1,=ax1.plot(x[20:],df1['<HU>'][20:],'k')
p2,=ax1.plot(x[20:],df1['1HU/50'][20:],'k:')
ax1.set_ylabel('# HU',fontsize=7) #could be controlled by rc.font
ax1.legend([p1,p2],["circle","all"],loc=4,fontsize=7)#not controlled by rc.font
ax1.set_ylim((1,3.5))
majorLocator   = MultipleLocator(1)
majorFormatter = FormatStrFormatter('%d')
minorLocator   = MultipleLocator(0.5)
ax1.yaxis.set_major_locator(majorLocator)
ax1.yaxis.set_major_formatter(majorFormatter)
ax1.yaxis.set_minor_locator(minorLocator)
ax1.set_xticks([105, 126, 147])
setp(ax1.get_xticklabels(),visible=False)
ax1.text(88, 3.6,'A',fontsize=7)
ax1.text(153, 3.6,'B',fontsize=7)

filea2="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig1\protein_bound_probabilities_1per100_80-149_weighted by J factor.csv" 
df=pd.read_table(filea2,sep=',')
#print df
x=df['N(bp)'][20:]
HU2=df['2HUconfig'][20:]/float(10000)
HU3=df['3HUconfig'][20:]/float(10000)
HU4=df['4HUconfig'][20:]/float(10000)

p2=ax2.bar(x,HU2,color='0.8',bottom=HU3+HU4,linewidth=0)
p3=ax2.bar(x,HU3,color='0.',bottom=HU4,linewidth=0)
p4=ax2.bar(x,HU4,color='0.',linewidth=0)

ax2.set_xlabel('DNA chain length (bp)',fontsize=7)
ax2.set_xticks([105, 126, 147])
ax2.set_ylabel('# configurations'+r'$\mathregular{\times 10^4}$',fontsize=7)
ax2.legend((p2[0],p3[0]),('2HU',r'$\mathregular{\geqslant}$'+'3HU','4HU'),fontsize=7)
ax2.set_yticks([0,5,10,15,20,25])

fileb="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig1\\105profile_250.csv" 
with open(fileb,'rb') as rfile:
    reader = csv.reader(rfile, delimiter=',')
    next(reader, None) #the header
    config=0 #index of configuration
    posi2=[]
    posi3=[]
    posi4=[]
    nProteins=[]
    pca1s=[]
    pca2s=[]
    for row in reader:
        config+=1
	Seed1=row[1] 
	Seed2=row[2]
	nPro=int(row[3])
        pca1=float(row[4])
        pca2=float(row[5])
        pca3=float(row[6])
        positions=[0]*nPro #for each configuration
        if nPro==2:
            linestyle='0.8'
        if nPro==3:
            linestyle='0.'
        if nPro==4:
            linestyle='0.'
        nProteins.append(nPro)

        pca1s.append(pca1)
        pca2s.append(pca2)
        
        bx2.set_xlim((0,105))
        bx2.set_xticks([25, 50, 75])
        bx2.set_xlabel('Nucleotide position',fontsize=7)
        bx2.set_ylabel('Sampled configurations',fontsize=7)
        #bx2.get_yaxis().set_visible(False)
        for i in range(0,nPro):
            positions[i]=int(row[7+i])
            x2=range(positions[i],positions[i]+14)
            y2=[config]*len(x2)
            bx2.plot(x2,y2,linestyle,linewidth=0.5)
                        
fileb1="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig1\protein_positions-minicircle_105_HU+87.dat" 
with open(fileb1,'rb') as rfile:
    reader = csv.reader(rfile, delimiter=',')
    next(reader, None) #the header
    posicount=[0]*106 #counts for all configurations
    count=0
    for row in reader:
        posicount[int(row[6])+7]+=1 #mid basepair of the HU
        count+=1
    for i in range(0,106):
        posicount[i]=posicount[i]/float(count)
bx1.set_xlim((0,105))
bx1.set_xticks([25, 50, 75])
setp(bx1.get_xticklabels(),visible=False)
x1=range(0,106)   
bx1.bar(x1,posicount,color='0.8')
bx1.yaxis.tick_right()
bx1.set_yticks([0.005,0.010,0.015])
bx1.set_ylabel(r'$w_\mathregular{HU}$',fontsize=7)
#bx1.yaxis.set_label_position("right")
#bx1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#bx1.set_yticks([0,100,200])

x3=nProteins
y3=range(1,251)
bx3.plot(x3,y3,color='k')
bx3.set_xlim((1,5))
bx3.set_xticks([2,4])
bx3.set_xlabel('HU #',fontsize=7)
bx3.get_yaxis().set_visible(False)

y4=range(1,251)
bx4.plot(pca1s,y4,color='k')
#bx4.scatter(pca2s,y4,c='0.2',s=0.1)
bx4.set_ylim((1,250))
bx4.set_xticks([40,60])
bx4.set_xlabel(r'$\lambda_1(\AA)$',fontsize=7)
#bx4.set_ylabel('Sampled configurations',fontsize=7)
#bx4.yaxis.set_label_position("right")
#bx4.yaxis.tick_right()
# make some labels invisible
setp(bx3.get_yticklabels() + bx2.get_yticklabels() + bx4.get_yticklabels(),visible=False)


#show()
savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig1\\fig1.1.png',dpi=600)