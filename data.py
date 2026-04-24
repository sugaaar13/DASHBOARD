import streamlit as st
import pandas as pd
import plotly.express as px  # Tambahkan import plotly

def load_data():
    df = pd.read_csv("dataset/covid_19_indonesia_time_series_all.csv")
    return df

def filter_data(df, year):
    if year == "Semua Tahun":
        return df
    else:
        return df[df['Date'].astype(str).str.startswith(str(year))]

def select_year():
    tahun = st.sidebar.selectbox("Pilih Tahun", ["Semua Tahun", 2020, 2021, 2022])
    return tahun
    
def show_data(df):
    st.subheader("Data Covid-19 Indonesia")
    st.dataframe(df.head(10))

def total_case(df):
    return df["Total Cases"].sum()

def total_death(df):
    return df["Total Deaths"].sum()

def total_recovery(df):
    return df["Total Recovered"].sum()

def kolom(df):
    col1, col2, col3 = st.columns(3)
    
    kasus = total_case(df)
    kematian = total_death(df)
    sembuh = total_recovery(df)
    
    col1.metric("📊 Total Kasus", f"{kasus:,.0f}", border=True)
    col2.metric("💀 Total Kematian", f"{kematian:,.0f}", border=True)
    col3.metric("❤️ Total Sembuh", f"{sembuh:,.0f}", border=True)

# Fungsi Pie Chart
def pie_chart1(df):
    # Pemanggilan data
    total_mati = total_death(df)
    total_sembuh = total_recovery(df)
    
    # Dataframe untuk pie chart
    data = {
        'Status': ['Meninggal', 'Sembuh'],
        'Jumlah': [total_mati, total_sembuh]
    }
    
    fig = px.pie(
        data,
        names='Status',
        values='Jumlah',
        title='Perbandingan Total Kematian VS Total Kesembuhan',
        hole=0.5,  # Membuat donut chart (lubang di tengah)
        color_discrete_sequence=['#ff6459', '#4de89f']  # Merah untuk meninggal, hijau untuk sembuh
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Copyright
st.write("sugarano okto forbiah tamba - 184240004")