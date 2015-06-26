from matplotlib.pyplot import *
import pandas as pd
import numpy as np
import math
import matplotlib.colors as colors

fig={'figsize':(3.42,5),'dpi':300}
font = {'family':'Arial','weight':'normal','size':7}
rc('font', **font)
rc('figure',**fig)

filename="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\HU minicircle shape\HU lengths\80-149\HU3_spacing_probability_HU+37.csv" 
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
figure()

#This is for color scale
im=imshow(Z, interpolation='bicubic', origin='lower',cmap=None,norm = colors.Normalize(vmin=0, vmax =1, clip=False), extent=(80,150,0,150))

#This is for grey scale
#im=imshow(Z, interpolation='bicubic', origin='lower',cmap=cm.gray_r,norm = colors.Normalize(vmin=0, vmax =1, clip=False), extent=(80,150,0,150))

xlabel('chain length')
ylabel('HU position')
ylim(10,80)

#levels =np.arange(0, 1, 0.1)
#CS=contour(Z, levels, hold='on', colors = 'k', origin='image', extent=(80,150,80,150))
colorbar(im, orientation='vertical',shrink=0.5)


#show()
savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\HU minicircle shape\HU lengths\80-149\HU3_spacing_probability_HU37_color.png', dpi=300) 