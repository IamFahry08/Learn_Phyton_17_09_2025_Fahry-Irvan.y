# 1. Variabel dan Tipe Data
# Tipe data int
a = 3
print(type(a))
# Tipe Data Float
b = 2.5
print(type(b))
# Tipe Data String
c = "haickall"
print(type(c))
# List
Nama = ["Fahry", "Fara", "Bara", "Haikal"]
print(type(Nama))

# 2. List dan Manipulasi
# LIST DATA BELANJA
Barang_Belanjaan = ["Beras", "Minyak", "Telur"]
Barang_Belanjaan.append("gula") 
Barang_Belanjaan.append("Kopi")
print("Daftar Belanjaan:", Barang_Belanjaan)
# Tampilkan dengan perulangan
for barang in Barang_Belanjaan:
    print("Item:", barang)

# 3. Dictionary
harga = {
    "Beras": 12000,
    "Minyak": 17000,
    "Telur": 24000,
    "Gula": 15000,
    "Kopi": 20000
}
# Hitung total harga
total = sum(harga.values())
print("Daftar Harga:", harga)
print("Total Harga Belanjaan:", total)

# 4. Fungsi
def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling
p = 10
l = 5
luas, kel = persegi_panjang(p, l)
print(f"Panjang={p}, Lebar={l}")
print("Luas Persegi Panjang:", luas)
print("Keliling Persegi Panjang:", kel)

print("\n--- PERCABANGAN ---")
# 5. Percabangan
usia = int(input("Masukkan usia: "))

if 0 <= usia <= 13:
    print("Kategori: Anak")
elif 14 <= usia <= 24:
    print("Kategori: Remaja")
elif 25 <= usia <= 49:
    print("Kategori: Dewasa")
elif usia >= 50:
    print("Kategori: Lansia")
else:
    print("Usia tidak valid!")
