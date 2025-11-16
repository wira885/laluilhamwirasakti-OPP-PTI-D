# class parent
class Mhs_alumni:
    def __init__(self):
        self.tahun_lulus = 2025

class Mhs_aktif:
    def __init__(self):
        self.tahun_masuk = 2024

# class child (multiple inheritance)
class Mahasiswa(Mhs_alumni, Mhs_aktif):
    def __init__(self, nama):
        Mhs_alumni.__init__(self)
        Mhs_aktif.__init__(self)
        self.nama = nama
        self.ktm = True
        self.ijazah = False
        self.beasiswa = False

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Tahun Masuk: {self.tahun_masuk}")
        print(f"Tahun Lulus: {self.tahun_lulus}")
        print(f"KTM: {self.ktm}")
        print(f"Ijazah: {self.ijazah}")
        print(f"Beasiswa: {self.beasiswa}")

# contoh class multilevel
class Mahasiswa_Beasiswa(Mahasiswa):
    def __init__(self, nama, jenis_beasiswa):
        super().__init__(nama)
        self.beasiswa = jenis_beasiswa

    def info_beasiswa(self):
        print(f"Mahasiswa {self.nama} menerima beasiswa {self.beasiswa}")

# contoh penggunaan
m = Mahasiswa_Beasiswa("Budi", "KIP")
m.info()
m.info_beasiswa()
