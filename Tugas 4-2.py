class TaskNotFoundError(Exception):
    """Exception untuk tugas yang tidak ditemukan"""
    pass

class TaskManager:
    def __init__(self):
        self.tasks = []

    def tambah_tugas(self, task):
        if not task.strip():
            raise ValueError("Tugas tidak boleh kosong.")
        self.tasks.append(task)
        print("Tugas berhasil ditambahkan!")

    def hapus_tugas(self, index):
        if not self.tasks:
            raise TaskNotFoundError("Daftar tugas kosong.")
        if index < 1 or index > len(self.tasks):
            raise TaskNotFoundError(f"Tugas dengan nomor {index} tidak ditemukan.")
        removed = self.tasks.pop(index - 1)
        print(f"Tugas '{removed}' berhasil dihapus!")

    def tampilkan_tugas(self):
        if not self.tasks:
            print("Daftar tugas kosong.")
        else:
            print("Daftar Tugas:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

def main():
    manager = TaskManager()

    while True:
        print("\nPilih aksi:")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Tampilkan daftar tugas")
        print("4. Keluar")

        try:
            pilihan = int(input("Masukkan pilihan (1/2/3/4): "))
            if pilihan == 1:
                tugas = input("Masukkan tugas yang ingin ditambahkan: ")
                manager.tambah_tugas(tugas)
            elif pilihan == 2:
                try:
                    nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                    manager.hapus_tugas(nomor)
                except ValueError:
                    print("Input harus berupa angka.")
                except TaskNotFoundError as e:
                    print(f"Error: {e}")
            elif pilihan == 3:
                manager.tampilkan_tugas()
            elif pilihan == 4:
                print("Terima kasih telah menggunakan program ini.")
                break
            else:
                raise ValueError("Pilihan tidak valid. Masukkan angka 1-4.")
        except ValueError as ve:
            print(f"Input Error: {ve}")

if __name__ == "__main__":
    main()
