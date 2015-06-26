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
gs1 = gridspec.GridSpec(1, 5)
gs1.update(top=0.99, bottom=0.54,left=0.,right=1.,wspace=0.,hspace=0.0)
ax=[0]*5
for i in range(0,5):
    ax[i]=subplot(gs1[:,i])
    ax[i].set_frame_on(False)
    ax[i].axis('off')
    ax[i].set_ylim((0,400))
    ax[i].set_xlim((200,400))

gs2 = gridspec.GridSpec(1, 5)
gs2.update(top=0.46, bottom=0.01,left=0.,right=1., wspace=0.,hspace=0.)
bx=[0]*5
for i in range(0,5):
    bx[i]=subplot(gs2[:,i])
    bx[i].set_frame_on(False)
    bx[i].axis('off')
    bx[i].set_ylim((0,400))
    bx[i].set_xlim((200,400))

ima0 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig2\Luke\structure-105bp-ID0_B0-5.png')
ax[0].imshow(ima0)
ax[0].text(260, -70,'105bp\n2HU\n96%',fontsize=7)
ima1 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig2\Luke\structure-111bp-ID0_B0-3.png')
ax[1].imshow(ima1)
ax[1].text(260, -70,'111bp\n3HU\n45%',fontsize=7)
ima2 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig2\Luke\structure-113bp-ID0_B0-16.png')
ax[2].imshow(ima2)
ax[2].text(260, -70,'113bp\n4HU\n39%',fontsize=7)
ima3 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig2\Luke\structure-115bp-ID0_B0-4.png')
ax[3].imshow(ima3)
ax[3].text(260, -70,'115bp\n2HU\n93%',fontsize=7)
ima4 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig2\Luke\structure-126bp-ID0_B0-5.png')
ax[4].imshow(ima4)
ax[4].text(260, -70,'126bp\n2HU\n90%',fontsize=7)

ima5 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig2\hbb\\structure-105bp-ID1_B0-6.png')
bx[0].imshow(ima5)
bx[0].arrow(420,115,-30,0,width=0.5)
ima6 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig2\hbb\\structure-105bp-ID1_B0-8.png')
bx[1].imshow(ima6)
bx[1].arrow(420,130,-30,0,width=0.5)
ima7 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig2\hbb\\structure-105bp-ID1_B0-2.png')
bx[2].imshow(ima7)
bx[2].arrow(420,185,-30,0,width=0.5)
ima8 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig2\hbb\\structure-105bp-ID1_B0-9.png')
bx[3].imshow(ima8)
bx[3].arrow(420,260,-30,0,width=0.5)
ima9 = Image.open('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig2\hbb\\structure-105bp-ID1_B0-1.png')
bx[4].imshow(ima9)
bx[4].arrow(380,325,-10,0,width=0.5)

fig.savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\\fig2\\fig2.1.png', dpi=600)
