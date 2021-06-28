# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 11:17:35 2021

@author: x220
"""

print("")
print("========================================")
print(" DAFTAR MENU ")
print("========================================")
print(" a = COCA COLA   Rp 10.000")
print(" b = AQUA        Rp 5.000")
print(" c = MIZONE      Rp 8.000")
print(" d = ABC KOPI    Rp 3.000")
print(" e = MOCACINO    Rp 15.000")
print("========================================")
print("")

#1. SIAPKAN VARIABEL
kode =['a','b','c','d','e']
namaBarang = [' COCA COLA','AQUA','MIZONE','ABC KOPI','MOCACINO']
harga = [10000,5000,8000,3000,15000]

#2. INPUT PILIHAN
pilihan = input(">> Masukkan Kode Barang    = ")

#3. INPUT QTY
qty     = input(">> Masukkan Jumlah Barang  = ")

#4. HITUNG BAYAR
##cek nama barang dan ambil harga satuan
i = 0
while i<len(namaBarang):
    #jika value pada list kode[i] == pilihan
    if kode[i] == pilihan:
        #ambil nama barang
        nm_brg = namaBarang[i]

        #ambil harga satuan
        hrgsat = harga[i]
        
    #jika tidak cocok, lanjut ke i berikutnya
    i+=1

tot_byr = hrgsat * int(qty)

#5. TAMPILKAN 
print(">>> NAMA BARANG      : " + nm_brg)
print(">>> HARGA BARANG     : " + str(hrgsat))
print(">>> JUMLAH BARANG    : " + qty)
print(("-------------------------------"))
print(">>> TOTAL BAYAR      : " + str(tot_byr))

"""
1. buatlah agar format uang tersebut memiliki digit ribuan
2. tambahkan fitur Mengulang transaksi
3. Challenge:
    - output ke Notepad
"""

"""
pada materi selanjutnya: 
    program akan dibuat agar pembeli dapat membeli 
    beberapa barang sekaligus dalam SATU kali transaksi
    clue: looping pada tambah Item.
"""
