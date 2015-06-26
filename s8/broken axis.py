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
ax1lim=[70,90]
bx1lim=[115,125]
ax1limratio=float(ax1lim[1]-ax1lim[0])/(bx1lim[1]-bx1lim[0]+ax1lim[1]-ax1lim[0])
bx1limratio=float(bx1lim[1]-bx1lim[0])/(bx1lim[1]-bx1lim[0]+ax1lim[1]-ax1lim[0])
gs1 = gridspec.GridSpec(1,2,width_ratios=[ax1limratio,bx1limratio])
gs1.update(left=0.12, right=0.88,top=0.98, bottom=0.25, wspace=0.05,hspace=0.02)
ax1=subplot(gs1[:,0])
bx1=subplot(gs1[:,1])
ax1.set_xlim(ax1lim)
bx1.set_xlim(bx1lim)

ax1.spines['right'].set_visible(False)
bx1.spines['left'].set_visible(False)
ax1.tick_params(labelright='off',right='off')
bx1.tick_params(labelleft='off',left='off')

kwargs = dict(color='k', clip_on=False,linewidth=0.8)
ylim = ax1.get_ylim()
dy=.01*(ylim[1]-ylim[0])
dx=.01*(ax1lim[1]-ax1lim[0])/ax1limratio
ax1.plot((ax1lim[1]-dx,ax1lim[1]+dx),(ylim[0]-dy,ylim[0]+dy), **kwargs)
ax1.plot((ax1lim[1]-dx,ax1lim[1]+dx), (ylim[1]-dy,ylim[1]+dy), **kwargs)
dx=.01*(bx1lim[1]-bx1lim[0])/bx1limratio
bx1.plot((bx1lim[0]-dx,bx1lim[0]+dx),(ylim[0]-dy,ylim[0]+dy), **kwargs)
bx1.plot((bx1lim[0]-dx,bx1lim[0]+dx), (ylim[1]-dy,ylim[1]+dy), **kwargs)

ax1.set_ylim(ylim)
bx1.set_ylim(ylim)

majorLocator   = MultipleLocator(5)
majorFormatter = FormatStrFormatter('%d')
bx1.xaxis.set_major_locator(majorLocator)
bx1.xaxis.set_major_formatter(majorFormatter)
savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s8\s8.1.png',dpi=600)