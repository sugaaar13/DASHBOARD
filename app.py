import streamlit as st
from data import *

def judul():
    st.title("📊 Dashboard COVID-19")
    st.markdown("Selamat datang di dashboard interaktif untuk menganalisis data covid-19 di Indonesia")
    
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman Data"])

# Halaman HOME
if menu == "Home":
    judul()
    # Pilih tahun
    year = select_year()
    # Load & filter data
    df = load_data()
    df_filtered = filter_data(df, year)
    
    # Tampilkan metrik (3 kolom)
    kolom(df_filtered)
    
    # Tambahkan pie chart di sini
    st.markdown("---")  # Garis pemisah
    st.subheader("📈 Visualisasi Perbandingan Data")
    pie_chart1(df_filtered)  # Panggil fungsi pie chart

# Halaman Data
elif menu == "Halaman Data":
    judul()
    # Pilih tahun
    year = select_year()
    # Load & filter data
    df = load_data()
    df_filtered = filter_data(df, year)
    show_data(df_filtered)