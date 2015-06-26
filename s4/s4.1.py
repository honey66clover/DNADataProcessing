#import csv
from matplotlib.pyplot import *
import pandas as pd
import matplotlib.gridspec as gridspec

fig=figure(figsize=(3.42,2.8),dpi=600) #is in control
#fig={'figsize':(3.42,5),'dpi':600} #is not in control
font = {'family':'Arial','weight':'normal','size':7} #is in control
rc('font', **font)
#rc('figure',**fig)
gs1 = gridspec.GridSpec(3, 1)
gs1.update(left=0.12, right=0.88,top=0.98, bottom=0.25, wspace=0.05,hspace=0.02)
ax1=subplot(gs1[0, :])
ax2=subplot(gs1[1, :])
ax3=subplot(gs1[2, :])

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

filename="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s4\HU-bound DNA shape_1per50_100-149.csv" 
df=pd.read_table(filename,sep=',')
#print df
x=df['HU/50bp']
HU2even=df['2HU even']
HU2uneven=df['2HU uneven']
HU3equi=df['3HU equilateral']
HU3iso=df['3HU isosceles']
HU3scal=df['3HU scalene']
HU4=df['4HU or more']
p21=ax1.bar(x,HU2even,color='0',label='2HU even',linewidth=0)
p22=ax1.bar(x,HU2uneven,color='0.3',bottom=HU2even,label='2HU uneven',linewidth=0)
p31=ax1.bar(x,HU3equi,color='r',bottom=HU2even+HU2uneven,label='3HU equilateral',linewidth=0)
p32=ax1.bar(x,HU3iso,color='0.5',bottom=HU2even+HU2uneven+HU3equi,label='3HU isosceles',linewidth=0)
p33=ax1.bar(x,HU3scal,color='0.8',bottom=HU2even+HU2uneven+HU3equi+HU3iso,label='3HU scalene',linewidth=0)
p4=ax1.bar(x,HU4,color='1',bottom=HU2even+HU2uneven+HU3equi+HU3iso+HU3scal,label='3HU scalene',linewidth=0)
#title('probabilities of different shapes for 1per50')
#legend((p21[0],p22[0],p31[0],p32[0],p33[0]),('2HU even','2HU uneven','3HU equilateral','3HU isosceles','3HU scalene'))
#legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,prop={'size':10})
#legend(bbox_to_anchor=(0., 0, 1, .102), loc=3,ncol=5, mode="expand",borderaxespad=0.)

filename="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s4\HU-bound DNA shape_1per100_100-149.csv" 
df=pd.read_table(filename,sep=',')
#print df
x=df['HU/100bp']
HU2even=df['2HU even']
HU2uneven=df['2HU uneven']
HU3equi=df['3HU equilateral']
HU3iso=df['3HU isosceles']
HU3scal=df['3HU scalene']
HU4=df['4HU or more']
p21=ax2.bar(x,HU2even,color='0',label='2HU even',linewidth=0)
p22=ax2.bar(x,HU2uneven,color='0.3',bottom=HU2even,label='2HU uneven',linewidth=0)
p31=ax2.bar(x,HU3equi,color='r',bottom=HU2even+HU2uneven,label='3HU equilateral',linewidth=0)
p32=ax2.bar(x,HU3iso,color='0.5',bottom=HU2even+HU2uneven+HU3equi,label='3HU isosceles',linewidth=0)
p33=ax2.bar(x,HU3scal,color='0.8',bottom=HU2even+HU2uneven+HU3equi+HU3iso,label='3HU scalene',linewidth=0)
p4=ax2.bar(x,HU4,color='1',bottom=HU2even+HU2uneven+HU3equi+HU3iso+HU3scal,label='3HU scalene',linewidth=0)

filename="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s4\HU-bound DNA shape_1per200_100-149.csv" 
df=pd.read_table(filename,sep=',')
#print df
x=df['HU/200bp']
HU2even=df['2HU even']
HU2uneven=df['2HU uneven']
HU3equi=df['3HU equilateral']
HU3iso=df['3HU isosceles']
HU3scal=df['3HU scalene']
HU4=df['4HU or more']
p21=ax3.bar(x,HU2even,color='0',label='2HU even',linewidth=0)
p22=ax3.bar(x,HU2uneven,color='0.3',bottom=HU2even,label='2HU uneven',linewidth=0)
p31=ax3.bar(x,HU3equi,color='r',bottom=HU2even+HU2uneven,label='3HU equilateral',linewidth=0)
p32=ax3.bar(x,HU3iso,color='0.5',bottom=HU2even+HU2uneven+HU3equi,label='3HU isosceles',linewidth=0)
p33=ax3.bar(x,HU3scal,color='0.8',bottom=HU2even+HU2uneven+HU3equi+HU3iso,label='3HU scalene',linewidth=0)
p4=ax2.bar(x,HU4,color='1',bottom=HU2even+HU2uneven+HU3equi+HU3iso+HU3scal,label='3HU scalene',linewidth=0)

#fig.legend(bbox_to_anchor=(0., -0., 1, -0.), loc=8,ncol=3, mode="expand",borderaxespad=0.)
fig.legend((p21,p31,p22,p32,p4,p33),('2HU even','3HU equilateral','2HU uneven','3HU isosceles','\t','3HU scalene'),bbox_to_anchor=(0., 0., 1, -0.6),loc=8,ncol=3,borderpad=0.2,handletextpad=0.,columnspacing=0.5)
#fig.legend((p21,p31,p22,p32,p4,p33),('2HU even','3HU equilateral','2HU uneven','3HU isosceles','\t','3HU scalene'), bbox_to_anchor=(0., 0.2, 1, -0.),loc=4,borderpad=0.2,handletextpad=0.)
setp(ax1.get_xticklabels() + ax2.get_xticklabels(),visible=False)
ax1.set_yticks([0,0.2,0.4,0.6,0.8])
ax2.set_yticks([0,0.2,0.4,0.6,0.8])
ax3.set_yticks([0,0.2,0.4,0.6,0.8])
ax1.set_ylim((0,1))
ax2.set_ylim((0,1))
ax3.set_ylim((0,1))
ax1.set_xticks([105,115,126,136,147])
ax2.set_xticks([105,115,126,136,147])
ax3.set_xticks([105,115,126,136,147])
ax1.set_ylabel(r'$\mathit{f}_\mathsf{HU}$',fontsize=8)
ax2.set_ylabel(r'$\mathit{f}_\mathsf{HU}$',fontsize=8)
ax3.set_ylabel(r'$\mathit{f}_\mathsf{HU}$',fontsize=8)
ax3.set_xlabel('DNA chain length (bp)',fontsize=8)
ax1.text(103.4, 0.06,'1/50bp',bbox={'facecolor':'white', 'alpha':1., 'pad':2},fontsize=8)
ax2.text(103.4, 0.06,'1/100bp',bbox={'facecolor':'white', 'alpha':1., 'pad':2},fontsize=8)
ax3.text(103.4, 0.06,'1/200bp',bbox={'facecolor':'white', 'alpha':1., 'pad':2},fontsize=8)
savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s4\s4.1.png',dpi=600)