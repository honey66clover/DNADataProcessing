# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import csv
from matplotlib.pyplot import *
import matplotlib.colors as colors
import matplotlib.gridspec as gridspec

fig=figure(figsize=(3.42,1.8),dpi=600) #is in control
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
			 
gs2 = gridspec.GridSpec(1, 1)
gs2.update(top=1.02, bottom=0.87, left=0.085, right=0.98, wspace=0.05,hspace=0.05)
bx=subplot(gs2[:, :])
gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.87, bottom=0.18, left=0.085, right=0.98, wspace=0.05,hspace=0.05)
ax=subplot(gs1[:, :])
rfile="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig6\\file re gal loops with HU.csv" 
df=pd.read_table(rfile,sep=',')
bp=df['bp']
MC=df['MC']
prob=df['Prob']

dot=df['Aki/Adhya']
ax.bar(bp,prob,color='0.',linewidth=0)
bx.plot(bp,1*dot/30,'k.',markersize=1)
bx.plot(bp[54:66],1*dot[54:66]/50,'k.',markersize=4)
bx.plot(bp[71:83],1*dot[71:83]/50,'k.',markersize=4)
bx.plot(bp[66],1,'k.',markersize=9)

majorLocator   = MultipleLocator(1)
majorFormatter = FormatStrFormatter('%s')
ax.xaxis.set_major_locator(majorLocator)
ax.xaxis.set_major_formatter(majorFormatter)
#ax.xaxis.set_ticks_position('bottom')
#ax.set_ylim((0,105))
ax.set_xlim((48,100))
bx.set_ylim((0,1.5))
bx.set_xlim((48,100))
bx.set_frame_on(False)
bx.axis('off')

#bx.yaxis.set_label_coords(-0.02, 0.5)
bx.arrow(61,0.15,5.5,0,head_width=0.2, head_length=0.5, fc='k', ec='k')
bx.arrow(66,0.15,-4.5,0,head_width=0.2, head_length=0.5, fc='k', ec='k')
bx.arrow(56,0.35,5.5,0,head_width=0.2, head_length=0.5, fc='k', ec='k')
bx.arrow(61,0.35,-4.5,0,head_width=0.2, head_length=0.5, fc='k', ec='k')
bx.text(62.5, 0.25,r'$\mathit{P1}$',fontsize=8)
bx.text(57.5, 0.45,r'$\mathit{P2}$',fontsize=8)
bx.text(44, 0.8,'Exp',fontsize=8)
seq=[x.upper() for x in df['seq'][46:].tolist()]
#sites=[str(int(x)) for x in df['sites'][46:100].tolist()]

sites=['','','','','-10','','','','','-5','','','','','1','','','','5','','','','','10','','','','','15','','','','','20','','','','','25','','','','','30','','','','','35','','','','','40']
xlabels = [i+'\n'+j for i, j in zip(seq, sites)]
ax.set_xticklabels(xlabels,fontsize=7)
#ylabels=['0','20','40','60','80','100','']
#ax.set_yticklabels(ylabels)
ax.set_ylabel('HU buildup (%)',fontsize=8)
majorLocator   = MultipleLocator(2)
majorFormatter = FormatStrFormatter('%d')
ax.yaxis.set_major_locator(majorLocator)
ax.yaxis.set_major_formatter(majorFormatter)
#ax1.set_yticks([1e-10,1e-8,1e-6])
#ax.set_xlabel(r'$\mathit{gal}$'+' operon control region',fontsize=8)
ax.text(64, -2.1,r'$\mathit{gal}$'+' operon control region',fontsize=8)
ax.xaxis.set_label_coords(0.5, -0.11)
ax.yaxis.set_label_coords(-0.05, 0.5)

savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig6\\fig6.1.png',dpi=600)