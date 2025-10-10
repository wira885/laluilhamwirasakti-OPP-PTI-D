import time
import random

class Motor:
    def __init__(self, nama, cc):
        self.nama = nama
        self.cc = cc
        self.kecepatan = 0
        self.waktu_tempuh = 0
        self.nitro = 3  # jumlah nitro yang bisa dipakai
        self.selesai = False

    def gas(self):
        # Semakin besar CC, semakin cepat akselerasi
        percepatan = random.randint(30, 60) if self.cc >= 2000 else random.randint(10, 25)
        self.kecepatan += percepatan
        if self.kecepatan > 400:
            self.kecepatan = 400  # batas kecepatan maksimum

    def gunakan_nitro(self):
        if self.nitro > 0:
            self.kecepatan += 100  # efek nitro besar di mesin 2000cc
            if self.kecepatan > 450:
                self.kecepatan = 450
            self.nitro -= 1
            print(f"💥 {self.nama} menggunakan NITRO! Kecepatan sekarang {self.kecepatan} km/jam")
        else:
            print("⚠️ Nitro habis!")

    def update_waktu(self, detik):
        self.waktu_tempuh += detik
        if self.waktu_tempuh >= 10:  # simulasi lintasan 10 detik
            self.selesai = True


# Membuat motor NMAX Drag 2000cc
motor1 = Motor("Yamaha NMAX Drag 2000cc", 2000)

print("🏁 BALAPAN DIMULAI 🏁\n")

while not motor1.selesai:
    time.sleep(1)
    aksi = random.choice(["gas", "nitro", "gas", "gas"])  # lebih sering gas
    if aksi == "gas":
        motor1.gas()
    elif aksi == "nitro":
        motor1.gunakan_nitro()

    motor1.update_waktu(1)
    print(f"{motor1.nama} → Kecepatan: {motor1.kecepatan} km/jam | Waktu: {motor1.waktu_tempuh:.1f} detik")

print("\n🏆 BALAPAN SELESAI 🏆")
print(f"Nama Motor     : {motor1.nama}")
print(f"Kapasitas Mesin: {motor1.cc} cc")
print(f"Kecepatan Akhir: {motor1.kecepatan} km/jam")
print(f"Waktu Tempuh   : {motor1.waktu_tempuh:.1f} detik")
print("🔥 Drag Race Berakhir 🔥")

