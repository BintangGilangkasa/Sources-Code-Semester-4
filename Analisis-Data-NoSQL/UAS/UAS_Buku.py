import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["perpustakaan"]
mycol = mydb["buku"]

mycol.insert_many([
    {"judul": "Atomic Habits", "pengarang": "james clear", "tahun": 2018, "stok": 10},
    {"judul": "Laut Bercerita", "pengarang": "Leila S. Chudori", "tahun": 2017, "stok": 5},
    {"judul": "Machine Learning", "pengarang": "Ethem Alpaydin", "tahun": 2016, "stok": 7},
    {"judul": "Garis Waktu", "pengarang": "Fiersa Besari", "tahun": 2019, "stok": 4}
])

# Menampilkan semua data buku
print("Data Buku: ")
for buku in mycol.find():
    print(f"Judul: {buku['judul']}, Pengarang: {buku['pengarang']}, Tahun: {buku['tahun']}, Stok: {buku['stok']}")
