#!/usr/bin/env python3
import os,sys

def parcours(repertoire):
    pres=1
    print("Je suis dans le repertoire "+repertoire)
    liste=os.listdir(repertoire)
    for f in liste :
        if os.path.isfile(os.path.join(repertoire,f)) :
            print("err")
            os.system('./dehuf '+os.path.join(repertoire,f)+' '+os.path.join(repertoire,f)+'.dehuf')
            os.system('rm '+os.path.join(repertoire,f))
        if os.path.isdir(os.path.join(repertoire,f)) :
            parcours(os.path.join(repertoire,f))

parcours(sys.argv[1])




