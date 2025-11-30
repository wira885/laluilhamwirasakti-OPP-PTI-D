# Class Buyut
class JenisKelamin:
    def kelamin(self):
        print("Perempuan")

# Class Kakek
class StatusHidup(JenisKelamin):
    def status(self):
        print("Orang ini hidup")

# Class Orang Tua / Mahasiswa sebelum lulus
class MahasiswaAlumni(StatusHidup):
    def masuk(self):
        print("Felicia masuk kuliah tahun 2020")

# Class Anak / Setelah lulus = CEO
class SetelahLulus(MahasiswaAlumni):
    def lulus(self):
        print("Felicia sekarang menjadi CEO")

# --- Program dijalankan ---
felicia = SetelahLulus()

felicia.kelamin()   # dari buyut
felicia.status()    # dari kakek
felicia.masuk()     # sebelum lulus
felicia.lulus()     # setelah lulus
