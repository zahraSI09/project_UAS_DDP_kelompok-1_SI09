import streamlit  as st

Dashboard = st.Page("./fitur/Dashboard.py", title="Pencatatan Zakat", icon=":material/start:",
    default=True,
) 
Layanan_Utama = st.Page("./fitur/LayananUtama.py", title="LayananUtama",icon=":material/start:",)
zakat_fitrah = st.Page("./fitur/zakatfitrah.py", title="Zakat fitrah", icon=":material/toggle_on:",
)
zakat_mal = st.Page("./fitur/zakatmal.py", title="Zakat Mal", icon=":material/toggle_on:",)
Warisan = st.Page("./fitur/warisan.py", title="Warisan", icon=":material/toggle_on:",)
About = st.Page("./fitur/About.py", title="About", icon=":material/start:",)


st.markdown("<h1 style='text-align: center; color:blue;'>✨Welcome To Aplication Zakat✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: green;'>Zakat lebih mudah,aman, dan terpercaya hanya disini!</p>", unsafe_allow_html=True)
st.write("---")

pg = st.navigation(
    {
        "Dashboard": [About, Dashboard],
        "Layanan Utama": [zakat_fitrah, zakat_mal, Warisan, ]  
    } 
)

# --- SHARED ON ALL PAGES ---
st.logo("zakat.png")
st.sidebar.markdown("✨ Project UAS DDP Semester 1 ✨")

pg.run()


