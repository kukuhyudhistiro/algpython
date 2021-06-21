# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 15:33:34 2021

@author: x220
"""
#1. Mencetak seluruh item List menggunakan Loop
namakota = ['A','B','C','D','E']
#a. While
print(" Menggunakan WHILE ------------------------------")
i = 0;
while i < len(namakota):
    print(namakota[i])
    i = i + 1;
    
#b. For
print(" Menggunakan FOR ------------------------------")
for i in range(len(namakota)):
    print(namakota[i])
    
#2. mencetak nomor indeks dari item yang terpilih
pilihan = input(">> Masukkan Pilihan = ")

i = 0;
while i<len(namakota):
    #cek apakah namakota pada index yg AKTIF == pilihan
    if namakota[i] == pilihan:
        #jika COCOK, print index numbernya
        print(">>> Index Number dari item terpilih = " + str(i))
    
    i+=1

