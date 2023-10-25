#materi list
profilKendaraan = ["r15","motor","150cc","biru",2]
profilKendaraan.append(20000000)
profilKendaraan.append("Motor Sport")
profilKendaraan.insert(2,"Yamaha")
print(profilKendaraan)

print()

#materi matchcase
soal = int(input ("Menghitung Luas Bangun Datar  (pilih dari 1-3) :"))
match soal:
    case 1:
        print("Menghitung luas Persegi")
        sisiPersegi = int(input("Masukan sisi :"))
        luasPersegi = sisiPersegi * sisiPersegi
        print("Luas Persegi = " , luasPersegi)
    case 2:
        print("Menghitung Luas Lingkaran\n")
        jariJariLingkaran = int(input("Masukan Jari jari Lingkaran : "))
        luasLingkaran = 3.14 * jariJariLingkaran * jariJariLingkaran
        print ("Luas Lingkaran = ", float(luasLingkaran))
    case 3:
        print("Menghitung Luas Segitiga")
        alasSegitiga = int(input("Masukan Alas Segitiga :"))
        tinggiSegitiga = int(input("Masukan Tinggi Segitiga :"))
        luasSegitiga = 1/2 * alasSegitiga * tinggiSegitiga
        print("Luas Segitiga = " , int(luasSegitiga))

