import streamlit as st
import pandas as pd
import pickle
import urllib.request
import io

# --- Load model dari GitHub ---
url = "https://raw.githubusercontent.com/bagusangkasawan/Submission2BPDS-JayaJayaInstitut/main/rf_model.pkl"
response = urllib.request.urlopen(url)
model_file = io.BytesIO(response.read())
loaded_rf_model = pickle.load(model_file)

# --- Setup halaman ---
st.set_page_config(page_title="Prediksi Status Mahasiswa", page_icon="🎓", layout="centered")
st.title("🎓 Prediksi Status Mahasiswa")
st.markdown("Masukkan data berikut untuk mengetahui prediksi status mahasiswa: apakah akan **lulus**, **dropout**, atau masih **terdaftar**.")

st.markdown("### 🧾 Input Data Mahasiswa")

# --- Layout dua kolom ---
col1, col2 = st.columns(2)

with col1:
    cu1_approved = st.number_input(
        label="✅ Jumlah Mata Kuliah Lulus Semester 1",
        help="Contoh: 10",
        min_value=0, value=10, placeholder="e.g. 10")

    cu2_approved = st.number_input(
        label="✅ Jumlah Mata Kuliah Lulus Semester 2",
        help="Contoh: 12",
        min_value=0, value=12, placeholder="e.g. 12")

with col2:
    cu1_grade = st.number_input(
        label="📊 Nilai Rata-rata Semester 1 (0–20)",
        help="Contoh: 14.5",
        min_value=0.0, max_value=20.0, value=14.5, placeholder="e.g. 14.5")

    cu2_grade = st.number_input(
        label="📊 Nilai Rata-rata Semester 2 (0–20)",
        help="Contoh: 15.0",
        min_value=0.0, max_value=20.0, value=15.0, placeholder="e.g. 15.0")

tuition_up_to_date = st.selectbox(
    label="💸 Apakah UKT Sudah Dibayar?",
    options=[1, 0],
    format_func=lambda x: "Sudah Lunas" if x == 1 else "Belum Lunas",
    help="Pilih 'Sudah Lunas' jika mahasiswa tidak menunggak UKT"
)

# --- Prediksi ---
st.markdown("### 🔍 Hasil Prediksi")
if st.button("🎯 Prediksi Status"):
    new_data = {
        'Curricular_units_2nd_sem_approved': [cu2_approved],
        'Curricular_units_1st_sem_approved': [cu1_approved],
        'Curricular_units_2nd_sem_grade': [cu2_grade],
        'Curricular_units_1st_sem_grade': [cu1_grade],
        'Tuition_fees_up_to_date': [tuition_up_to_date]
    }

    new_data_df = pd.DataFrame(new_data)
    prediction_numeric = loaded_rf_model.predict(new_data_df)

    # Mapping hasil
    status_map = {0: "Enrolled", 1: "Dropout", 2: "Graduate"}
    status_color = {"Graduate": "green", "Dropout": "red", "Enrolled": "blue"}

    predicted_status = status_map.get(prediction_numeric[0], "Unknown")
    color = status_color.get(predicted_status, "gray")

    st.markdown(
        f"<h3 style='text-align: center;'>📌 Prediksi: <span style='color:{color}'>{predicted_status}</span></h3>",
        unsafe_allow_html=True
    )

    if predicted_status == "Dropout":
        st.warning("⚠️ Mahasiswa ini berisiko tinggi untuk dropout. Perlu intervensi akademik atau finansial.")
    elif predicted_status == "Graduate":
        st.success("🎉 Mahasiswa diprediksi akan lulus!")
    else:
        st.info("📘 Mahasiswa masih aktif terdaftar.")

# --- Footer ---
st.markdown("---")
st.caption("📌 Model ini menggunakan algoritma Random Forest dan mempertimbangkan 5 fitur utama dari performa awal akademik mahasiswa.")
