pelanggan = "Nanda Ilham"
totalBelanja = 100000

if(totalBelanja > 50000):
    keterangan = "Selamat anda mendapatkan diskon"
else:
    keterangan = "terima kasih telah berbelanja"

print("")

    
print("Pelanggan",pelanggan , "\nTotal belanja anda : Rp.",totalBelanja, "\n" , keterangan)

nama ="ical"
matpel = "matkom"
nilai =  76
keterangan = "Lulus" if nilai >= 75 else "Gagal"

print("Nama Siswa \t:", nama,"\nMata Kuliah \t:", matpel,
"\nNilai Matpel \t:", nilai, "\nKeterangan \t:" , keterangan
)

if(nilai >= 85 and nilai <= 100):
    grade = "A"

elif(nilai >= 75 and nilai <=85):
    grade = "B"
elif(nilai >= 60 and nilai <=75):
    grade = "C"
else:
    grade = "E"

print ("Nilai Akreditasi \t:",grade)