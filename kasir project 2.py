import pandas as pd
import os 
os.system('cls')
print("---------------------  Mangood Program  --------------------")
print("---------------- Selamat Datang di Mangood -----------------")
pembeli = input("Masukkan namamu: ")
print ("Hai", pembeli) 
data='project.csv'
df=pd.read_csv(data)
df.index=[1,2,3,4,5,6,7,8,9,10,11]
print(df)
def habis():
    if nomor==1:
        if jumlah>Madu:
            print("Stok kurang, silahkan pilih dari awal")

            awal()
    elif nomor==2:
        if jumlah>Apel:
            print("Stok kurang, silahkan pilih dari awal")
            awal()
    elif nomor==3:
        if jumlah>hm:
            print("Stok kurang, silahkan pilih dari awal")
            awal()
    elif nomor==4:
        if jumlah>Manalagi:
            print("Stok kurang, silahkan pilih dari awal")
            awal()
    elif nomor==5:
         if jumlah>Madu:
            print("Stok kurang, silahkan pilih dari awal")
            awal()
    elif nomor==6:
        if jumlah>Madu:
            print("Stok kurang, silahkan pilih dari awal")
            awal()
    elif nomor==7:
        if jumlah>Madu:
            print("Stok kurang, silahkan pilih dari awal")
            awal()
    elif nomor==8:
        if jumlah>Madu:
            print("Stok kurang, silahkan pilih dari awal")
            awal()
    elif nomor==9:
        if jumlah>Madu:
            print("Stok kurang, silahkan pilih dari awal")
            awal()
    elif nomor==10:
        if jumlah>Madu:
            print("Stok kurang, silahkan pilih dari awal")
            awal()
    elif nomor==11:
        if jumlah>Madu:
            print("Stok kurang, silahkan pilih dari awal")
            awal()
    
def listmangga():
    global Madu
    global Apel
    global hm
    global Manalagi
    global Indramayu
    global Golek
    global Kweni
    global Alpukat
    global Gandaria
    global Budiraja
    global Gadung
    Madu=df.iloc[0,1]
    Apel=df.iloc[1,1]
    hm=df.iloc[2,1]
    Manalagi=df.iloc[3,1]
    Indramayu=df.iloc[4,1]
    Golek=df.iloc[5,1]
    Kweni=df.iloc[6,1]
    Alpukat=df.iloc[7,1]
    Gandaria=df.iloc[8,1]
    Budiraja=df.iloc[9,1]
    Gadung=df.iloc[10,1]
