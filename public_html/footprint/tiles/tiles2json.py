import pandas as pd
import geojson as gj
import numpy as np
import os
from pyproj import Proj
from shapely.geometry import shape

tiles=pd.read_csv('unique_tiles_y1a1.csv')

def r2m(ra):
    #return ra
    if ra> 180.:
        return ra-360.
    else:
        return ra


def toploygon(rall,decll,raul,decul,raur,decur,ralr,declr):
    P=gj.Polygon([[(r2m(rall),decll),(r2m(raul),decul),(r2m(raur),decur),(r2m(ralr),declr),(r2m(rall),decll)]])
    return P


ntiles=len(tiles)
areas = []
FC=[]
for i in xrange(ntiles):
    #i = w[j]
    P=toploygon(tiles.RALL[i],tiles.DECLL[i],tiles.RAUL[i],tiles.DECUL[i],
                tiles.RAUR[i],tiles.DECUR[i],tiles.RALR[i],tiles.DECLR[i])
    areas.append(shape(P).area)
    F=gj.Feature(geometry=P, id=i, properties={"tilename":tiles.TILENAME[i], "RA_C": tiles.RA_T[i], "DEC_C": tiles.DEC_T[i]})
    FC.append(F)

areas = np.array(areas)

bigFC=gj.FeatureCollection(FC)

dump=gj.dumps(bigFC)

ff=open('tiles.geojson','w')
ff.write(dump)
ff.close()

#if os.path.exists('des.json'):
#    os.remove('des.json')
#                
#os.system('topojson tiles.geojson > des.json')
