from pymongo import MongoClient

# Koneksi ke MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['perpustakaan']  # Ganti dengan nama database yang diinginkan
koleksi_buku = db['buku']

# Menambahkan dokumen ke dalam koleksi "buku"
buku_data = [
    {
        "judul": "Belajar Python",
        "pengarang": "John Doe",
        "tahun": 2021,
        "stok": 10
    },
    {
        "judul": "Dasar-Dasar MongoDB",
        "pengarang": "Jane Smith",
        "tahun": 2020,
        "stok": 5
    },
    {
        "judul": "Pemrograman Web dengan Flask",
        "pengarang": "Alice Johnson",
        "tahun": 2022,
        "stok": 8
    }
]

# Menyisipkan data ke dalam koleksi
koleksi_buku.insert_many(buku_data)

# Menampilkan semua data buku
for buku in koleksi_buku.find():
    print(buku)