from matplotlib.pyplot import *
import pandas as pd
import numpy as np
import math
import matplotlib.colors as colors
import matplotlib.gridspec as gridspec

fig={'figsize':(3.42,2.8),'dpi':600}
font = {'family':'Arial','weight':'normal','size':7}
rc('font', **font)
rc('figure',**fig)

gs1=gridspec.GridSpec(1,2)
gs1.update(left=0.12, right=0.85, wspace=0.05,top=0.9,bottom=0.15)
ax1=subplot(gs1[0])
ax2=subplot(gs1[1])
gs2=gridspec.GridSpec(1,1)
gs2.update(left=0.87, right=0.9,top=0.8,bottom=0.25)
ax3=subplot(gs2[0])


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
im1=ax1.imshow(Z, interpolation='bicubic', origin='lower',cmap=None, extent=(80,150,0,150))
#ax1.xlabel('chain length')
#ax1.ylabel('HU position')
#levels =np.arange(0, 1, 0.1)
#CS=contour(Z, levels, hold='on', colors = 'k', origin='image', extent=(80,150,80,150))
#colorbar(im, orientation='vertical',shrink=0.3)
ax1.set_ylim(15,100)
majorLocator   = MultipleLocator(10.5)
#majorFormatter = FormatStrFormatter('%d')
#minorLocator   = MultipleLocator(10.5)
ax1.yaxis.set_major_locator(majorLocator)
#ax1.yaxis.set_minor_locator(minorLocator)
#ax1.yaxis.set_major_formatter(majorFormatter)
#ax1.yaxis.set_minor_locator(minorLocator)
ax1.set_yticklabels(['',2,'',4,'',6,'',8])
setp( ax1.get_yticklabels())

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
im2=ax2.imshow(Z, interpolation='bicubic', origin='lower',cmap=None, extent=(80,150,0,150))
ax2.set_ylim(15,100)
ax2.yaxis.set_major_locator(majorLocator)
#ax2.yaxis.set_minor_locator(minorLocator)
#ax1.yaxis.set_major_formatter(majorFormatter)
#ax1.yaxis.set_minor_locator(minorLocator)
#ax2.set_yticklabels([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
setp( ax2.get_yticklabels())
#This is for grey scale
#im=imshow(Z, interpolation='bicubic', origin='lower',cmap=cm.gray_r,norm = colors.Normalize(vmin=0, vmax =1, clip=False), extent=(80,150,0,150))

ax1.set_ylabel('HU spacing (turns)')
#ax1.set_ylim(10,100)
#ax1.set_yticks([20,40,60,80])
ax1.set_xticks([84,105,126,147])

#ax2.set_xlabel('DNA chain length (bp)')
#ax2.set_ylim(10,100)
#ax2.set_yticks([20,40,60,80])
ax2.set_xticks([84,105,126,147])

ax1.text(81.9, 93.9,'2HU',bbox={'facecolor':'white', 'alpha':1., 'pad':3},fontsize=8)
ax2.text(81.9, 93.9,'3HU',bbox={'facecolor':'white', 'alpha':1., 'pad':3},fontsize=8)
ax2.text(50, -5.2,'DNA chain length (bp)',fontsize=8)
ax1.text(0.1, 0.5, 'HU position', ha='center', va='center', rotation='vertical',fontsize=7)
#levels =np.arange(0, 1, 0.1)
#CS=contour(Z, levels, hold='on', colors = 'k', origin='image', extent=(80,150,80,150))
#ax2.colorbar(im, orientation='vertical',shrink=0.5)
colorbar(im2, cax=ax3)
#majorLocator = MultipleLocator(0.1)
#majorFormatter = FormatStrFormatter('%d')
#minorLocator   = MultipleLocator(1)
#ax3.yaxis.set_major_locator(majorLocator)
#ax3.yaxis.set_minor_locator(minorLocator)

ax1.xaxis.set_tick_params(color='w')
ax1.yaxis.set_tick_params(color='w')
ax2.xaxis.set_tick_params(color='w')
ax2.yaxis.set_tick_params(color='w')
    
    
ax3.set_yticklabels([0,'',0.1,'',0.2,'',0.3,'',0.4])
ax3.text(0, -0.07,r'$\mathit{w}$',fontsize=8)
setp(ax2.get_yticklabels(),visible=False)

savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s2\s2.1.png', dpi=600) 