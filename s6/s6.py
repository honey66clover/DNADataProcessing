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
gs = gridspec.GridSpec(3, 3)
gs.update(wspace=0.05,hspace=0.05)
ax=[0]*9
filename=[0]*9
filename[1]="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s6\PCA_1HUper100.csv"
for i in range(0,9):
    ax[i]=subplot(gs[i])
    ax[i].set_xlim((105,126))
    ax[i].set_ylim((0,60))
    ax[i].set_yticks([10,20,30,40,50])
    ax[i].set_xticks([105,115,126])
width=0.5
for i in range(1,2):
    df=pd.read_table(filename[i],sep=',')
    ax[i].bar(df['N(bp)'],df['PA1_2HU'],width,color='0.8',linewidth=0)
    ax[i].bar(df['N(bp)']+width,df['PA1_3HU'],width,color='0.2',linewidth=0)
    ax[i].plot(df['N(bp)'],df['PA1_all'],'k')
    ax[i+3].bar(df['N(bp)'],df['PA2_2HU'],width,color='0.8',linewidth=0)
    ax[i+3].bar(df['N(bp)']+width,df['PA2_3HU'],width,color='0.2',linewidth=0)
    ax[i+3].plot(df['N(bp)'],df['PA2_all'],'k')
    ax[i+6].bar(df['N(bp)'],df['PA3_2HU'],width,color='0.8',linewidth=0)
    ax[i+6].bar(df['N(bp)']+width,df['PA3_3HU'],width,color='0.2',linewidth=0)
    ax[i+6].plot(df['N(bp)'],df['PA3_all'],'k')
for i in range(0,6):
    setp(ax[i].get_xticklabels(),visible=False)
for i in [1,2,4,5,7,8]:
    setp(ax[i].get_yticklabels(),visible=False)
savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s6\s6_300',dpi=300)