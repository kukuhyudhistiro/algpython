"""
Cek golongan usia menggunakan loop
- loop cek inputan range usia harus >0-100
- loop run program (ok)
"""
#cek golongan usia
jwbulangprog = "y"
while jwbulangprog=="y" or jwbulangprog=="Y":
    print ("=========================")
    print(" CEK GOLONGAN USIA ")
    print ("=========================")
    u=1
    while int(u)>0 and int(u)<=100:
        u = input(">> Masukkan Usia = ")
        #cek batasan inputan usia 0-100
        if int(u)>0 and int(u)<=100:
            if int(u)>=60: 
                sts="lansia"
            elif int(u)>=35: sts="dewasa"
            elif int(u)>=18: sts="pemuda"
            elif int(u)>=15: sts="remaja"
            else:
                sts="anak"
            print (sts)

            jwbulangprog = input(">>> Ulang program? y/t = ")
            if jwbulangprog=="t" or jwbulangprog=="T":
                break
        else:
            pesan=">>> Masukkan angka usia 0-100 saja"
            print(pesan)
            break
    

  