# Code python pour lire une série de keywords dans le metadata des fichiers FITS pour créer une table qui sera accessible via une page web.
# Le but est de pouvoir vérifier si une cible a déjà été observée, et si oui, avwec quel instrument et filtre.
# Information qui sera tirée du metadata
# keys = ["OBJECT", "RATXT", "DECTXT", "TELESCOP", "INSTRUME", "FILTER", N_IND", "T_TOT", "NIGHTID", "EPOCH", "RELEASE"]
# RATXT et DECTXT sont les corrdonnées en format hh:mm:ss.s dd:mm:ss.s
# N_IND : nombre de fichiers combinés pour former le produit final
# T_TOT : Temps total du produit final

# Le code passe à travers toutes les nuits YYMMDD sur la tour d'archives OMM
# Exemple : pour CPAPIR, ce sont les images finales : /data/cpapir/reductions

# La recherche sera mis dans une table ascii ou csv, et cette table sera lu par un code php

# En premier lieu, toute l'archive sera lu, et par la suite, il faudrait trouver un moyen de lire l'archive pour 1) les nouvelles nuits, 2) les nuits qui ont été réduites de nouveau. 
# La liste devra se réorganiser en ordre ascendant de "nom d'objet", mais ça reste à discuter.

from astropy.io import ascii
from astropy.io import fits
import numpy as np

a = ascii.read("z.txt")
i = 0
while i<=2:
    b = fits.open(a[0][i])
    h = b[0].header
    OBJECT = np.array([h["OBJECT"]])
    RA = np.array([h["RATXT"]])
    DEC = np.array([h["DECTXT"]])
    TELESCOP = np.array([h["TELESCOP"]])
    INSTRUME = np.array([h["INSTRUME"]])
    FILTER = np.array([h["FILTER"]])
    NIGHTID = np.array([h["NIGHTID"]])
    EPOCH = np.array([h["EPOCH"]])
    RELEASE = np.array([h["RELEASE"]])
    N_IND = np.array([h["N_IND"]])
    T_TOT = np.array([h["T_TOT"]])
    ascii.write({"OBJECT": OBJECT, "RA": RA, "DEC": DEC,"TELESCOP": TELESCOP,"INSTRUME": INSTRUME, "FILTER": FILTER, "N_IND": N_IND, "T_TOT": T_TOT, "NIGHTID": NIGHTID, "EPOCH": EPOCH, "RELEASE": RELEASE}, "coordinates.dat", names=["OBJECT", "RA", "DEC", "TELESCOP", "INSTRUME", "FILTER", "N_IND", "T_TOT", "NIGHTID", "EPOCH", "RELEASE"])
    i = i+1
        
