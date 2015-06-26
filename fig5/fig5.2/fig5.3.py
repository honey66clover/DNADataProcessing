import numpy as np
import pandas as pd
import csv,Image
from matplotlib.pyplot import *
import matplotlib.colors as colors
import matplotlib.gridspec as gridspec

fig=figure(figsize=(3.42,3.1),dpi=600) #is in control
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

gs1 = gridspec.GridSpec(1, 4,width_ratios=[38,36,31,41])
gs1.update(top=1.0, bottom=0.55,left=0.,right=1.,wspace=0.,hspace=0.0)
ax=[0]*4
for i in range(0,4):
    ax[i]=subplot(gs1[:,i])
    ax[i].set_frame_on(False)
    ax[i].axis('off')
    ax[i].set_ylim((550,0))
    ax[i].set_xlim((400,800))

gs2 = gridspec.GridSpec(1, 4,width_ratios=[38,36,31,41])
gs2.update(top=0.55, bottom=0.1,left=0.,right=1., wspace=0.,hspace=0.)
bx=[0]*4
for i in range(0,4):
    bx[i]=subplot(gs2[:,i])
    bx[i].set_frame_on(False)
    bx[i].axis('off')
    bx[i].set_ylim((550,0))
    bx[i].set_xlim((400,800))

ima0 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig5\\fig5.2\lacA1.1.png')
ax[0].imshow(ima0)
#ax[0].text(600, 30,'Lac',fontsize=8)
ima1 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig5\\fig5.2\lacP1.1.png')
ax[1].imshow(ima1)

#ax[1].set_ylim((570,-30))
ima2 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig5\\fig5.2\galP1.1.png')
ax[2].imshow(ima2)

#ax[2].set_ylim((570,-30))
#ax[2].text(600, 0,'Gal',fontsize=8)
ima3 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig5\\fig5.2\galA1.1.png')
ax[3].imshow(ima3)


ima5 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig5\\fig5.2\lacA1.2.png')
bx[0].imshow(ima5)

#bx[0].arrow(420,115,-30,0,width=0.5)
#bx[0].text(135, -10,'Hbb'+r'$_{1}$'+'\nHbb'+r'$_{2}$',fontsize=8)

#bx[0].text(135, 760,'A',fontsize=8)
#bx[0].text(135, 330,'B',fontsize=8)
ima6 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig5\\fig5.2\lacP1.2.png')
bx[1].imshow(ima6)
#bx[1].set_ylim((570,-30))
#bx[1].arrow(420,190,-30,0,width=0.5)

ima7 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig5\\fig5.2\\galP1.2.png')
bx[2].imshow(ima7)
#bx[2].set_ylim((550,-50))
#bx[2].arrow(420,215,-30,0,width=0.5)

ima8 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig5\\fig5.2\galA1.2.png')
bx[3].imshow(ima8)
#bx[3].arrow(420,280,-30,0,width=0.5)

ax[0].set_xlim((420,800))#380
ax[1].set_xlim((430,790))#360
ax[2].set_xlim((450,760))#310
ax[3].set_xlim((410,820))#410
bx[0].set_xlim((390,770))#380
bx[1].set_xlim((520,880))#360
bx[2].set_xlim((430,740))#310
bx[3].set_xlim((330,740))#410

#ax[0].set_ylim((930,130))#710
#ax[1].set_ylim((930,200))#620
#bx[0].set_ylim((1030,-170))
#bx[1].set_ylim((1050,-150))
#bx[3].set_ylim((1050,-150))
ax[1].text(400, 70,r'$\mathit{lac}$',fontsize=8)
ax[3].text(400, 70,r'$\mathit{gal}$',fontsize=8)
bx[0].text(550, 650,'0HU\n40%',fontsize=8)
bx[1].text(620, 650,'2HU\n88%',fontsize=8)
bx[2].text(550, 650,'0HU\n64%',fontsize=8)
bx[3].text(550, 650,'1HU\n47%',fontsize=8)
fig.savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig5\\fig5.2\\fig5.3.png', dpi=600)
