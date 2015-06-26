#import csv
from matplotlib.pyplot import *
import pandas as pd

filename="C:\Users\honey66clover\Desktop\Weijuan\DNA\HU\sample pictures2\s4\HU-bound DNA shape_1per200_100-149.csv" 
df=pd.read_table(filename,sep=',')
#print df
x=df['HU/200bp']
HU2even=df['2HU even']
HU2uneven=df['2HU uneven']
HU3equi=df['3HU equilateral']
HU3iso=df['3HU isosceles']
HU3scal=df['3HU scalene']

p21=bar(x,HU2even,color='0',label='2HU even')
p22=bar(x,HU2uneven,color='0.3',bottom=HU2even,label='2HU uneven')
p31=bar(x,HU3equi,color='r',bottom=HU2even+HU2uneven,label='3HU equilateral')
p32=bar(x,HU3iso,color='0.8',bottom=HU2even+HU2uneven+HU3equi,label='3HU isosceles')
p33=bar(x,HU3scal,color='1',bottom=HU2even+HU2uneven+HU3equi+HU3iso,label='3HU scalene')

title('probabilities of different shapes for 1per200')
#legend((p21[0],p22[0],p31[0],p32[0],p33[0]),('2HU even','2HU uneven','3HU equilateral','3HU isosceles','3HU scalene'))
#legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,prop={'size':10})
legend(bbox_to_anchor=(0., 0, 1, .102), loc=3,ncol=5, mode="expand",borderaxespad=0.)
show()