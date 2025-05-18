# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan lembaga pendidikan tinggi yang berdiri sejak tahun 2000. Meskipun telah menghasilkan banyak lulusan, institusi ini menghadapi masalah signifikan berupa **tingginya angka mahasiswa yang dropout** atau tidak menyelesaikan pendidikan. Hal ini dapat merusak reputasi, mempengaruhi pendapatan institusi, serta menurunkan efisiensi sistem pendidikan.

Pihak manajemen ingin **mendeteksi potensi dropout lebih awal** dengan memanfaatkan data akademik dan sosial mahasiswa, agar mereka bisa melakukan intervensi yang tepat waktu.

### Permasalahan Bisnis

* Tingginya jumlah mahasiswa yang mengalami dropout.
* Sulitnya mendeteksi mahasiswa yang berisiko dropout secara dini.
* Tidak adanya sistem prediktif berbasis data untuk memantau performa dan risiko mahasiswa.
* Minimnya dukungan dashboard interaktif untuk pengambilan keputusan akademik.

### Cakupan Proyek

* Melakukan analisis terhadap variabel-variabel penting yang berkorelasi dengan risiko dropout.
* Membangun model machine learning untuk memprediksi status akhir mahasiswa (lulus, dropout, atau masih aktif).
* Menyusun dashboard interaktif yang menampilkan performa dan tren dropout mahasiswa.
* Menyediakan prototipe aplikasi prediksi yang bisa digunakan oleh staf akademik.

### Persiapan

**Sumber data:**
Dataset publik dari Dicoding Academy:
[https://github.com/dicodingacademy/dicoding\_dataset/blob/main/students\_performance/data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

**Setup environment:**

```bash
pip install -r requirements.txt
```

---

## Business Dashboard

Dashboard ini dirancang untuk menampilkan metrik penting seperti:

* Distribusi status mahasiswa (Lulus, Dropout, Terdaftar)
* Korelasi antara usia, gender, dan performa akademik terhadap dropout
* Dampak status pembayaran terhadap risiko dropout

Dashboard dapat digunakan oleh pihak akademik untuk memantau kondisi mahasiswa secara real-time dan melakukan intervensi jika diperlukan.

---

## Menjalankan Sistem Machine Learning

Sistem machine learning dibangun menggunakan algoritma **Random Forest Classifier** yang dilatih pada 5 fitur utama:

* Curricular\_units\_2nd\_sem\_approved
* Curricular\_units\_1st\_sem\_approved
* Curricular\_units\_2nd\_sem\_grade
* Curricular\_units\_1st\_sem\_grade
* Tuition\_fees\_up\_to\_date

Sistem ini mampu mengklasifikasikan apakah seorang mahasiswa kemungkinan akan **dropout**, **lulus**, atau masih **terdaftar**.

**Link prototipe aplikasi (Streamlit):**
[https://submission2bpds-jayajayainstitut.streamlit.app/](https://submission2bpds-jayajayainstitut.streamlit.app/)

Cara menjalankan di lokal:

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Conclusion

Model machine learning yang dikembangkan menunjukkan performa yang baik dalam memprediksi status mahasiswa. Analisis menunjukkan bahwa mahasiswa yang memiliki usia 20–25 tahun, perempuan, tidak menerima beasiswa, dan mengalami penurunan nilai pada semester kedua, memiliki kemungkinan lebih tinggi untuk dropout.

Proyek ini memberikan solusi berbasis data untuk membantu institusi dalam memantau dan menanggulangi risiko dropout secara sistematis.

### Rekomendasi Action Items

* Menjalankan program pembinaan dini bagi mahasiswa usia 20–25 tahun.
* Menyediakan dukungan akademik dan psikologis bagi mahasiswi.
* Memperluas cakupan program beasiswa untuk mendukung mahasiswa secara finansial.
* Menggunakan dashboard secara berkala untuk memantau performa dan risiko mahasiswa.
* Melakukan evaluasi rutin terhadap performa mahasiswa semester awal untuk mendeteksi risiko lebih awal.
