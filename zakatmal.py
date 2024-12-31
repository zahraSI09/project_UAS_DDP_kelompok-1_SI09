import streamlit as st

def hitung_zakat(jenis_harta, jumlah_harta):
    nisab = 0  # Tentukan nisab sesuai jenis harta
    if jenis_harta == "uang":
        nisab = 850000  # Contoh nisab untuk uang
    elif jenis_harta == "emas":
        nisab = 85  # Contoh nisab untuk emas (dalam gram)
    
    if jumlah_harta >= nisab:
        zakat = jumlah_harta * 0.025  # 2.5% zakat
        return zakat
    else:
        return 0

# Judul aplikasi
st.title("Perhitungan Zakat Mal")

# Input dari pengguna
jenis_harta = st.selectbox("Pilih jenis harta:", ["uang", "emas"])
jumlah_harta = st.number_input("Masukkan jumlah harta:", min_value=0.0)

# Tombol untuk menghitung zakat
if st.button("Hitung Zakat"):
    zakat = hitung_zakat(jenis_harta, jumlah_harta)
    if zakat > 0:
        st.success(f"Zakat yang harus dikeluarkan: {zakat:.2f}")
    else:
        st.warning("Anda tidak wajib mengeluarkan zakat.")