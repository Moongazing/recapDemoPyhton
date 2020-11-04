# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:25:49 2020

@author: TUNAHAN
"""

sayi=int(input("Sayıyı Giriniz:"))
asalMi=True
for x in range(2,sayi):
    if sayi%x==0:
       asalMi=False
       break
if asalMi:#default true geldiğinden şarto yazamaya gerek yok 
    print("Asal")
else:
    print("Asal Değil")
