import numpy as np
import pandas as pd
import csv
from matplotlib.pyplot import *
import matplotlib.colors as colors
import matplotlib.gridspec as gridspec

fig=figure(figsize=(3.42,5),dpi=600) #is in control
#fig={'figsize':(3.42,5),'dpi':600} #is not in control
font = {'family':'Arial','weight':'normal','size':7} #family is in control for axis labels, size is in control for tick labels only
rc('font', **font)
#rc('figure',**fig)
gs1 = gridspec.GridSpec(1,3)
gs1.update(bottom=0.78, wspace=0.05)
ax1=subplot(gs1[:,0])
ax2=subplot(gs1[:,1])
ax3=subplot(gs1[:,2])
gs2 = gridspec.GridSpec(1,3)
gs2.update(top=0.77, wspace=0.05)
bx1=subplot(gs2[:,0])
bx2=subplot(gs2[:,1])
bx3=subplot(gs2[:,2])

filename1="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s3\protein_bound_probabilities_1per50_80-149.dat" 
df1=pd.read_table(filename1,sep='\t')
#print df
df1['<HU>'] = df1['1HU'] + 2*df1['2HU']+3*df1['3HU']+4*df1['4HU']+5*df1['5HU']+6*df1['6HU']+7*df1['7HU']+8*df1['8HU']
df1['1HU/50']=df1['N(bp)']/float(50)
#print df['<HU>']
#print df['1HU/50']
x=df1['N(bp)']
#print x
p1,=ax1.plot(x,df1['<HU>'],'k')
p2,=ax1.plot(x,df1['1HU/50'],'k:')
#ax1.set_title('numbers of HU proteins',fontsize=7)
#ax1.legend([p1,p2],["<HU>","1HU/50"],loc=4,fontsize=7)


filename="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s3\protein_bound_probabilities_1per50_80-149_weighted_by_J_factor.csv" 
df=pd.read_table(filename,sep=',')
#print df
x=df['N(bp)']
HU2=df['2HUconfig']/float(10000)
HU3=df['3HUconfig']/float(10000)
HU4=df['4HUconfig']/float(10000)

p2=bx1.bar(x,HU2,color='0.8',bottom=HU3+HU4,linewidth=0)
p3=bx1.bar(x,HU3,color='0.',bottom=HU4,linewidth=0)
p4=bx1.bar(x,HU4,color='0.',linewidth=0)


#ax2.set_xlabel('chain length',fontsize=7)
#ax2.set_title('numbers of configurations for 1HU/50bp',fontsize=7)
#ax2.legend((p2[0],p3[0],p4[0]),('2HU','3HU','4HU'),fontsize=7)


#2#############################################3
filename1="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s3\protein_bound_probabilities_1per100_80-149.dat" 
df1=pd.read_table(filename1,sep='\t')
#print df
df1['<HU>'] = df1['1HU'] + 2*df1['2HU']+3*df1['3HU']+4*df1['4HU']+5*df1['5HU']+6*df1['6HU']+7*df1['7HU']+8*df1['8HU']
df1['1HU/100']=df1['N(bp)']/float(100)
#print df['<HU>']
#print df['1HU/100']
x=df1['N(bp)']
#print x
p1,=ax2.plot(x,df1['<HU>'],'k')
p2,=ax2.plot(x,df1['1HU/100'],'k:')
#ax1.set_title('numbers of HU proteins')
#ax1.legend([p1,p2],["<HU>","1HU/100"],loc=4)


filename="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s3\protein_bound_probabilities_1per100_80-149_weighted_by_J_factor.csv" 
df=pd.read_table(filename,sep=',')
#print df
x=df['N(bp)']
HU2=df['2HUconfig']/float(10000)
HU3=df['3HUconfig']/float(10000)
HU4=df['4HUconfig']/float(10000)

p2=bx2.bar(x,HU2,color='0.8',bottom=HU3+HU4,linewidth=0)
p3=bx2.bar(x,HU3,color='0.',bottom=HU4,linewidth=0)
p4=bx2.bar(x,HU4,color='0.',linewidth=0)


#ax2.set_xlabel('chain length')
#ax2.set_title('numbers of configurations for 1HU/100bp')
#ax2.legend((p2[0],p3[0],p4[0]),('2HU','3HU','4HU'))

#3#########################################################################
filename1="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s3\protein_bound_probabilities_1per200_80-149.dat" 
df1=pd.read_table(filename1,sep=',')
#print df
df1['<HU>'] = df1['1HU'] + 2*df1['2HU']+3*df1['3HU']+4*df1['4HU']+5*df1['5HU']+6*df1['6HU']+7*df1['7HU']+8*df1['8HU']
df1['1HU/200']=df1['N(bp)']/float(200)
#print df['<HU>']
#print df['1HU/200']
x=df1['N(bp)']
#print x
p1,=ax3.plot(x,df1['<HU>'],'k')
p2,=ax3.plot(x,df1['1HU/200'],'k:')
#ax1.set_title('numbers of HU proteins')
#ax1.legend([p1,p2],["<HU>","1HU/200"],loc=4)


filename="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s3\protein_bound_probabilities_1per200_80-149_weighted_by_J_factor.csv" 
df=pd.read_table(filename,sep=',')
#print df
x=df['N(bp)']
HU2=df['2HUconfig']/float(10000)
HU3=df['3HUconfig']/float(10000)
HU4=df['4HUconfig']/float(10000)

p2=bx3.bar(x,HU2,color='0.8',bottom=HU3+HU4,linewidth=0)
p3=bx3.bar(x,HU3,color='0.',bottom=HU4,linewidth=0)
p4=bx3.bar(x,HU4,color='0.',linewidth=0)


#ax2.set_xlabel('chain length')
#ax2.set_title('numbers of configurations for 1HU/200bp')
#ax2.legend((p2[0],p3[0],p4[0]),('2HU','3HU','4HU'))
for i in [ax1,ax2,ax3,bx1,bx2,bx3]:
    i.set_xlim((100,150))
    i.set_xticks([105, 126, 147])
for i in [bx1,bx2,bx3]:
    i.set_ylim((0,65))
for i in [ax1,ax2,ax3]:
    i.set_ylim((0,4))
    i.set_yticks([1,2,3])
bx1.text(132, 63,'1/50bp',bbox={'facecolor':'white', 'alpha':1., 'pad':3},fontsize=7)
bx2.text(129, 63,'1/100bp',bbox={'facecolor':'white', 'alpha':1., 'pad':3},fontsize=7)
bx3.text(129, 63,'1/200bp',bbox={'facecolor':'white', 'alpha':1., 'pad':3},fontsize=7)
ax1.set_ylabel('# HU',fontsize=7) #could be controlled by rc.font
bx1.set_ylabel('# configurations'+r'$\mathregular{\times 10^4}$',fontsize=7)
setp(ax1.get_xticklabels()+ax2.get_xticklabels()+ax3.get_xticklabels()+ax2.get_yticklabels()+ax3.get_yticklabels()+bx2.get_yticklabels()+bx3.get_yticklabels(),visible=False)
savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s3\s3',dpi=600)