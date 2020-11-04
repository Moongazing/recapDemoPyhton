# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:50:25 2020

@author: TUNAHAN
"""
def topla(sayi1,sayi2):
    return(sayi1+sayi2)
def cikar(sayi1,sayi2):
    return(sayi1-sayi2)
def carp(sayi1,sayi2):
    return(sayi1*sayi2)
def bol(sayi1,sayi2):
   return(sayi1/sayi2)
    
sayi1=int (input ("Birinci Sayıyı Giriniz:"))
sayi2=int (input("İkinci Sayıyı Giriniz:"))
opar=(input ("Operatörü Giriniz:"))
if opar=="+":
   print( str(topla(sayi1,sayi2)))
elif opar=="-":
    print(str(cikar(sayi1,sayi2)))
elif opar=="*":
    print(str(carp(sayi1,sayi2)))
elif opar=="/":
    print(str(bol(sayi1,sayi2)))
else :
    print("Uyumsuz Operatör")
    

    
    