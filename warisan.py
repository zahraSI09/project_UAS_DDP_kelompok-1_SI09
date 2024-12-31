import streamlit as st

def hitung_waris(total_harta, jumlah_anak_laki, jumlah_anak_perempuan, ada_istri=False, ada_suami=False):
    # Inisialisasi variabel
    hasil = {}
    
    # Aturan dasar pembagian waris
    if ada_istri and ada_suami:
        st.error("Hanya bisa ada satu pasangan (istri atau suami).")
        return
    
    # Hitung bagian pasangan
    if ada_istri:
        bagian_istri = total_harta * 0.25  # Istri mendapatkan 1/4
        total_harta -= bagian_istri
        hasil['Bagian Istri'] = bagian_istri
    elif ada_suami:
        bagian_suami = total_harta * 0.25  # Suami mendapatkan 1/4
        total_harta -= bagian_suami
        hasil['Bagian Suami'] = bagian_suami

    # Hitung bagian anak
    total_anak = jumlah_anak_laki + jumlah_anak_perempuan
    if total_anak > 0:
        # Bagian anak laki-laki mendapatkan 2 kali bagian anak perempuan
        bagian_perempuan = total_harta / (jumlah_anak_laki * 2 + jumlah_anak_perempuan)
        bagian_laki = bagian_perempuan * 2
        
        # Hitung total bagian untuk anak laki-laki dan perempuan
        hasil['Bagian Anak Laki-laki'] = bagian_laki
        hasil['Bagian Anak Perempuan'] = bagian_perempuan
        hasil['Total Bagian Anak Laki-laki'] = bagian_laki * jumlah_anak_laki
        hasil['Total Bagian Anak Perempuan'] = bagian_perempuan * jumlah_anak_perempuan
    else:
        hasil['Tidak ada anak'] = "Tidak ada anak untuk dibagikan."

    return hasil

# Input dari pengguna
st.title("Hitung Ahli Waris")
total_harta = st.number_input("Total Harta (Rp)", min_value=1)
jumlah_anak_laki = st.number_input("Jumlah Anak Laki-laki", min_value=0)
jumlah_anak_perempuan = st.number_input("Jumlah Anak Perempuan", min_value=0)
ada_istri = st.checkbox("Ada Istri")
ada_suami = st.checkbox("Ada Suami")

# Tombol hitung
if st.button("Hitung"):
    hasil = hitung_waris(total_harta, jumlah_anak_laki, jumlah_anak_perempuan, ada_istri, ada_suami)

    # Tampilkan hasil
    for k, v in hasil.items():
        if isinstance(v, (int, float)):
            st.write(f"{k}: Rp {v:,.0f}")
        else:
            st.write(f"{k}: {v}")