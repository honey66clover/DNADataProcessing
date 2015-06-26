import numpy as np
import pandas as pd
import csv,Image
from matplotlib.pyplot import *
import matplotlib.colors as colors
import matplotlib.gridspec as gridspec

fig=figure(figsize=(3.42,5),dpi=600) #is in control
#fig={'figsize':(3.42,5),'dpi':600} #is not in control
font = {'family':'Arial','weight':'normal','size':7} #is in control
rc('font', **font)
#rc('figure',**fig)
gs1 = gridspec.GridSpec(2, 2)
gs1.update(top=0.98,bottom=0.12,wspace=0.,hspace=0.0)
ax=[0]*4
ax[0]=subplot(gs1[0,0])
ax[1]=subplot(gs1[0,1])
ax[2]=subplot(gs1[1,0])
ax[3]=subplot(gs1[1,1])
for i in range(0,4):
    ax[i].set_frame_on(False)
    ax[i].axis('off')
    ax[i].set_ylim((0,400))
    ax[i].set_xlim((150,450))

ima0 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s1\steps_145_895047_40092_2HU.png')
ax[0].imshow(ima0)
ax[0].text(270, 0,'2HU\n40%',fontsize=7)
ima1 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s1\steps_145_628995_635644_3HU.png')
ax[1].imshow(ima1)
ax[1].text(270, 0,'3HU\n16%',fontsize=7)
ima2 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s1\steps_145_283456_327814_4HU.png')
ax[2].imshow(ima2)
ax[2].text(270, 0,'4HU\n42%',fontsize=7)
ax[2].text(425, -50,'145bp',fontsize=7)
ima3 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s1\steps_145_990073_141808_5HU.png')
ax[3].imshow(ima3)
ax[3].text(270, 0,'5HU\n2%',fontsize=7)

fig.savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s1\s1.png', dpi=600)
