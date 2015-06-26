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
ax1lim=[70,91.5]
bx1lim=[114.5,125.5]
ax1limratio=float(ax1lim[1]-ax1lim[0])/(bx1lim[1]-bx1lim[0]+ax1lim[1]-ax1lim[0])
bx1limratio=float(bx1lim[1]-bx1lim[0])/(bx1lim[1]-bx1lim[0]+ax1lim[1]-ax1lim[0])
gs1 = gridspec.GridSpec(1,2,width_ratios=[ax1limratio,bx1limratio])
gs1.update(left=0.13, right=0.8,top=0.98, bottom=0.73, wspace=0.07,hspace=0.02)
ax1=subplot(gs1[:,0])
bx1=subplot(gs1[:,1])
ax1.set_xlim(ax1lim)
bx1.set_xlim(bx1lim)
ax1.spines['right'].set_visible(False)
bx1.spines['left'].set_visible(False)
ax1.yaxis.tick_left()
bx1.yaxis.tick_right()
ax1.set_yticklabels(ax1.get_yticks(), ha = 'left')
yax = ax1.get_yaxis()
yax.set_tick_params(pad=20)
ax1.set_yscale('log',subsy=[])
bx1.set_yscale('log',subsy=[])
majorLocator   = MultipleLocator(5)
majorFormatter = FormatStrFormatter('%d')
bx1.xaxis.set_major_locator(majorLocator)
bx1.xaxis.set_major_formatter(majorFormatter)
#ax1.get_yaxis().set_major_formatter(matplotlib.ticker.LogFormatter(base=10**2))
#ax1.get_yaxis().set_major_locator(matplotlib.ticker.LogLocator(base=10**2))
#bx1.get_yaxis().set_major_formatter(matplotlib.ticker.LogFormatter(base=10**2))
#bx1.get_yaxis().set_major_locator(matplotlib.ticker.LogLocator(base=10**2))
ax1.set_yticks([1e-10,1e-8,1e-6])
bx1.set_yticks([1e-10,1e-8,1e-6])
ax1.set_xticks([70,75,80,85,90])
bx1.set_xticks([115,120])
ax1.set_ylim((pow(10,-12),pow(10,-3.8)))
setp(bx1.get_yticklabels(),visible=False)


ax2lim=[105,131.5]
bx2lim=[194.5,201.5]
ax2limratio=float(ax2lim[1]-ax2lim[0])/(bx2lim[1]-bx2lim[0]+ax2lim[1]-ax2lim[0])
bx2limratio=float(bx2lim[1]-bx2lim[0])/(bx2lim[1]-bx2lim[0]+ax2lim[1]-ax2lim[0])
gs2 = gridspec.GridSpec(1,2,width_ratios=[ax2limratio,bx2limratio])
gs2.update(left=0.13, right=0.8,top=0.67, bottom=0.42, wspace=0.07,hspace=0.02)
ax2=subplot(gs2[:,0])
bx2=subplot(gs2[:,1])
ax2.set_xlim(ax2lim)
bx2.set_xlim(bx2lim)
ax2.spines['right'].set_visible(False)
bx2.spines['left'].set_visible(False)
ax2.yaxis.tick_left()
bx2.yaxis.tick_right()
ax2.set_yticklabels(ax1.get_yticks(), ha = 'left')
yax = ax2.get_yaxis()
yax.set_tick_params(pad=20)
ax2.set_yscale('log',subsy=[])
bx2.set_yscale('log',subsy=[])
majorLocator   = MultipleLocator(5)
majorFormatter = FormatStrFormatter('%d')
bx2.xaxis.set_major_locator(majorLocator)
bx2.xaxis.set_major_formatter(majorFormatter)
#ax2.get_yaxis().set_major_formatter(matplotlib.ticker.LogFormatter(base=10**2))
#ax2.get_yaxis().set_major_locator(matplotlib.ticker.LogLocator(base=10**2))
#bx2.get_yaxis().set_major_formatter(matplotlib.ticker.LogFormatter(base=10**2))
#bx2.get_yaxis().set_major_locator(matplotlib.ticker.LogLocator(base=10**2))
ax2.set_ylim((1e-13,1e-6))
ax2.set_yticks([1e-12,1e-10,1e-8])
bx2.set_yticks([1e-12,1e-10,1e-8])
setp(bx2.get_yticklabels(),visible=False)


