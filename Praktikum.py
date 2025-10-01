# ===============================
# Casting Tipe Data
# ===============================

# konversi dari string ke integer
angka_str = "456"
angka_str_ke_int = int(angka_str)
print("Sebelum casting :", angka_str, ", tipe datanya adalah", type(angka_str))
print("Setelah casting :", angka_str_ke_int, ", tipe datanya adalah", type(angka_str_ke_int))

# konversi dari integer ke string
angka_int = 12345
angka_int_ke_str = str(angka_int)
print("Sebelum casting :", angka_int, ", tipe datanya adalah", type(angka_int))
print("Setelah casting :", angka_int_ke_str, ", tipe datanya adalah", type(angka_int_ke_str))

# konversi dari integer ke boolean
num_int = 1
num_bool = bool(num_int)
print(num_bool, type(num_bool))

num_int = 0
num_bool = bool(num_int)
print(num_bool, type(num_bool))


# ===============================
# Operator Perbandingan
# ===============================
print(8 == 8)   # Sama dengan
print(8 != 9)   # Tidak sama dengan
print(8 > 9)    # Lebih besar
print(8 < 9)    # Lebih kecil
print(8 <= 9)   # Lebih kecil atau sama
print(9 >= 9)   # Lebih besar atau sama


# ===============================
# Operator Logika
# ===============================
a = True
b = True
print(a and b)
print(a or b)
print(not b)

# contoh logika
print(5 > 6 and 6 < 7)


# ===============================
# Operator Aritmatika
# ===============================
e = 8
f = 2

# Penjumlahan
jumlah = e + f
print(f"Hasil penjumlahan e + f adalah : {jumlah}\n")

# Pengurangan
kurang = e - f
print(f"Hasil pengurangan e - f adalah : {kurang}\n")

# Perkalian
kali = e * f
print(f"Hasil perkalian e * f adalah : {kali}\n")

# Pembagian
bagi = e / f
print(f"Hasil pembagian e / f adalah : {bagi}\n")

# Modulus
sisa = e % f
print(f"Sisa hasil bagi e % f adalah : {sisa}\n")

# Pangkat
pangkat = e ** f
print(f"Hasil pemangkatan e ** f adalah : {pangkat}\n")


# ===============================
# Input & Output
# ===============================
nama = str(input("Siapa namamu : "))
usia = int(input("Berapa usiamu : "))

print("Nama: ", nama)
print("Usia: ", usia)

# Variasi output
print('Halo semuanya! Nama saya', nama, 'usia', usia, 'tahun')
print(f'Halo semuanya! Nama saya {nama} usia {usia} tahun')
print("Halo semuanya! Nama saya %s usia %d tahun" % (nama, usia))

print(30*"=")
print("Program Kalkulator Suhu")
print(30*"=")


# ===============================
# Kondisional & Exception Handling
# ===============================
try:
    ipk = float(input("Masukkan nilai IPK: "))
    if 4.0 >= ipk >= 0.0:
        if 4.0 >= ipk >= 3.80:
            print(f"Wihh kamu lulus dengan predikat magna cumlaude! IPK: {ipk}")
        elif 3.50 <= ipk < 3.80:
            print(f"Keren!! Kamu cumlaude dengan IPK {ipk}")
        elif 3.00 <= ipk < 3.50:
            print(f"IPK kamu stabil, bagus 👍")
        elif ipk < 3.0:
            print(f"Kamu harus lebih giat belajar, IPK kamu {ipk}")
    else:
        print(f"Maaf, nilai IPK {ipk} tidak valid")
except:
    print("Harap masukkan IPK yang benar")

# match-case
try:
    kode_status = int(input("Masukkan kode status: "))
    print("Arti kode status:")
    match kode_status:
        case 200:
            print("Berhasil!")
        case 400:
            print("Bad Request (Permintaan Salah)")
        case 401:
            print("Unauthorized (Tidak memiliki izin)")
        case 402:
            print("Payment Required (Butuh pembayaran)")
        case 403:
            print("Forbidden (Dilarang)")
        case 404:
            print("Not Found (Tidak ditemukan)")
        case 500:
            print("Internal Server Error (Kesalahan server)")
except:
    print("Harap masukkan kode status yang valid")

# Operator ternary
a = 3
b = "Bilangan Genap" if a % 2 == 0 else "Bilangan Ganjil"
print(b)


# ===============================
# Perulangan
# ===============================
for i in range(5):
    print(i)

# For loop dengan range
for i in range(5):
    print("Belajar Python itu mudah!")

print(50*"=")

for i in range(1, 5, 2):
    print("Belajar Python itu menyenangkan!")

# Looping string
kata = "Saya ingin menguasai data science"
for huruf in kata:
    print(huruf)

# Menggunakan enumerate
for indeks, huruf in enumerate(kata):
    print(f"Indeks {indeks}. {huruf}")

# Loop mundur
for i in range(5, 1, -1):
    print("Saya ingin belajar big data")

# Keyword control
for i in range(5):
    if i == 2:
        continue  # lewati ketika i = 2
    if i == 4:
        break     # hentikan loop ketika i = 4
    print(i)

# While loop
hitung = 0
while hitung < 4:
    print("Tetap semangat belajar Python!")
    hitung += 1
