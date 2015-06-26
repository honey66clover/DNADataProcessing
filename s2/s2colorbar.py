from matplotlib.pyplot import *
import pandas as pd
import numpy as np
import math
import matplotlib.colors as colors
import matplotlib.gridspec as gridspec

fig={'figsize':(3.42,5),'dpi':600}
font = {'family':'Arial','weight':'normal','size':7}
rc('font', **font)
rc('figure',**fig)

fig, axes = subplots(nrows=2, ncols=1)
ax1=axes.flat[0]
ax2=axes.flat[1]
#for ax in axes.flat:
#    im = ax.imshow(np.random.random((10,10)), vmin=0, vmax=1)

filename="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s2\HU2_spacing_probability_HU+37.csv" 
df=pd.read_table(filename,sep=',')
bp=df['N(bp)']
p1=df['1']
x=range(0,70)
y=range(1,150)
X, Y = np.meshgrid(x, y)
z=df.values
Z=z[X,Y]
Z=np.nan_to_num(Z)
Z=np.around(Z,decimals=3)

#t=1/(Z*100)
#t=np.around(t,decimals=3)
#im=imshow(Z, interpolation='bicubic', origin='lower',cmap=None,norm = colors.Normalize(vmin=0, vmax =1, clip=False), extent=(80,150,0,150))
im=ax1.imshow(Z, interpolation='bicubic', origin='lower',cmap=None, extent=(80,150,0,150))
#ax1.xlabel('chain length')
#ax1.ylabel('HU position')
ax1.set_ylim(30,100)
ax1.set_yticks([30,50,70,90])
ax1.set_xticks([84,94,105,115,126,136,147])
#levels =np.arange(0, 1, 0.1)
#CS=contour(Z, levels, hold='on', colors = 'k', origin='image', extent=(80,150,80,150))
#colorbar(im, orientation='vertical',shrink=0.3)

filename="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s2\HU3_spacing_probability_HU+37.csv" 
df=pd.read_table(filename,sep=',')
bp=df['N(bp)']
p1=df['1']
x=range(0,70)
y=range(1,150)
X, Y = np.meshgrid(x, y)
z=df.values
Z=z[X,Y]
Z=np.nan_to_num(Z)
Z=np.around(Z,decimals=3)

#t=1/(Z*100)
#t=np.around(t,decimals=3)

#This is for color scale
#im=imshow(Z, interpolation='bicubic', origin='lower',cmap=None,norm = colors.Normalize(vmin=0, vmax =1, clip=False), extent=(80,150,0,150))
im=ax2.imshow(Z, interpolation='bicubic', origin='lower',cmap=None, extent=(80,150,0,150))

#This is for grey scale
#im=imshow(Z, interpolation='bicubic', origin='lower',cmap=cm.gray_r,norm = colors.Normalize(vmin=0, vmax =1, clip=False), extent=(80,150,0,150))

ax2.set_xlabel('DNA chain length (bp)')
#ax2.set_ylabel('HU position')
ax2.set_ylim(10,80)
ax2.set_yticks([10,30,50,70])
ax2.set_xticks([84,94,105,115,126,136,147])

ax1.text(81, 96.5,'2HU',bbox={'facecolor':'white', 'alpha':1., 'pad':3},fontsize=7)
ax2.text(81, 76.5,'3HU',bbox={'facecolor':'white', 'alpha':1., 'pad':3},fontsize=7)
fig.text(0.1, 0.5, 'HU position', ha='center', va='center', rotation='vertical',fontsize=7)
#levels =np.arange(0, 1, 0.1)
#CS=contour(Z, levels, hold='on', colors = 'k', origin='image', extent=(80,150,80,150))
fig.subplots_adjust(left=0., right=0.95,hspace=0.05)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
setp(ax1.get_xticklabels(),visible=False)
fig.colorbar(im, cax=cbar_ax)

savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s2\s2.png', dpi=600) 