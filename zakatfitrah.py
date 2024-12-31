import streamlit as st

def hitung_zakat_fitrah(jumlah_anggota, harga_per_kg):
    # Nisab zakat fitrah dalam kg
    nisab = 37.5  # kg per orang
    total_zakat = jumlah_anggota * nisab * harga_per_kg
    return total_zakat

# Judul aplikasi
st.title("Penghitung Zakat Fitrah")

# Input dari pengguna
jumlah_anggota = st.number_input("Masukkan jumlah anggota keluarga:", min_value=1, step=1)
harga_per_kg = st.number_input("Masukkan harga makanan pokok per kg:", min_value=0.0, step=0.01)

# Tombol untuk menghitung
if st.button("Hitung Zakat Fitrah"):
    # Menghitung total zakat fitrah
    total_zakat = hitung_zakat_fitrah(jumlah_anggota, harga_per_kg)
    st.success(f"Total zakat fitrah yang harus dikeluarkan: {total_zakat:.2f}")
        

