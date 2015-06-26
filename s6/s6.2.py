import numpy as np
import pandas as pd
import csv
from matplotlib.pyplot import *
import matplotlib.colors as colors
import matplotlib.gridspec as gridspec

fig=figure(figsize=(3.42,2.1),dpi=600) #is in control
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


gs = gridspec.GridSpec(3, 3)
gs.update(top=0.90,bottom=0.15,left=0.15, right=0.95,wspace=0.27,hspace=0.00)
ax=[0]*9
filename=[0]*3
filename[0]="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s6\PCA_2HU.csv"
filename[1]="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s6\PCA_3HU.csv"
filename[2]="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s6\PCA_all.csv"
for i in range(0,9):
    ax[i]=subplot(gs[i])
    ax[i].set_xlim((100,129))
    ax[i].set_xticks([105,115,126])
    ax[i].xaxis.set_tick_params(length=1, width=0.5)
    ax[i].yaxis.set_tick_params(length=1.5, width=0.5)

width=0.5
for i in range(0,3):
    df=pd.read_table(filename[i],sep=',')
    ax[i].plot(df['N(bp)'],df['PA1_50bp'],'r',linewidth=0.5)
    ax[i].plot(df['N(bp)'],df['PA1_100bp'],'g',linewidth=0.5)
    ax[i].plot(df['N(bp)'],df['PA1_200bp'],'k',linewidth=0.5)
    ax[i+3].plot(df['N(bp)'],df['PA2_50bp'],'r',linewidth=0.5)
    ax[i+3].plot(df['N(bp)'],df['PA2_100bp'],'g',linewidth=0.5)
    ax[i+3].plot(df['N(bp)'],df['PA2_200bp'],'k',linewidth=0.5)
    p1,=ax[i+6].plot(df['N(bp)'],df['PA3_50bp'],'r',linewidth=0.5)
    p2,=ax[i+6].plot(df['N(bp)'],df['PA3_100bp'],'g',linewidth=0.5)
    p3,=ax[i+6].plot(df['N(bp)'],df['PA3_200bp'],'k',linewidth=0.5)


for i in range(0,6):
    setp(ax[i].get_xticklabels(),visible=False)
for i in [1,2,4,5,7,8]:
    setp(ax[i].get_yticklabels(),visible=False)
for i in range(0,3):
    ax[i].set_ylim((30,60))
    ax[i].set_yticks([40,50])
for i in range(3,6):
    ax[i].set_ylim((20,40))
    ax[i].set_yticks([25,35])
for i in range(6,9):
    ax[i].set_ylim((4,15))
    ax[i].set_yticks([8,12])
    
#ax[8].legend((p1,p2,p3),('1/50bp','1/100bp','1/200bp'),bbox_to_anchor=(0.07, 0.19, 1, -0.2),loc=8, borderpad=0.2,labelspacing=0.1,handletextpad=0.1,fontsize=8)
ax[3].legend((p1,p2,p3),('1/50bp','1/100bp','1/200bp'),bbox_to_anchor=(0.07, 0.45, 1, -0.2),loc=8, borderpad=0.2,labelspacing=0.1,handletextpad=0.1,fontsize=8)
ax[7].set_xlabel('DNA chain length (bp)',fontsize=8)
ax[0].set_ylabel(r'$\mathit{\lambda}_1$'+ur'(\u00c5)',fontsize=8)
ax[3].set_ylabel(r'$\mathit{\lambda}_2$'+ur'(\u00c5)',fontsize=8)
ax[6].set_ylabel(r'$\mathit{\lambda}_3$'+ur'(\u00c5)',fontsize=8)
ax[0].text(110, 64,'2HU',fontsize=8)
ax[1].text(110, 64,'3HU',fontsize=8)
ax[2].text(112, 64,'All',fontsize=8)

savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s6\s6.2.png',dpi=600)