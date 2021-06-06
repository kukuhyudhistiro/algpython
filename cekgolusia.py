#cek golongan usia
print ("=========================")
print(" CEK GOLONGAN USIA ")
print ("=========================")

u = input(">> Masukkan Usia = ")
#cek batasan inputan usia 0-100
if int(u)>0 and int(u)<=100:
    if int(u)>=60: 
        sts="lansia"
    elif int(u)>=35: 
        sts="dewasa"
    elif int(u)>=18: 
        sts="pemuda"
    elif int(u)>=15: sts="remaja"
    else:
        sts="anak"
    print (sts)
else:
    pesan=">>> Masukkan angka usia 0-100 saja"
    print(pesan)