ax3lim=[237,253.5]
bx3lim=[336.5,350.5]
ax3limratio=float(ax3lim[1]-ax3lim[0])/(bx3lim[1]-bx3lim[0]+ax3lim[1]-ax3lim[0])
bx3limratio=float(bx3lim[1]-bx3lim[0])/(bx3lim[1]-bx3lim[0]+ax3lim[1]-ax3lim[0])
gs3 = gridspec.GridSpec(1,2,width_ratios=[ax3limratio,bx3limratio])
gs3.update(left=0.13, right=0.8,top=0.36, bottom=0.11, wspace=0.07,hspace=0.02)
ax3=subplot(gs3[:,0])
bx3=subplot(gs3[:,1])
ax3.set_xlim(ax3lim)
bx3.set_xlim(bx3lim)
ax3.spines['right'].set_visible(False)
bx3.spines['left'].set_visible(False)
ax3.yaxis.tick_left()
bx3.yaxis.tick_right()
ax3.set_yticklabels(ax1.get_yticks(), ha = 'left')
yax = ax3.get_yaxis()
yax.set_tick_params(pad=20)
ax3.set_yscale('log',subsy=[])
bx3.set_yscale('log',subsy=[])
majorLocator   = MultipleLocator(5)
majorFormatter = FormatStrFormatter('%d')
ax3.xaxis.set_major_locator(majorLocator)
ax3.xaxis.set_major_formatter(majorFormatter)
majorLocator   = MultipleLocator(5)
majorFormatter = FormatStrFormatter('%d')
bx3.xaxis.set_major_locator(majorLocator)
bx3.xaxis.set_major_formatter(majorFormatter)
#ax3.get_yaxis().set_major_formatter(matplotlib.ticker.LogFormatter(base=10**1))
#ax3.get_yaxis().set_major_locator(matplotlib.ticker.LogLocator(base=10**1))
#bx3.get_yaxis().set_major_formatter(matplotlib.ticker.LogFormatter(base=10**1))
#bx3.get_yaxis().set_major_locator(matplotlib.ticker.LogLocator(base=10**1))
ax3.set_yticks([1e-8,1e-7])
bx3.set_yticks([1e-8,1e-7])
ax3.set_ylim((1e-9,1e-6))
setp(bx3.get_yticklabels(),visible=False)


file1="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s8\\file1.csv" 
df1=pd.read_table(file1,sep=',')
x1=df1['bp']
HU0=df1['0HU']
HU200=df1['1HU/200']
HU500=df1['1HU/500']
HU1000=df1['1HU/1000']
wt=df1['WT']
TPM_09=df1['TPM_09']
TPM_12=df1['TPM_12']
ax1HU0,=ax1.plot(x1,HU0,'k',linewidth=0.5)
ax1HU200,=ax1.plot(x1,HU200,'r',linewidth=0.5)
ax1HU500,=ax1.plot(x1,HU500,'g',linewidth=0.5)
ax1HU1000,=ax1.plot(x1,HU1000,'b',linewidth=0.5)
ax1wt,=ax1.plot(x1,wt,'k.',markersize=5)
bx1HU0,=bx1.plot(x1,HU0,'k',linewidth=0.5)
bx1TPM_09,=bx1.plot(x1,TPM_09,'k*',fillstyle='none',markersize=5)
bx1TPM_12,=bx1.plot(x1,TPM_12,'k+',markersize=5)
kwargs = dict(color='k', clip_on=False,linewidth=0.8)
ylim = ax1.get_ylim()
dy=(ylim[1]/ylim[0])**0.02
dx=.01*(ax1lim[1]-ax1lim[0])/ax1limratio
ax1.plot((ax1lim[1]-dx,ax1lim[1]+dx),(ylim[0]/dy,ylim[0]*dy), **kwargs)
ax1.plot((ax1lim[1]-dx,ax1lim[1]+dx), (ylim[1]/dy,ylim[1]*dy), **kwargs)
dx=.01*(bx1lim[1]-bx1lim[0])/bx1limratio
bx1.plot((bx1lim[0]-dx,bx1lim[0]+dx),(ylim[0]/dy,ylim[0]*dy), **kwargs)
bx1.plot((bx1lim[0]-dx,bx1lim[0]+dx), (ylim[1]/dy,ylim[1]*dy), **kwargs)
ax1.set_ylim(ylim)
bx1.set_ylim(ylim)

