class Kelas:
    def __init__(self, nama):
        self.__nama = nama

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nama_baru):
        self.__nama = nama_baru

# Buat objek dari kelas
objek_kelas = Kelas("Budi")

# Dapatkan nilai nama
print(objek_kelas.nama)

# Ubah nilai nama melalui setter
objek_kelas.nama = "Andi"

# Dapatkan nilai nama setelah diubah
print(objek_kelas.nama)
