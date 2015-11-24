import pandas as pd
import numpy as np

df=pd.read_csv('mini_y2.csv')

tiles=pd.read_csv('all_tiles.csv')

def find_tile(ra,dec):
    try:
        w=np.where( ( tiles.RACMAX > ra) & (tiles.RACMIN <=ra) & ( tiles.DECCMAX > dec) & ( tiles.DECCMIN < dec))[0]
        return w[0]
    except:
        return -1


tt=[]

for i in xrange(len(df)):
    if i%10000 == 0 :print i
    c=find_tile(df.RA[i],df.DEC[i])
    tt.append(c)

    