file2="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s8\\file2.csv" 
df2=pd.read_table(file2,sep=',')
x2=df2['bp']
HU0=df2['0HU']
DNA=df2['DNA']
HU600=df2['1HU/600bp']
HU1500=df2['1HU/1500bp']
HU10nM=df2['10 nM HU']
HU4nM=df2['4 nM HU']
ax2HU0,=ax2.plot(x2,HU0,'k',linewidth=0.5)
ax2DNA,=ax2.plot(x2,DNA,'k.',markersize=5)
bx2HU0,=bx2.plot(x2,HU0,'k',linewidth=0.5)
bx2HU600,=bx2.plot(x2,HU600,'m',linewidth=0.5)
bx2HU1500,=bx2.plot(x2,HU1500,'c',linewidth=0.5)
bx2DNA,=bx2.plot(x2,DNA,'k.',markersize=5)
bx2HU10nM,=bx2.plot(x2,HU10nM,'k*',fillstyle='none',markersize=5)
bx2HU4nM,=bx2.plot(x2,HU4nM,'k+',fillstyle='none',markersize=5)
kwargs = dict(color='k', clip_on=False,linewidth=0.8)
ylim = ax2.get_ylim()
dy=(ylim[1]/ylim[0])**0.02
dx=.01*(ax2lim[1]-ax2lim[0])/ax2limratio
ax2.plot((ax2lim[1]-dx,ax2lim[1]+dx),(ylim[0]/dy,ylim[0]*dy), **kwargs)
ax2.plot((ax2lim[1]-dx,ax2lim[1]+dx), (ylim[1]/dy,ylim[1]*dy), **kwargs)
dx=.01*(bx2lim[1]-bx2lim[0])/bx2limratio
bx2.plot((bx2lim[0]-dx,bx2lim[0]+dx),(ylim[0]/dy,ylim[0]*dy), **kwargs)
bx2.plot((bx2lim[0]-dx,bx2lim[0]+dx), (ylim[1]/dy,ylim[1]*dy), **kwargs)
ax2.set_ylim(ylim)
bx2.set_ylim(ylim)

file3="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s8\\file3.csv" 
df3=pd.read_table(file3,sep=',')
x3=df3['bp']
HU0=df3['0HU']
DNA=df3['DNA']
ax3HU0,=ax3.plot(x3,HU0,'k',linewidth=0.5)
ax3DNA,=ax3.plot(x3,DNA,'k.',markersize=5)
bx3HU0,=bx3.plot(x3,HU0,'k',linewidth=0.5)
bx3DNA,=bx3.plot(x3,DNA,'k.',markersize=5)
kwargs = dict(color='k', clip_on=False,linewidth=0.8)
ylim = ax3.get_ylim()
dy=(ylim[1]/ylim[0])**0.02
dx=.01*(ax3lim[1]-ax3lim[0])/ax3limratio
ax3.plot((ax3lim[1]-dx,ax3lim[1]+dx),(ylim[0]/dy,ylim[0]*dy), **kwargs)
ax3.plot((ax3lim[1]-dx,ax3lim[1]+dx), (ylim[1]/dy,ylim[1]*dy), **kwargs)
dx=.01*(bx3lim[1]-bx3lim[0])/bx3limratio
bx3.plot((bx3lim[0]-dx,bx3lim[0]+dx),(ylim[0]/dy,ylim[0]*dy), **kwargs)
bx3.plot((bx3lim[0]-dx,bx3lim[0]+dx), (ylim[1]/dy,ylim[1]*dy), **kwargs)
ax3.set_ylim(ylim)
bx3.set_ylim(ylim)

ax1.legend((ax1HU0,ax1HU200,ax1HU500,ax1HU1000,ax1wt,bx1TPM_09,bx1TPM_12),('0HU','1HU/200','1HU/500','1HU/1000','WT','E8-09','E8-12'),bbox_to_anchor=(2.053, 1.075),borderpad=0.2,labelspacing=0.1,handlelength=1.,handletextpad=0.15,numpoints=1,fontsize=8)
bx1.legend((ax2HU0,ax2DNA,bx2HU600,bx2HU1500,bx2HU10nM,bx2HU4nM),('0HU','DNA','1HU/600','1HU/1500','10nM HU','4nM HU'),bbox_to_anchor=(1.955, -.164),borderpad=0.2,labelspacing=0.1,handlelength=1.,handletextpad=0.15,numpoints=1,fontsize=8)
ax3.legend((ax3HU0,ax3DNA),('0HU','DNA'),bbox_to_anchor=(2.295, 1.08),borderpad=0.2,labelspacing=0.1,handlelength=1.,handletextpad=0.15,numpoints=1,fontsize=8)
ax3.text(248,pow(10,-10),'Chain length (bp)',fontsize=8)
ax3.text(231.5,pow(10,0),r'$\mathit{J}$'+' (M)',rotation='vertical',fontsize=8)
ax3.text(231.5,pow(10,-3.8),r'$\mathit{J}$'+' (M)',rotation='vertical',fontsize=8)
ax3.text(231.5,pow(10,-7.5),r'$\mathit{J}$'+' (M)',rotation='vertical',fontsize=8)
ax3.text(231.5,pow(10,1),'a',fontsize=8)
ax3.text(231.5,pow(10,-2.8),'b',fontsize=8)
ax3.text(231.5,pow(10,-6.5),'c',fontsize=8)


savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s8\s8.1.png',dpi=600)