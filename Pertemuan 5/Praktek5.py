a = [1,2,3,4,5]
nama = ["nanda","ical","igun"]
profil = ["1234", "aiko",20,33,111]
print(profil)

a.append("layla")
nama.insert(2,'ijal')
print(a)
print(nama)

print()

cuaca = input ("Apakah Cuaca Hari ini?")
match cuaca:
    case "panas" | "Panas" | "PANAS" :
        print("jangan lupa minum air putih")
    case "dingin":
        print("jangan lupa minum air putih")
    case _:
        print("jawab dong")