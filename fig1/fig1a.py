#import csv
from matplotlib.pyplot import *
import matplotlib.gridspec as gridspec
import pandas as pd

fig=figure(figsize=(3.42,5),dpi=600) #is in control
#fig={'figsize':(3.42,5),'dpi':600} #is not in control
font = {'family':'Arial','weight':'normal','size':7} #is in control
rc('font', **font)
#rc('figure',**fig)

gs=gridspec.GridSpec(2,1,height_ratios=[1,4])
ax1=subplot(gs[0])
ax2=subplot(gs[1])

filename1="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\HU binding probability\Average HU number and binding probabilities weighted by J factor\protein_bound_probabilities_1per50_80-149.dat" 
df1=pd.read_table(filename1,sep='\t')
#print df
df1['<HU>'] = df1['1HU'] + 2*df1['2HU']+3*df1['3HU']+4*df1['4HU']+5*df1['5HU']+6*df1['6HU']+7*df1['7HU']+8*df1['8HU']
df1['1HU/50']=df1['N(bp)']/float(50)
#print df['<HU>']
#print df['1HU/50']
x=df1['N(bp)']
#print x
p1,=ax1.plot(x,df1['<HU>'],'k--')
p2,=ax1.plot(x,df1['1HU/50'],'k-')
ax1.set_ylabel('numbers of HU') #could be controlled by rc.font
ax1.legend([p1,p2],["<HU>","1HU/50"],bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.,fontsize=7)#not controlled by rc.font
setp( ax1.get_xticklabels())
majorLocator   = MultipleLocator(1)
majorFormatter = FormatStrFormatter('%d')
minorLocator   = MultipleLocator(0.5)
ax1.yaxis.set_major_locator(majorLocator)
ax1.yaxis.set_major_formatter(majorFormatter)
ax1.yaxis.set_minor_locator(minorLocator)
setp( ax1.get_yticklabels())


filename="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\HU binding probability\Average HU number and binding probabilities weighted by J factor\protein_bound_probabilities_1per50_80-149_weighted_by_J_factor.csv" 
df=pd.read_table(filename,sep=',')
#print df
x=df['N(bp)']
HU2=df['2HUconfig']
HU3=df['3HUconfig']
HU4=df['4HUconfig']

p2=ax2.bar(x,HU2,color='0.3')
p3=ax2.bar(x,HU3,color='0.65',bottom=HU2)
p4=ax2.bar(x,HU4,color='1',bottom=HU3+HU2)

ax2.set_xlabel('DNA chain length (bp)')
ax2.set_ylabel('numbers of configurations')
ax2.legend((p2[0],p3[0],p4[0]),('2HU','3HU','4HU'),fontsize=7)
setp( ax2.get_xticklabels())
setp( ax2.get_yticklabels())
ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,5))


#fig.show()
savefig('C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\HU binding probability\Average HU number and binding probabilities weighted by J factor\\fig1.png',dpi=600) 