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

# En premier lieu, toute l'archive sera lu, et on va créer un fichier ascii de l'information par objet.
# Par la suite, il faudrait faire une liste contenant tous les fichier déjà créé, et faire lire cette liste par le code pour détecter 
# les nouvelles nuits, et les nuits qui ont été réduites de nouveau pour y inclure les changements. 
# La liste de compilation des nuits devra se réorganiser en ordre ascendant de "nom d'objet" (mais ça reste à discuter). 
# Cette liste pourra être lu par le code php.
# On devra faire rouler le code par instrument, et ensuite, combiner les listes pour n'en faire qu'une.
# Un code php sera créé pour lire la liste complete (de tous les instruments), quelque chose de très simple pour débuter (la raison d'avoir une liste ascendante de "nom d'objet"), 
# mais qui pourrait évoluer par la suite.

# Il faut lire dans /data/cpapir/reductions/YYMMDD/YYMMDD_*.fits.gz (pour CPAPIR) (ensuite adapter le code pour PESTO etc...)
# PLus rapide et directe que d'essayer de se créer une liste de nuits qui serait ensuite passé au code.

# Surement qu'il y a une façon plus simple... mais bon, voilà ce dont nous avons besoin :

# At the begining, we need to create the basic file : here, we need a question at the begining "Creating a basic file ?" if "Y" move to Boucle 1...
# if "N", then move to Boucle 5
# Boucle 1 : probe /data/cpapir/reductions/ and create a list of /data/cpapir/reductions/YYMMDD/YYMMDD_*.fits.gz (called basic_files_list_1)
# Boucle 2 : from that list, probe the metadata, and create one "simple_header_YYMMDD_targetname_filter" table file per image, save in the image night folder
# Boucle 3 : probe the /data/cpapir/reductions/YYMMDD/simple_header_YYMMDD_targetname_filter file and create a new list of all the table files "CPAPIR_simple_header_all"
# Boucle 4 : open a table file called "archive_targets_omm" read CPAPIR_simple_header_all, and fetch the information in those indovodual tables, and dump in "archive_targets_omm"
# Once we have run this once, stop
# For new data, run de code, and answer "N" to the question at the begining
# Boucle 5 : probe /data/cpapir/reductions/ and create a new list of /data/cpapir/reductions/YYMMDD/YYMMDD_*.fits.gz called "basic_files_list_2", 
# and compare with the previous basic list, and create a file with new entries "new_entries"
# Boucle 6 : read "new_entries" and probe the metadata, and create one "simple_header_YYMMDD_targetname_filter" table file per image, 
# save in the image night folder, and add the entore path of that file to "CPAPIR_simple_header_all", and then, read the table file, and dump in "archive_targets_omm"

# ce début de code plante... 
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
        
