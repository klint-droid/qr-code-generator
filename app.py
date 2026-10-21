import streamlit as st
import qrcode

st.title("QR Code Generator")

url = st.text_input("Enter URL or Text")

if st.button("Generate"):
    img = qrcode.make(url)
    img.save("qr.png")

    st.image("qr.png")