#import csv
from matplotlib.pyplot import *
import pandas as pd
import matplotlib.gridspec as gridspec

fig=figure(figsize=(3.42,2.8),dpi=600) #is in control
#fig={'figsize':(3.42,5),'dpi':600} #is not in control
font = {'family':'Arial','weight':'normal','size':7} #is in control
rc('font', **font)
#rc('figure',**fig)
gs1 = gridspec.GridSpec(2, 1)
gs1.update(left=0.15, right=0.95,top=0.98, bottom=0.12, wspace=0.05,hspace=0.02)
ax1=subplot(gs1[0, :])
ax2=subplot(gs1[1, :])

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

filename="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s7\hu binding position.csv" 
df=pd.read_table(filename,sep=',')
#print df
x=df['HU_center']
HU1=df['1 HU']
HU2=df['2 HU']
HU3=df['3 HU']
A1=df['A1']
A2=df['A2']
P1=df['P1']
P2=df['P2']
p1=ax1.bar(x,HU1,color='0',label='1HU',linewidth=0)
p2=ax1.bar(x,HU2,color='0.3',bottom=HU1,label='2HU',linewidth=0)
p3=ax1.bar(x,HU3,color='0.6',bottom=HU1+HU2,label='3HU',linewidth=0)
pA1=ax2.bar(x,A1,color='0',label='A1',linewidth=0)
pA2=ax2.bar(x,A2,color='0.3',bottom=A1,label='A2',linewidth=0)
pP1=ax2.bar(x,P1,color='0.6',bottom=A1+A2,label='P1',linewidth=0)
pP2=ax2.bar(x,P2,color='0.8',bottom=A1+A2+P1,label='P2',linewidth=0)
#title('probabilities of different shapes for 1per50')
#legend((p21[0],p22[0],p31[0],p32[0],p33[0]),('2HU even','2HU uneven','3HU equilateral','3HU isosceles','3HU scalene'))
#legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,prop={'size':10})
#legend(bbox_to_anchor=(0., 0, 1, .102), loc=3,ncol=5, mode="expand",borderaxespad=0.)
majorLocator   = MultipleLocator(2)
majorFormatter = FormatStrFormatter('%d')
ax1.yaxis.set_major_locator(majorLocator)
ax1.yaxis.set_major_formatter(majorFormatter)
ax2.yaxis.set_major_locator(majorLocator)
ax2.yaxis.set_major_formatter(majorFormatter)

#xlabels=['','','','','-50','','','','','','','','','','-40','','','','','','','','','','-30','','','','','','','','','','-20','','','','','','','','','','-10','','','','','-5','','','','','1','','','','','','','','','10','','','','','15','','','','','20','','','','','25','','','','','30','','','','','35','','','','','40','','','','','','','','','','50']
#ax2.set_xticklabels(xlabels,fontsize=7)

ax1.legend(bbox_to_anchor=(0., 1, 1, 0.), loc=1)
ax2.legend(bbox_to_anchor=(0., 1, 1, 0),loc=1)
#fig.legend((p21,p31,p22,p32,p4,p33),('2HU even','3HU equilateral','2HU uneven','3HU isosceles','\t','3HU scalene'), bbox_to_anchor=(0., 0.2, 1, -0.),loc=4,borderpad=0.2,handletextpad=0.)
setp(ax1.get_xticklabels(),visible=False)
ax1.set_xlim((-54,48))
ax2.set_xlim((-54,48))
ax2.set_xlabel(r'$\mathit{g}$'+'al operon control region',fontsize=8)
ax1.set_ylabel('HU buildup (%)',fontsize=8)
ax2.set_ylabel('HU buildup (%)',fontsize=8)
savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s7\s7.1.png',dpi=600)