import numpy as np
import pandas as pd
import csv,Image
from matplotlib.pyplot import *
import matplotlib.colors as colors
import matplotlib.gridspec as gridspec

fig=figure(figsize=(3.42,2.1),dpi=600) #is in control
#fig={'figsize':(3.42,5),'dpi':600} #is not in control
font = {'family':'Arial','weight':'normal','size':7} #is in control
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
			     
			     
gs1 = gridspec.GridSpec(1, 4)
gs1.update(top=0.98,bottom=0.12,wspace=0.,hspace=0.0)
ax=[0]*4
ax[0]=subplot(gs1[0])
ax[1]=subplot(gs1[1])
ax[2]=subplot(gs1[2])
ax[3]=subplot(gs1[3])
for i in range(0,4):
    ax[i].set_frame_on(False)
    ax[i].axis('off')
    ax[i].set_ylim((0,400))
    ax[i].set_xlim((150,450))

ima0 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s1\Luke\structure-145bp-ID0_B0-2.png')
ax[0].imshow(ima0)
ax[0].text(250, -40,'2HU\n40%',fontsize=8)
ima1 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s1\Luke\structure-145bp-ID0_B0-1.png')
ax[1].imshow(ima1)
ax[1].text(250, -40,'3HU\n16%',fontsize=8)
ima2 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s1\Luke\structure-145bp-ID0_B0-4.png')
ax[2].imshow(ima2)
ax[2].text(250, -40,'4HU\n42%',fontsize=8)
ax[2].text(80, -100,'145bp',fontsize=8)
ima3 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s1\Luke\structure-145bp-ID0_B0-89.png')
ax[3].imshow(ima3)
ax[3].text(250, -40,'5HU\n2%',fontsize=8)

fig.savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s1\s1.1.png', dpi=600)
