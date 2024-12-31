import streamlit as st
import csv
from datetime import datetime

# Fungsi untuk mencatat zakat ke dalam file CSV
def catat_zakat(tanggal, jenis_zakat, jumlah, penerima):
    with open('riwayat_zakat.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tanggal, jenis_zakat, jumlah, penerima])

# Judul Aplikasi
st.title("Pencatatan Zakat")

# Input dari pengguna
tanggal = datetime.now().strftime("%Y-%m-%d")
jenis_zakat = st.selectbox("Pilih jenis zakat:", ["fitrah", "mal"])
jumlah = st.number_input("Masukkan jumlah zakat:", min_value=0.0, format="%.2f")
penerima = st.text_input("Masukkan nama penerima:")

# Tombol untuk mencatat zakat
if st.button("Catat Zakat"):
    if penerima:
        catat_zakat(tanggal, jenis_zakat, jumlah, penerima)
        st.success("Data zakat berhasil dicatat.")
    else:
        st.error("Nama penerima tidak boleh kosong.")