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
Dataset publik **"Students' Academic Performance and Dropout Prediction"** dari Dicoding Academy
[https://github.com/dicodingacademy/dicoding\_dataset/blob/main/students\_performance/data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

**Penjelasan:**
Dataset ini dikembangkan dari institusi pendidikan tinggi dan dikumpulkan dari beberapa basis data yang terpisah. Data ini berisi informasi mengenai mahasiswa yang terdaftar dalam berbagai program studi sarjana seperti agronomi, desain, pendidikan, keperawatan, jurnalisme, manajemen, layanan sosial, dan teknologi.
Informasi yang disertakan mencakup data yang tersedia saat awal pendaftaran mahasiswa, seperti jalur akademik, faktor demografi, dan sosial-ekonomi. Selain itu, juga tersedia catatan kinerja akademik mahasiswa pada akhir semester pertama dan kedua.
Tujuan utama penggunaan dataset ini adalah untuk membangun model klasifikasi yang mampu memprediksi kemungkinan mahasiswa mengalami *dropout* (berhenti kuliah) atau mencapai keberhasilan akademik.

**Setup Environment - Anaconda**
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

**Setup Environment - Shell/Terminal**
```bash
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

---

## Business Dashboard

Dashboard ini dirancang untuk menampilkan metrik penting seperti:

* Distribusi status mahasiswa (Lulus, Dropout, Terdaftar)
* Korelasi antara usia, gender, dan performa akademik terhadap dropout
* Dampak status pembayaran terhadap risiko dropout

Dashboard dapat digunakan oleh pihak akademik untuk memantau kondisi mahasiswa secara real-time dan melakukan intervensi jika diperlukan.


### Cara Menjalankan Dashboard

#### **Opsi 1: Menggunakan Docker CLI**

1. Siapkan folder `metabase-data/` dan simpan file `metabase.db.mv.db` di dalamnya.
2. Jalankan perintah berikut di terminal:

```bash
docker run -d -p 3000:3000 \
  -v $(pwd)/metabase-data:/metabase-data \
  -e MB_DB_TYPE=h2 \
  -e MB_DB_FILE=/metabase-data/metabase.db \
  --name metabase metabase/metabase
```

> **Catatan (Windows CMD):** Ganti `$(pwd)` dengan path absolut, misalnya:
> `-v C:\Users\NamaUser\metabase-data:/metabase-data`

3. Akses dashboard di browser:
   ```
   http://localhost:3000
   ```

4. Login dengan:

   * **Email:** `root@mail.com`
   * **Password:** `root123`

---

#### **Opsi 2: Menggunakan Docker Desktop (GUI)**

1. **Buka Docker Desktop**.

2. Klik tab **Containers**, lalu klik **+ Create** > pilih **Image**: `metabase/metabase`.

3. Klik **Optional Settings** dan atur:

   * **Container Name:** `metabase`
   * **Port:** `3000` (host) → `3000` (container)
   * **Volume:**

     * Host: arahkan ke folder lokal `metabase-data/` (harus berisi `metabase.db.mv.db`)
     * Container: `/metabase-data`
   * **Environment Variables:**

     * `MB_DB_TYPE=h2`
     * `MB_DB_FILE=/metabase-data/metabase.db`

4. Klik **Run**.

5. Buka browser dan akses:
   ```
   http://localhost:3000
   ```

6. Login dengan:

   * **Email:** `root@mail.com`
   * **Password:** `root123`

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
