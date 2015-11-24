import pandas as pd
import geojson as gj
import numpy as np
import os
from pyproj import Proj
from shapely.geometry import shape


def r2m(ra):
    #return ra
    if ra> 180.:
        return ra-360.
    else:
        return ra


def toploygon(rall,decll,raul,decul,raur,decur,ralr,declr):
    P=gj.Polygon([[(r2m(rall),decll),(r2m(raul),decul),(r2m(raur),decur),(r2m(ralr),declr),(r2m(rall),decll)]])
    return P

decL=[-75,-60,-45,-30,-15,0,15,30,45,60,75]
raL=[0,30,60,90,120,150,180,-30,-60,-90,-120,-150]

FC=[]
for i in xrange(len(decL)):
    P= gj.Polygon([[(-180,decL[i]),(180,decL[i]),(180,decL[i]+0.0001),(-180,decL[i]+0.0001),(-180,decL[i])]])
    F=gj.Feature(geometry=P, id=i)
    FC.append(F)

i=i+1
for j in xrange(len(raL)):
    P= gj.Polygon([[(raL[j],-90),(raL[j],90),(raL[j]+0.0001,90),(raL[j]+0.0001,-90),(raL[j],-90)]])
    F=gj.Feature(geometry=P, id=i+j)
    FC.append(F)

bigFC=gj.FeatureCollection(FC)

dump=gj.dumps(bigFC)

ff=open('grid.geojson','w')
ff.write(dump)
ff.close()

if os.path.exists('gridt.json'):
    os.remove('gridt.json')
                
os.system('topojson grid.geojson > gridt.json')
