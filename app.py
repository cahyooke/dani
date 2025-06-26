import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediksi Pasien Liver", layout="centered")
st.title("🩺 Prediksi Status Pasien Liver")
st.markdown("Silakan masukkan data pasien di bawah ini:")

# Form input data pasien
with st.form("form_pasien"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=1, max_value=100, value=45)
    tb = st.number_input("TB (Total Bilirubin)", value=1.0)
    db = st.number_input("DB (Direct Bilirubin)", value=0.5)
    alkphos = st.number_input("ALKPHOS (Alkaline Phosphotase)", value=200)
    sgpt = st.number_input("SGPT (Alanine Aminotransferase)", value=40)
    sgot = st.number_input("SGOT (Aspartate Aminotransferase)", value=50)
    tp = st.number_input("TP (Total Protein)", value=6.5)
    alb = st.number_input("ALB (Albumin)", value=3.0)
    ag_ratio = st.number_input("A/G Ratio", value=1.0)
    
    submit = st.form_submit_button("🔍 Prediksi Status Pasien")

# Load model
try:
    model = joblib.load("model_ilpd_knn.pkl")
except Exception as e:
    st.error("❌ Gagal memuat model.")
    st.exception(e)
    st.stop()

# Prediksi saat tombol ditekan
if submit:
    try:
        input_data = pd.DataFrame([{
            'Age': age,
            'Gender': 1 if gender == "Male" else 0,
            'TB': tb,
            'DB': db,
            'Alkphos': alkphos,
            'SGPT': sgpt,
            'SGOT': sgot,
            'TP': tp,
            'ALB': alb,
            'AG_Ratio': ag_ratio
        }])

        prediction = model.predict(input_data)[0]
        if prediction == 1:
            st.success("✅ Hasil: Pasien **terindikasi sehat**.")
        else:
            st.warning("⚠️ Hasil: Pasien **terindikasi memiliki penyakit liver**.")
    except Exception as e:
        st.error("❌ Gagal melakukan prediksi.")
        st.exception(e)
