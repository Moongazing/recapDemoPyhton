# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 19:54:54 2020

@author: TUNAHAN
"""

ogrenciler=["Engin","Derin","Salih","Ali","Ayşe"]
fileToAppend=open("ogrenciler.txt","a")
for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")
    
fileToAppend.close()