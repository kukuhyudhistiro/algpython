# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 09:42:52 2021

@author: x220
"""
"""
Buat program untuk menghitung biaya total pengiriman barang di perusahaan Ekspedisi
Lorena di Malang
SOAL Aplikasi 6e hal 3
"""
print("==============================================")
print(" TRANSAKSI BIAYA EKSPEDISI ")
print("==============================================")
print(" a = Surabaya")
print(" b = Bandung")
print(" ")
#jika menggunakan list Kode dibawah ini, maka metode yang digunakan
#adalah mendeteksi indeks value yang terpilih pada list kode.
#caranya: melakukan pencarian pada list kode menggunakan 
# nilai kode yang diinputkan
#salah satu metode : gunakan while
kode =['a','b']
#algoritma:
# baca berulang2 index dalam list kode, jika value sama dengan 
# value pilihan, ambil index nya

kota = ['surabaya','bandung']
jarak = [169,452]
ongkirperkm = [2500,4000]

pilihan = input(">> Masukkan Kode Tujuan = ")
#identifikasi Indeks list berdasarkan pilihan
if pilihan=="a":
    idx = 0
elif pilihan=="b":
    idx = 1
else:
    idx =0
print(">>> Pilihan Tujuan   = " + kota[idx])
print(">>>          Jarak   = " + str(jarak[idx]) + " km")
print(">>>  Ongkir per Km   = Rp. " + str(ongkirperkm[idx]))

#tahap hitung biaya
ongkir = jarak[idx] * ongkirperkm[idx]
#tampilkan biaya kirim
print(">>>> Total           = Rp. " + str(ongkir))
print(" ")
print("==============================================")

