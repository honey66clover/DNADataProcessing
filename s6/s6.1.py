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
filename[0]="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s6\PCA_1HUper50.csv"
filename[1]="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s6\PCA_1HUper100.csv"
filename[2]="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s6\PCA_1HUper200.csv"
for i in range(0,9):
    ax[i]=subplot(gs[i])
    ax[i].set_xlim((100,129))
    ax[i].set_ylim((0,60))
    ax[i].set_yticks([10,30,50])
    ax[i].set_xticks([105,115,126])
    ax[i].xaxis.set_tick_params(length=1, width=0.5)
    ax[i].yaxis.set_tick_params(length=1.5, width=0.5)

width=0.5
for i in range(0,3):
    df=pd.read_table(filename[i],sep=',')
    ax[i].bar(df['N(bp)'],df['PA1_2HU'],width,color='0.8',linewidth=0)
    ax[i].bar(df['N(bp)']+width,df['PA1_3HU'],width,color='0.2',linewidth=0)
    ax[i].plot(df['N(bp)'],df['PA1_all'],'k',linewidth=0.5)
    ax[i+3].bar(df['N(bp)'],df['PA2_2HU'],width,color='0.8',linewidth=0)
    ax[i+3].bar(df['N(bp)']+width,df['PA2_3HU'],width,color='0.2',linewidth=0)
    ax[i+3].plot(df['N(bp)'],df['PA2_all'],'k',linewidth=0.5)
    p2=ax[i+6].bar(df['N(bp)'],df['PA3_2HU'],width,color='0.8',linewidth=0)
    p3=ax[i+6].bar(df['N(bp)']+width,df['PA3_3HU'],width,color='0.2',linewidth=0)
    p1,=ax[i+6].plot(df['N(bp)'],df['PA3_all'],'k',linewidth=0.5)


for i in range(0,6):
    setp(ax[i].get_xticklabels(),visible=False)
for i in [1,2,4,5,7,8]:
    setp(ax[i].get_yticklabels(),visible=False)

ax[8].legend((p2[0],p3[0],p1),('2HU','3HU','all'),bbox_to_anchor=(0.18, 0.19, 1, -0.2),loc=8, borderpad=0.2,labelspacing=0.1,handletextpad=0.1,fontsize=8)
ax[7].set_xlabel('DNA chain length (bp)',fontsize=8)
ax[0].set_ylabel(r'$\mathit{\lambda}_1$'+ur'(\u00c5)',fontsize=8)
ax[3].set_ylabel(r'$\mathit{\lambda}_2$'+ur'(\u00c5)',fontsize=8)
ax[6].set_ylabel(r'$\mathit{\lambda}_3$'+ur'(\u00c5)',fontsize=8)
ax[0].text(107, 64,'1/50bp',fontsize=8)
ax[1].text(107, 64,'1/100bp',fontsize=8)
ax[2].text(107, 64,'1/200bp',fontsize=8)

savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s6\s6.1.png',dpi=600)