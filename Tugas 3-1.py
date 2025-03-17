import math  

class Kalkulator:
    def __init__(self, nilai):
        self.nilai = nilai  

    def __add__(self, other):
        if isinstance(other, Kalkulator):  
            return Kalkulator(self.nilai + other.nilai)  
        else:
            raise TypeError("Operasi hanya bisa dilakukan dengan objek Kalkulator")

    def __sub__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(self.nilai - other.nilai)
        else:
            raise TypeError("Operasi hanya bisa dilakukan dengan objek Kalkulator")

    def __mul__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(self.nilai * other.nilai)
        else:
            raise TypeError("Operasi hanya bisa dilakukan dengan objek Kalkulator")

    def __truediv__(self, other):
        if isinstance(other, Kalkulator):
            if other.nilai == 0:
                raise ZeroDivisionError("Tidak bisa membagi dengan nol")
            return Kalkulator(self.nilai / other.nilai)
        else:
            raise TypeError("Operasi hanya bisa dilakukan dengan objek Kalkulator")

    def __pow__(self, other):
        if isinstance(other, Kalkulator):
            return Kalkulator(self.nilai ** other.nilai)
        else:
            raise TypeError("Operasi hanya bisa dilakukan dengan objek Kalkulator")

    def log(self):
        if self.nilai <= 0:
            raise ValueError("Logaritma hanya bisa dihitung untuk angka positif")
        return Kalkulator(math.log(self.nilai))

    def __str__(self):
        return f"Kalkulator({self.nilai})"

try:
    nilai1 = float(input("Masukkan angka pertama: "))
    nilai2 = float(input("Masukkan angka kedua: "))
    
    angka1 = Kalkulator(nilai1)
    angka2 = Kalkulator(nilai2)

    print("\nPilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Eksponen (^)")
    print("6. Logaritma (hanya angka pertama)")

    pilihan = input("Masukkan pilihan (1-6): ")

    if pilihan == "1":
        print("Hasil:", angka1 + angka2)
    elif pilihan == "2":
        print("Hasil:", angka1 - angka2)
    elif pilihan == "3":
        print("Hasil:", angka1 * angka2)
    elif pilihan == "4":
        print("Hasil:", angka1 / angka2)
    elif pilihan == "5":
        print("Hasil:", angka1 ** angka2)
    elif pilihan == "6":
        print("Hasil:", angka1.log())
    else:
        print("Pilihan tidak valid!")

except ValueError:
    print("Masukkan angka yang valid!")
except Exception as e:
    print("Terjadi kesalahan:", e)
