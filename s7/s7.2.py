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
ax1lim=[-48,-1]
bx1lim=[1,54]
ax1limratio=float(ax1lim[1]-ax1lim[0])/(bx1lim[1]-bx1lim[0]+ax1lim[1]-ax1lim[0])
bx1limratio=float(bx1lim[1]-bx1lim[0])/(bx1lim[1]-bx1lim[0]+ax1lim[1]-ax1lim[0])
gs1 = gridspec.GridSpec(1,2,width_ratios=[ax1limratio,bx1limratio])
gs1.update(left=0.12, right=0.98,top=0.57, bottom=0.17, wspace=0.0,hspace=0.02)
ax1=subplot(gs1[:,0])
bx1=subplot(gs1[:,1])
ax1.set_xlim(ax1lim)
bx1.set_xlim(bx1lim)
ax1.spines['right'].set_visible(False)
bx1.spines['left'].set_visible(False)
ax1.yaxis.tick_left()
bx1.yaxis.tick_right()


ax2lim=[-48,-1]
bx2lim=[1,54]
ax2limratio=float(ax2lim[1]-ax2lim[0])/(bx2lim[1]-bx2lim[0]+ax2lim[1]-ax2lim[0])
bx2limratio=float(bx2lim[1]-bx2lim[0])/(bx2lim[1]-bx2lim[0]+ax2lim[1]-ax2lim[0])
gs2 = gridspec.GridSpec(1,2,width_ratios=[ax2limratio,bx2limratio])
gs2.update(left=0.12, right=0.98,top=0.98, bottom=0.58,wspace=0.0,hspace=0.02)
ax2=subplot(gs2[:,0])
bx2=subplot(gs2[:,1])
ax2.set_xlim(ax2lim)
bx2.set_xlim(bx2lim)
ax2.spines['right'].set_visible(False)
bx2.spines['left'].set_visible(False)
ax2.yaxis.tick_left()
bx2.yaxis.tick_right()

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
p1=ax1.bar(x,HU1,color='#58FA58',label='1HU',linewidth=0)
p2=ax1.bar(x,HU2,color='#F4FA58',bottom=HU1,label='2HU',linewidth=0)
p3=ax1.bar(x,HU3,color='#FA8258',bottom=HU1+HU2,label='3HU',linewidth=0)
pA1=ax2.bar(x,A1,color='#58FA58',label='A1',linewidth=0)
pA2=ax2.bar(x,A2,color='#F4FA58',bottom=A1,label='A2',linewidth=0)
pP1=ax2.bar(x,P1,color='#FA8258',bottom=A1+A2,label='P1',linewidth=0)
pP2=ax2.bar(x,P2,color='#58FAD0',bottom=A1+A2+P1,label='P2',linewidth=0)

p1=bx1.bar(x,HU1,color='#58FA58',label='1HU',linewidth=0)
p2=bx1.bar(x,HU2,color='#F4FA58',bottom=HU1,label='2HU',linewidth=0)
p3=bx1.bar(x,HU3,color='#FA8258',bottom=HU1+HU2,label='3HU',linewidth=0)
pA1=bx2.bar(x,A1,color='#58FA58',label='A1',linewidth=0)
pA2=bx2.bar(x,A2,color='#F4FA58',bottom=A1,label='A2',linewidth=0)
pP1=bx2.bar(x,P1,color='#FA8258',bottom=A1+A2,label='P1',linewidth=0)
pP2=bx2.bar(x,P2,color='#58FAD0',bottom=A1+A2+P1,label='P2',linewidth=0)

majorLocator   = MultipleLocator(2)
majorFormatter = FormatStrFormatter('%d')
ax1.yaxis.set_major_locator(majorLocator)
ax1.yaxis.set_major_formatter(majorFormatter)
ax2.yaxis.set_major_locator(majorLocator)
ax2.yaxis.set_major_formatter(majorFormatter)

bx1.legend(bbox_to_anchor=(0., 1, 1, 0.), loc=1)
bx2.legend(bbox_to_anchor=(0., 1, 1, 0),loc=1)
#fig.legend((p21,p31,p22,p32,p4,p33),('2HU even','3HU equilateral','2HU uneven','3HU isosceles','\t','3HU scalene'), bbox_to_anchor=(0., 0.2, 1, -0.),loc=4,borderpad=0.2,handletextpad=0.)

#ax2.set_xlabel(r'$\mathit{g}$'+'al operon control region',fontsize=8)
ax1.text(-22,-2.2,r'$\mathit{gal}$'+' operon control region',fontsize=8)
ax1.set_ylabel('HU buildup (%)',fontsize=8)
ax2.set_ylabel('HU buildup (%)',fontsize=8)
bx1.set_xticks([1,10,20,30,40])
bx2.set_xticks([1,10,20,30,40])
setp(bx1.get_yticklabels()+bx2.get_yticklabels()+ax2.get_xticklabels()+bx2.get_xticklabels(),visible=False)
savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s7\s7.2.png',dpi=600)