#Soal no 1
nama = "bambang"
umur = 20

if(umur <=17):
    kategori = "Anak-Anak"
elif(umur >= 18 and umur <=65 ):
    kategori = "Dewasa"
elif(umur >=65):
    kategori="Lanjut Usia"

print("Nama \t:" , nama ,"\nUmur \t:", umur, "\nKategori \t:", kategori)

print("")
#Soal no 2

bil1 = 14
bil2 = 10

if (bil1 > bil2):
    Hasil = "Bilangan 1 Lebih Besar Dari Bilangan 2"
    
elif(bil1 < bil2):
    Hasil = "Bilangan 1 Lebih Kecil Dari Bilangan 2"

print("Bilangan 1 = ", bil1 , "\nBilangan 2 = ", bil2,
      "\n", Hasil)

