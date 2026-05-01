import streamlit as st
from data import *

# =========================
# JUDUL
# =========================
def judul():

    st.title("🔴 Dashboard Covid-19 Indonesia")

    st.markdown(
        """
        Selamat datang di dashboard interaktif
        untuk menganalisis data Covid-19
        di Indonesia 🔴⚪
        """
    )


# =========================
# FOOTER
# =========================
def footer():
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**📊 Sumber Data**")
        st.caption("COVID-19 Indonesia Time Series")
    
    with col2:
        st.markdown("**📅 Update Terakhir**")
        st.caption("Data real-time dari sumber resmi")
    
    with col3:
        st.markdown("**👨‍💻 Dibuat oleh**")
        st.caption("Dashboard Analisis COVID-19 Indonesia")
    
    st.markdown(
        "<p style='text-align: center; color: gray; font-size: 12px;'>"
        "© 2024 Dashboard COVID-19 Indonesia | Semua hak dilindungi"
        "</p>",
        unsafe_allow_html=True
    )


# =========================
# SIDEBAR
# =========================
st.sidebar.title("🏙️ Navigasi")

menu = st.sidebar.radio(
    "Pilih Halaman",
    ["Home", "Halaman Data"]
)


# =========================
# HOME
# =========================
if menu == "Home":

    judul()

    # Load data
    df = load_data()

    # Filter
    year = select_year()

    locations = select_location(df)

    # Filter dataframe
    df_filtered = filter_data(
        df,
        year,
        locations
    )

    # Metric
    kolom(df_filtered)

    # Pie chart
    pie_chart1(df_filtered)

    # Bar chart
    bar_chart1(df_filtered)

    # Bar chart
    bar_chart2(df_filtered)

    # Map chart
    map_chart(df_filtered, year)
    
    # Footer
    footer()


# =========================
# HALAMAN DATA
# =========================
elif menu == "Halaman Data":

    judul()

    # Load data
    df = load_data()

    # Filter
    year = select_year()

    locations = select_location(df)

    # Filter dataframe
    df_filtered = filter_data(
        df,
        year,
        locations
    )

    # Show data
    show_data(df_filtered)
    
    # Footer
    footer( "sugarano okto forbiah tamba || 184240004 || sains data - A")