listharga=[]
listjumlah=[]
listnama=[]
listsubtotal=[]
totalsemua=0
def pemesanan():
    global harga
    global jumlah
    global nama
    global totalsemua
    global subtotal
    global nomor
    global Madu
    global Apel
    global hm
    global i
    global Manalagi
    global Indramayu
    global Golek
    global Kweni
    global Alpukat
    global Gandaria
    global Budiraja
    global Gadung
    for i in range(x):
        nomor=int(input("Masukan Jenis Mangga (dalam bentuk angka): "))
        while True:
            if nomor not in df.index:
                nomor=int(input("Mangga Tidak Tersedia, Silahkan Pilih Ulang (dalam bentuk angka): "))
                continue
            jumlah= int(input("jumlah dalam kg: "))
            listjumlah.append(jumlah)
            habis()
            if nomor==1   :
                            harga=30000
                            listharga.append(harga)
                            nama=("Mangga Madu")
                            listnama.append(nama)
                            subtotal=listharga[i]*listjumlah[i]
                            listsubtotal.append(subtotal)
                            print (jumlah,"Kg",nama,"Rp.",harga, "= Rp.",subtotal)
                            df.iloc[0,1]=Madu-jumlah
                            df.to_csv(data,index=False)
                            break
            elif nomor==2:
                            harga=40000
                            listharga.append(harga)
                            nama=("Mangga Apel")
                            listnama.append(nama)
                            subtotal=listharga[i]*listjumlah[i]
                            listsubtotal.append(subtotal)
                            print (jumlah,"Kg",nama,"Rp.",harga, "= Rp.",subtotal)
                            df.iloc[1,1]=Apel-jumlah
                            df.to_csv(data,index=False)
                            break
            elif nomor==3:
                            harga=40000
                            listharga.append(harga)
                            nama=("Mangga Harum Manis")
                            listnama.append(nama)
                            subtotal=listharga[i]*listjumlah[i]
                            listsubtotal.append(subtotal)
                            print (jumlah,"Kg",nama,"Rp.",harga, "= Rp.",subtotal)
                            df.iloc[2,1]=hm-jumlah
                            df.to_csv(data,index=False)
                            break
            elif nomor==4:
                            harga=15000
                            listharga.append(harga)
                            nama=("Mangga Manalagi")
                            listnama.append(nama)
                            subtotal=listharga[i]*listjumlah[i]
                            listsubtotal.append(subtotal)
                            print (jumlah,"Kg",nama,"Rp.",harga, "= Rp.",subtotal)
                            df.iloc[3,1]=Manalagi-jumlah
                            df.to_csv(data,index=False)
                            break
            elif nomor==5:
                            harga=20000
                            listharga.append(harga)
                            nama=("Mangga Indramayu")
                            listnama.append(nama)
                            subtotal=listharga[i]*listjumlah[i]
                            listsubtotal.append(subtotal)
                            print (jumlah,"Kg",nama,"Rp.",harga, "= Rp.",subtotal)
                            df.iloc[4,1]=Indramayu-jumlah
                            df.to_csv(data,index=False)
                            break
            elif nomor==6:
                            harga=40000
                            listharga.append(harga)
                            nama=("Mangga Golek")
                            listnama.append(nama)
                            subtotal=listharga[i]*listjumlah[i]
                            listsubtotal.append(subtotal)
                            print (jumlah,"Kg",nama,"Rp.",harga, "= Rp.",subtotal)
                            df.iloc[5,1]=Golek-jumlah
                            df.to_csv(data,index=False)
                            break
            elif nomor==7:
                            harga=30000
                            listharga.append(harga)
                            nama=("Mangga Kweni")
                            listnama.append(nama)
                            subtotal=listharga[i]*listjumlah[i]
                            listsubtotal.append(subtotal)
                            print (jumlah,"Kg",nama,"Rp.",harga, "= Rp.",subtotal)
                            df.iloc[6,1]=Kweni-jumlah
                            df.to_csv(data,index=False)
                            break
            elif nomor==8:
                            harga=50000
                            listharga.append(harga)
                            nama=("Mangga Alpukat")
                            listnama.append(nama)
                            subtotal=listharga[i]*listjumlah[i]
                            listsubtotal.append(subtotal)
                            print (jumlah,"Kg",nama,"Rp.",harga, "= Rp.",subtotal)
                            df.iloc[7,1]=Alpukat-jumlah
                            df.to_csv(data,index=False)
                            break
            elif nomor==9:
                            harga=40000
                            listharga.append(harga)
                            nama=("Mangga Gandaria")
                            listnama.append(nama)
                            subtotal=listharga[i]*listjumlah[i]
                            listsubtotal.append(subtotal)
                            print (jumlah,"Kg",nama,"Rp.",harga, "= Rp.",subtotal)
                            df.iloc[8,1]=Gandaria-jumlah
                            df.to_csv(data,index=False)
                            break
            elif nomor==10:
                            harga=40000
                            listharga.append(harga)
                            nama=("Mangga Budiraja")
                            listnama.append(nama)
                            subtotal=listharga[i]*listjumlah[i]
                            listsubtotal.append(subtotal)
                            print (jumlah,"Kg",nama,"Rp.",harga, "= Rp.",subtotal)
                            df.iloc[9,1]=Budiraja-jumlah
                            df.to_csv(data,index=False)
                            break
            elif nomor==11:
                            harga=40000
                            listharga.append(harga)
                            nama=("Mangga Gadung")
                            listnama.append(nama)
                            subtotal=listharga[i]*listjumlah[i]
                            listsubtotal.append(subtotal)
                            print (jumlah,"Kg",nama,"Rp.",harga, "= Rp.",subtotal)
                            df.iloc[10,1]=Gadung-jumlah
                            df.to_csv(data,index=False)
                            break
            else:
                print()
def awal():
    global menu1 
    global x
    menu1=input("Mau pesan? pilih y jika Ya, pilih n jika Tidak (y/n) = ")
    while menu1!='y' and menu1!='n':
        menu1=input("Indikator salah, Silahkan pilih y jika Pesan, dan pilih n jika Tidak (y/n) = ")
    if menu1=="y" :    
        x=int(input("Frekuensi Pesanan: "))

listmangga()
awal()
if menu1=="y" :
    pemesanan()
    
    print("==================================".center(100))
    print("======== P E M B E L I A N =======".center(100))
    print("==================================".center(100))
    for i in range(x):   
        print ("%d Kg   %s\t\t Rp.%d \t : Rp.%d"%(listjumlah[i],listnama[i],listharga[i],listsubtotal[i]))
        totalsemua=totalsemua+listsubtotal[i]
    print("Total harus Dibayar\t                  : Rp.",totalsemua)
    uang=int(input("Uang Tunai Pembeli\t\t          : Rp. "))
    kembalian=int(uang-totalsemua)
    print("\n")
    print("==================================".center(100))
    print("========== M A N G O O D =========".center(100))
    print("==================================".center(100))
    print ("Nama:",pembeli)
    print ("Jumlah\t       Nama\t\t          Harga\t\t           Total")   
    for i in range(x):
        print ("%d Kg    %s\t\t Rp.%d \t\t : Rp.%d"%(listjumlah[i],listnama[i],listharga[i],listsubtotal[i]))
        totalfix=totalsemua
    print ("Total                               : Rp.",totalfix)
    print ("Bayar                               : Rp.",uang)
    print ("Kembali                             : Rp.",kembalian)
    print("Mangga yang sudah dibayar tidak dapat dikembalikan".center(100))
    print("Terima kasih atas kunjungan anda".center(100))
if menu1=='n':
    print('Terima Kasih telah menggunakan program Mangood')