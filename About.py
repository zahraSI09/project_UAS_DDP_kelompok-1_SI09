import streamlit as st

#menambahkan gambar
st.image("tentang.jpg", caption="Ilustrasi Zakat", use_container_width=1000)

# Pengertian Zakat
st.header("Pengertian Zakat")
st.write("Zakat adalah kewajiban agama dalam Islam untuk memberikan sebagian harta tertentu kepada orang-orang yang berhak menerimanya. Zakat merupakan salah satu dari lima rukun Islam, yang berfungsi sebagai bentuk ibadah sekaligus wujud solidaritas sosial untuk membantu mereka yang membutuhkan..")

# Jenis-jenis Zakat
st.header("Jenis-jenis Zakat")
jenis_zakat = {
    "1. Zakat Fitrah": "zakat yang diwajibkan atas setiap jiwa muslim, baik laki-laki maupun perempuan, yang telah mencapai usia baligh dan memiliki harta lebih dari kebutuhan pokok. Zakat ini dikeluarkan pada bulan Ramadhan sebelum shalat Idul Fitri.",
    "2. Zakat Mal": " kewajiban bagi setiap muslim yang memiliki harta yang telah mencapai nisab (batas minimal harta yang wajib dizakati) dan haul (jangka waktu kepemilikan harta). Zakat mal ini bertujuan untuk membersihkan harta dan mendistribusikannya kepada mereka yang berhak, sehingga tercipta keseimbangan sosial."
}
for jenis, keterangan in jenis_zakat.items():
    st.write(f"- **{jenis}**: {keterangan}")

# Syarat Harta yang Wajib Dizakati
st.header("Syarat Harta yang Wajib Dizakati")
syarat_harta_zakat = [
    "Harta tersebut adalah milik penuh.",
    "Mencapai nisab (batas minimal harta yang wajib dizakati).",
    "Berada dalam kepemilikan selama satu tahun (haul), kecuali hasil pertanian.",
    "Harta diperoleh dengan cara yang halal."
]
for syarat in syarat_harta_zakat:
    st.write(f"- {syarat}")

# Golongan Penerima Zakat
st.header("Golongan Penerima Zakat")
golongan_penerima_zakat = [
    "Fakir",
    "Miskin",
    "Amil (pengelola zakat)",
    "Muallaf (orang yang baru masuk Islam)",
    "Hamba sahaya yang ingin memerdekakan diri",
    "Orang yang berhutang",
    "Fi sabilillah (berjuang di jalan Allah)",
    "Ibnu sabil (musafir yang kehabisan bekal)"
]
for golongan in golongan_penerima_zakat:
    st.write(f"- {golongan}")
    

# menambahkan gambar
st.image("warisan.jpg", caption="Ilustrasi Warisan", use_container_width=1000)
# Pengertian Warisan
st.header("Pengertian Warisan")
st.write("Warisan adalah harta benda, hak, atau kewajiban yang ditinggalkan oleh seseorang yang telah meninggal dunia kepada ahli warisnya. Dalam konteks hukum Islam, warisan juga dikenal sebagai faraidh, yaitu pembagian harta peninggalan pewaris sesuai ketentuan Al-Qur'an dan Hadis.")

st.header("Dalil Tentang Warisan dalam Islam")
st.write("(Surah An-Nisa (4:7) “Bagi laki-laki ada hak bagian dari harta peninggalan ibu-bapak dan kerabatnya, dan bagi perempuan ada hak bagian pula dari harta peninggalan ibu-bapak dan kerabatnya, baik sedikit atau banyak menurut bagian yang telah ditetapkan.“")
st.write("(Surah An-Nisa (4:11) “Allah mensyariatkan bagimu tentang pembagian pusaka untuk anak-anakmu. Yaitu, bagian seorang anak lelaki sama dengan bagian dua orang anak perempuan.“")

# Syarat-syarat terjadinya warisan
st.header("Syarat-Syarat terjadinya Warisan")
syarat_harta_zakat = [
    "Pewaris telah meninggal dunia, baik secara nyata maupun hukum (misalnya dinyatakan meninggal oleh pengadilan).",
    "Hubungan hukum antara pewaris dan ahli waris telah ditetapkan, baik melalui hubungan darah, pernikahan, atau sebab lainnya.",
    "Ahli waris masih hidup pada saat pewaris meninggal dunia."
]
for syarat in syarat_harta_zakat:
    st.write(f"- {syarat}")