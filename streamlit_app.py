import streamlit as st

st.set_page_config(page_title="Limbah Hazard Checker", layout="centered")
st.title("☣️ Limbah Hazard Checker")

st.markdown("""
Aplikasi ini digunakan untuk mengklasifikasikan limbah berbahaya dan beracun (**B3**) berdasarkan **PP No. 74 Tahun 2001**.
Masukkan karakteristik limbah di bawah ini untuk mengecek statusnya.
""")

# Sidebar for input
with st.sidebar:
    st.header("🧪 Karakteristik Limbah")
pH = st.slider("pH Limbah", 0.0, 14.0, 7.0)
logam_berat = st.radio("Apakah mengandung logam berat melebihi ambang batas?", ("Tidak", "Ya"))
mudah_menyala = st.checkbox("Mudah Menyala / Inflamabel")
reaktif = st.checkbox("Reaktif terhadap air / udara")
korosif = st.checkbox("Korosif terhadap logam atau jaringan hidup")
beracun = st.checkbox("Beracun terhadap manusia / lingkungan")

# Tombol klasifikasi
if st.button("🔍 Klasifikasikan Limbah"):
    alasan = []
    is_b3 = False

    if pH < 2 or pH > 12.5:
        alasan.append(f"- pH ekstrem ({pH}) → **Korosif**")
        is_b3 = True
    if logam_berat == "Ya":
        alasan.append("- Mengandung logam berat → **Toksik**")
        is_b3 = True
    if mudah_menyala:
        alasan.append("- Mudah menyala → **Inflamabel**")
        is_b3 = True
    if reaktif:
        alasan.append("- Reaktif terhadap air/udara → **Reaktif**")
        is_b3 = True
    if korosif:
        alasan.append("- Bersifat korosif → **Korosif**")
        is_b3 = True
    if beracun:
        alasan.append("- Bersifat racun → **Toksik**")
        is_b3 = True

    if is_b3:
        st.error("⚠️ Limbah ini dikategorikan sebagai **Limbah B3**.")
        st.markdown("### 🧾 Alasan Klasifikasi:")
        st.markdown("\n".join(alasan))

        st.markdown("### ♻️ Rekomendasi Pengolahan:")
        st.markdown("""
        - 🔥 **Insinerasi** untuk limbah inflamabel atau beracun.
        - 🧪 **Stabilisasi/Solidifikasi** untuk logam berat atau lumpur.
        - 🧊 **Netralisasi** untuk limbah asam atau basa ekstrem.
        - 🚛 **Landfilling khusus B3** untuk residu hasil pengolahan.
        """)
    else:
        st.success("✅ Limbah ini **bukan** termasuk kategori B3 menurut parameter yang dimasukkan.")

        st.markdown("### ♻️ Rekomendasi:")
        st.markdown("- Dapat diolah sebagai limbah domestik biasa sesuai peraturan lokal.")
