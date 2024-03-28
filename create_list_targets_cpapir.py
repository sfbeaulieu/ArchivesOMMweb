#faire une boucle pour passer toutes les images dans une même nuit
#dumper dans une table
# ['OBJECT', 'RATXT ', 'DECTXT', 'TELESCOP','INSTRUME','FILTER','NIGHTID','EPOCH','RELEASE','N_IND (no. images indiv)','T_TOT (temps total)']

from astropy.io import ascii
from astropy.io import fits
import numpy as np

#a = ascii.read("z.txt")
#i = 0
#while i<=2:
#    b = fits.open(a[0][i])
#    h = b[0].header
#    OBJECT = np.array([h["OBJECT"]])
#    RA = np.array([h["RATXT"]])
#    DEC = np.array([h["DECTXT"]])
#    TELESCOP = np.array([h["TELESCOP"]])
#    INSTRUME = np.array([h["INSTRUME"]])
#    FILTER = np.array([h["FILTER"]])
#    NIGHTID = np.array([h["NIGHTID"]])
#    EPOCH = np.array([h["EPOCH"]])
#    RELEASE = np.array([h["RELEASE"]])
#    N_IND = np.array([h["N_IND"]])
#    T_TOT = np.array([h["T_TOT"]])
#    ascii.write({"OBJECT": OBJECT, "RA": RA, "DEC": DEC,"TELESCOP": TELESCOP,"INSTRUME": INSTRUME,"FILTER": FILTER,"NIGHTID": NIGHTID,"EPOCH": EPOCH,"RELEASE": RELEASE,"N_IND": N_IND,"T_TOT": T_TOT }, "coordinates.dat", names=["OBJECT", "RA", "DEC", "TELESCOP", "INSTRUME", "FILTER", "NIGHTID", "EPOCH", "RELEASE", "N_IND", "T_TOT"])
#    i = i+1

keys = ["OBJECT", "RATXT", "DECTXT", "TELESCOP", "INSTRUME", "FILTER", "NIGHTID", "EPOCH", "RELEASE", "N_IND", "T_TOT"]

hdulist = fits.open("z.txt")
header = hdulist[0].header
for k in keys:
#    print k, "=", header[k]

        data = {}

# Initialize "data" with empty lists for each key
for k in keys:
    data[k] = []

# Collect all data in the "data" dictionary
for i in range(0, 2):
    data["RATXT"].append(np.array(i))
    data["DECTXT"].append(np.array(i+1))

ascii.write(data, "coords.dat", names=keys)
