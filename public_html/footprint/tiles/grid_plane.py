import pandas as pd
import geojson as gj
import numpy as np
import os
from pyproj import Proj
from shapely.geometry import shape
from astropy import units as u
from astropy.coordinates import SkyCoord

def r2m(ra):
    #return ra
    if ra> 180.:
        return ra-360.
    else:
        return ra


def toploygon(rall,decll,raul,decul,raur,decur,ralr,declr):
    P=gj.Polygon([[(r2m(rall),decll),(r2m(raul),decul),(r2m(raur),decur),(r2m(ralr),declr),(r2m(rall),decll)]])
    return P

#FC=[]
#for i in xrange(len(decL)):
#    P= gj.Polygon([[(-180,decL[i]),(180,decL[i]),(180,decL[i]+0.0001),(-180,decL[i]+0.0001),(-180,decL[i])]])
#    F=gj.Feature(geometry=P, id=i)
#    FC.append(F)


ll=np.linspace(0,360,100)
ra=[]
dec=[]
P=[]
FC=[]
for i in xrange(len(ll)):
    c=SkyCoord(l=ll[i]*u.degree, b=0.*u.degree, frame='galactic')
    ra.append(r2m(c.icrs.ra.value))
    dec.append(c.icrs.dec.value)
    
ra=np.array(ra)
dec=np.array(dec)

s=np.argsort(ra)

ra=ra[s]
dec=dec[s]

for i in xrange(len(ra)):
    P.append((ra[i],dec[i]))


for i in xrange(len(ra)):
    P.append((ra[-1-i],dec[-i-1]+0.1))

P.append((ra[0],dec[0]))
print i

print P
P2=gj.Polygon([P])
F=gj.Feature(geometry=P2, id=0)
FC.append(F)

bigFC=gj.FeatureCollection(FC)

dump=gj.dumps(bigFC)

ff=open('plane.geojson','w')
ff.write(dump)
ff.close()

#if os.path.exists('gridt.json'):
#    os.remove('gridt.json')
                
#os.system('topojson plane.geojson > gridt.json')
