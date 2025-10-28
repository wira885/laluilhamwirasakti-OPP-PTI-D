import time
import random

class Motor:
    # 🔹 CLASS VARIABLE — sama untuk semua objek
    batas_kecepatan = 450
    total_motor = 0

    def __init__(self, nama, cc):
        # 🔸 INSTANCE VARIABLE — khusus untuk setiap objek
        self.nama = nama
        self.cc = cc
        self.kecepatan = 0
        self.waktu_tempuh = 0
        self.nitro = 3
        self.selesai = False

        # setiap kali motor baru dibuat, total motor bertambah
        Motor.total_motor += 1

    def gas(self):
        # percepatan tergantung CC (instance variable)
        percepatan = random.randint(30, 60) if self.cc >= 2000 else random.randint(10, 25)
        self.kecepatan += percepatan

        # gunakan class variable untuk batas kecepatan
        if self.kecepatan > Motor.batas_kecepatan:
            self.kecepatan = Motor.batas_kecepatan

    def gunakan_nitro(self):
        if self.nitro > 0:
            self.kecepatan += 100
            if self.kecepatan > Motor.batas_kecepatan:
                self.kecepatan = Motor.batas_kecepatan
            self.nitro -= 1
            print(f"💥 {self.nama} menggunakan NITRO! Kecepatan sekarang {self.kecepatan} km/jam")
        else:
            print("⚠ Nitro habis!")

    def update_waktu(self, detik):
        self.waktu_tempuh += detik
        if self.waktu_tempuh >= 10:
            self.selesai = True


# Membuat objek motor (instance)
motor1 = Motor("Yamaha NMAX Drag 2000cc", 2000)

print("🏁 BALAPAN DIMULAI 🏁\n")
print(f"Jumlah motor yang ikut: {Motor.total_motor}\n")

while not motor1.selesai:
    time.sleep(1)
    aksi = random.choice(["gas", "nitro", "gas", "gas"])
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
print(f"Total Motor yang dibuat: {Motor.total_motor}")
print(f"Batas Kecepatan Global: {Motor.batas_kecepatan} km/jam")
print("🔥 Drag Race Berakhir 🔥")
