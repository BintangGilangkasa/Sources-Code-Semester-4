# Analisis Nilai Siswa Menggunakan PySpark
from pyspark import SparkContext

# Inisialisasi SparkContext
sc = SparkContext("local", "AnalisisNilai")

# Data Siswa
data = [("Andi", 90), ("Budi", 75), ("Citra", 85), ("Dewi", 95), ("Eka", 70)]

# Buat RDD dari data
rdd = sc.parallelize(data)

# Ambil hanya nilai
nilai_rdd = rdd.map(lambda x: x[1])

# Hitung jumlah data
jumlah_data = nilai_rdd.count()

# Hitung total nilai
total_nilai = nilai_rdd.sum()

# Hitung rata-rata nilai
rata_rata = total_nilai / jumlah_data

# Hitung jumlah siswa dengan nilai >= 80
jumlah_nilai_80 = nilai_rdd.filter(lambda x: x >= 80).count()

# Output
print("Jumlah Data:", jumlah_data)
print("Total Nilai:", total_nilai)
print("Rata-Rata Nilai:", rata_rata)
print("Jumlah Siswa dengan Nilai >= 80:", jumlah_nilai_80)

sc.stop()