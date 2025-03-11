#123140149_Fadzilah-Saputri_PBO-RA
#Tugas2-Latihan

class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info(self):
        return f"Kendaraan: {self.merk}, Tahun: {self.tahun}"

class Mobil(Kendaraan):
    def __init__(self, merk, tahun, jenis_bahan_bakar):
        super().__init__(merk, tahun)
        self.jenis_bahan_bakar = jenis_bahan_bakar

    def info(self):
        return f"Mobil: {self.merk}, Tahun: {self.tahun}, Bahan Bakar: {self.jenis_bahan_bakar}"

class MobilSport(Mobil):
    def __init__(self, merk, tahun, jenis_bahan_bakar, kecepatan_maksimum):
        super().__init__(merk, tahun, jenis_bahan_bakar)
        self.__kecepatan_maksimum = kecepatan_maksimum  

    def get_kecepatan_maksimum(self):
        return self.__kecepatan_maksimum

    def set_kecepatan_maksimum(self, kecepatan):
        if kecepatan > 0:
            self.__kecepatan_maksimum = kecepatan
        else:
            print("Kecepatan maksimum harus lebih dari 0!")

    def info(self):
        return (f"Mobil Sport: {self.merk}, Tahun: {self.tahun}, "
                f"Bahan Bakar: {self.jenis_bahan_bakar}, "
                f"Kecepatan Maksimum: {self.__kecepatan_maksimum} km/jam")
#contoh penggunaannya
mobil_sport = MobilSport("Ferrari", 2022, "Bensin", 350)
#mengakses informasi kendaraan
print(mobil_sport.info())
#menggunakan getter untuk mendapatkan kecepatan maksimum
print("Kecepatan Maksimum:", mobil_sport.get_kecepatan_maksimum())
#menggunakan setter untuk mengubah kecepatan maksimum
mobil_sport.set_kecepatan_maksimum(400)
print("Kecepatan Maksimum setelah diubah:", mobil_sport.get_kecepatan_maksimum())
#jika kita memasukkan nilai yg tidak valid
mobil_sport.set_kecepatan_maksimum(-50) 