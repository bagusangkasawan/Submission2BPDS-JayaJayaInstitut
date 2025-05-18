import streamlit as st
import pandas as pd
import pickle
import urllib.request
import io

# --- Load model dari GitHub ---
@st.cache_resource
def load_model_from_url(url):
    try:
        response = urllib.request.urlopen(url)
        model_file = io.BytesIO(response.read())
        model = pickle.load(model_file)
        return model
    except Exception as e:
        st.error(f"❌ Gagal memuat model: {e}")
        return None

model_url = "https://raw.githubusercontent.com/bagusangkasawan/Submission2BPDS-JayaJayaInstitut/main/rf_model.pkl"
model = load_model_from_url(model_url)

# --- Fitur yang digunakan saat training ---
top_5_features = [
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_1st_sem_grade',
    'Tuition_fees_up_to_date'
]

# --- UI Aplikasi ---
st.set_page_config(page_title="Prediksi Status Mahasiswa", page_icon="🎓")
st.title("🎓 Prediksi Status Mahasiswa")
st.markdown("Masukkan data berikut untuk mengetahui apakah mahasiswa akan **lulus**, **dropout**, atau masih **terdaftar**.")

st.markdown("### 🧾 Input Data Mahasiswa")
col1, col2 = st.columns(2)

with col1:
    cu1_approved = st.number_input("✅ Mata Kuliah Lulus Semester 1", min_value=0, value=10, help="Contoh: 10")
    cu2_approved = st.number_input("✅ Mata Kuliah Lulus Semester 2", min_value=0, value=12, help="Contoh: 12")

with col2:
    cu1_grade = st.number_input("📊 Nilai Rata-rata Semester 1", min_value=0.0, max_value=20.0, value=14.5, help="Contoh: 14.5")
    cu2_grade = st.number_input("📊 Nilai Rata-rata Semester 2", min_value=0.0, max_value=20.0, value=15.0, help="Contoh: 15.0")

tuition_status = st.selectbox("💸 Status Pembayaran UKT", options=[1, 0], format_func=lambda x: "Sudah Lunas" if x == 1 else "Belum Lunas")

# --- Prediksi ---
st.markdown("### 🔍 Hasil Prediksi")
if st.button("🎯 Prediksi Status"):
    new_data_dict = {
        'Curricular_units_1st_sem_approved': [cu1_approved],
        'Curricular_units_1st_sem_grade': [cu1_grade],
        'Curricular_units_2nd_sem_approved': [cu2_approved],
        'Curricular_units_2nd_sem_grade': [cu2_grade],
        'Tuition_fees_up_to_date': [tuition_status]
    }

    new_data_df = pd.DataFrame(new_data_dict)

    try:
        prediction_numeric = model.predict(new_data_df)
        status_map = {0: "Enrolled", 1: "Dropout", 2: "Graduate"}
        status_color = {"Graduate": "green", "Dropout": "red", "Enrolled": "blue"}
        predicted_status = status_map.get(prediction_numeric[0], "Unknown")
        color = status_color.get(predicted_status, "gray")

        st.markdown(
            f"<h3 style='text-align: center;'>📌 Prediksi: <span style='color:{color}'>{predicted_status}</span></h3>",
            unsafe_allow_html=True
        )

        if predicted_status == "Dropout":
            st.warning("⚠️ Mahasiswa ini berisiko tinggi dropout. Perlu perhatian akademik atau finansial.")
        elif predicted_status == "Graduate":
            st.success("🎉 Mahasiswa diprediksi akan lulus.")
        else:
            st.info("📘 Mahasiswa masih aktif terdaftar.")

    except Exception as e:
        st.error(f"❌ Gagal melakukan prediksi: {e}")

# --- Footer ---
st.markdown("---")
st.caption("🔐 Model menggunakan Random Forest dan hanya mempertimbangkan 5 fitur utama dari performa akademik awal.")
