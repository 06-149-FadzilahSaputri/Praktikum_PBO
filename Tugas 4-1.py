import math

while True:
    try:
        angka = input("Masukkan angka: ")
        angka = float(angka)

        if angka < 0:
            print("Input tidak valid. Harap masukkan angka positif.")
        elif angka == 0:
            raise ValueError("Akar kuadrat dari nol tidak diperbolehkan.")
        else:
            akar = math.sqrt(angka)
            print(f"Akar kuadrat dari {angka} adalah {akar}")
            break

    except ValueError as e:
        if str(e) == "could not convert string to float: '{}'".format(angka):
            print("Input tidak valid. Harap masukkan angka yang valid.")
        else:
            print(f"Error: {e}")
