import pandas as pd
import geojson as gj
import numpy as np
import os
from pyproj import Proj
from shapely.geometry import shape


tiles0=pd.read_csv('unique_svtiles.csv')
tiles1=pd.read_csv('unique_y1tiles.csv')
tiles2=pd.read_csv('unique_y2tiles.csv')


w2=np.array([i for i,val in enumerate(tiles1.TILENAME.values) if val not in tiles0.TILENAME.values ])
w3=np.array([i for i,val in enumerate(tiles2.TILENAME.values) if ((val not in tiles1.TILENAME.values) & (val not in tiles0.TILENAME.values)) ])

#print len(w3)
#tiles2=tiles2t.ix[w3]

#w = np.where(tiles.DEC_T < -10)[0]

def r2m(ra):
    #return ra
    if ra> 180.:
        return ra-360.
    else:
        return ra


def toploygon(rall,decll,raul,decul,raur,decur,ralr,declr):
    P=gj.Polygon([[(r2m(rall),decll),(r2m(raul),decul),(r2m(raur),decur),(r2m(ralr),declr),(r2m(rall),decll)]])
    return P


ntiles0=len(tiles0)
print ntiles0,' ntiles'
FC=[]
for i in xrange(len(tiles0)):
    #i = w[j]
    P=toploygon(tiles0.RAC1[i],tiles0.DECC1[i],tiles0.RAC2[i],tiles0.DECC2[i],
                tiles0.RAC3[i],tiles0.DECC3[i],tiles0.RAC4[i],tiles0.DECC4[i])
    #areas.append(shape(P).area)
    F=gj.Feature(geometry=P, id=i, properties={"tilename":tiles0.TILENAME[i], "RA_C": tiles0.RA[i], "DEC_C": tiles0.DEC[i]})
    FC.append(F)

bigFC=gj.FeatureCollection(FC)

dump=gj.dumps(bigFC)

ff=open('tiles_sv.geojson','w')
ff.write(dump)
ff.close()

if os.path.exists('des_sv.json'):
    os.remove('des_sv.json')
                
os.system('topojson tiles_sv.geojson > des_sv.json')



ntiles1=len(tiles1)
print ntiles1,' ntiles'
FC=[]
for j in xrange(len(w2)):
    i = w2[j]
    #i = w[j]
    P=toploygon(tiles1.RAC1[i],tiles1.DECC1[i],tiles1.RAC2[i],tiles1.DECC2[i],
                tiles1.RAC3[i],tiles1.DECC3[i],tiles1.RAC4[i],tiles1.DECC4[i])
    #areas.append(shape(P).area)
    F=gj.Feature(geometry=P, id=i, properties={"tilename":tiles1.TILENAME[i], "RA_C": tiles1.RA[i], "DEC_C": tiles1.DEC[i]})
    FC.append(F)

bigFC=gj.FeatureCollection(FC)

dump=gj.dumps(bigFC)

ff=open('tiles_y1.geojson','w')
ff.write(dump)
ff.close()

if os.path.exists('des_y1.json'):
    os.remove('des_y1.json')
                
os.system('topojson tiles_y1.geojson > des_y1.json')


ntiles2=len(tiles2)
print ntiles2,' ntiles'
FC=[]
for j in xrange(len(w3)):
    i = w3[j]
    P=toploygon(tiles2.RAC1[i],tiles2.DECC1[i],tiles2.RAC2[i],tiles2.DECC2[i],
                tiles2.RAC3[i],tiles2.DECC3[i],tiles2.RAC4[i],tiles2.DECC4[i])
    #areas.append(shape(P).area)
    F=gj.Feature(geometry=P, id=i, properties={"tilename":tiles2.TILENAME[i], "RA_C": tiles2.RA[i], "DEC_C": tiles2.DEC[i]})
    FC.append(F)

bigFC=gj.FeatureCollection(FC)

dump=gj.dumps(bigFC)

ff=open('tiles_y2.geojson','w')
ff.write(dump)
ff.close()

if os.path.exists('des_y2.json'):
    os.remove('des_y2.json')
                
os.system('topojson tiles_y2.geojson > des_y2.json')
