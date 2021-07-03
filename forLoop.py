# -*- coding: utf-8 -*-
"""
Created on Fri May 28 08:39:04 2021

@author: x220
"""

jwb="Y" 
while jwb=="Y" or jwb=="y":

    print("CEK KELULUSAN")
    print("------------------")
    n = input("Masukkan Nilai = ")
    m = int(n)
    if m>60:
        status = "Lulus"
    else:
        status="Ulang"
    print (status)
    
    jwb = input("Input Lagi?")
    if jwb == "T":
        #print(jwb)
        break
    