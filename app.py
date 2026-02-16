import streamlit as st

st.set_page_config(page_title="Website Python Saya", page_icon="🚀")

st.title("Selamat Datang di Website Python! 🐍")
st.write("Website ini dihosting gratis menggunakan Streamlit Cloud.")

# Contoh interaksi sederhana
nama = st.text_input("Siapa nama kamu?")
if nama:
    st.success(f"Halo {nama}! Senang bertemu denganmu di dunia maya.")

st.sidebar.info("Dibuat dengan ❤️ menggunakan Python.")
