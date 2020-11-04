# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:47:02 2020

@author: TUNAHAN
"""

liste=['engin',0,3,"6"]
for x in liste:
    try:
        print("Sayı:" + str(x))
        sonuc=1/int(x)
        print("Sonuç: "+str(sonuc))
    except ValueError:
        print("Lütfen Sayı Giriniz")
    except  ZeroDivisionError:
        print("Payda Sıfır Olamaz")
    except:
        print(str(x)+"Hesaplanamadı")
        print("Sistem Diyor Ki:" + str(sys.exc_info()[0]))#info alma 
    finally:
        print("İşlemler Bitti")