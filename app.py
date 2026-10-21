import streamlit as st
import qrcode
from PIL import Image

logo_file = st.file_uploader(
    "Upload Logo",
    type=["png", "jpg", "jpeg"]
)

st.set_page_config(
    page_title="Smart QR Generator",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Smart QR Generator")
st.write("Generate custom QR codes instantly.")

qr_type = st.selectbox(
    "Select QR Type",
    ["URL", "Email", "Phone", "Text"]
)

user_input = st.text_input("Enter Content")

fill_color = st.color_picker(
    "QR Color",
    "#000000"
)

bg_color = st.color_picker(
    "Background Color",
    "#FFFFFF"
)

if st.button("Generate QR"):

    if not user_input.strip():
        st.error("Please enter a value.")

    else:

        if qr_type == "Email":
            data = f"mailto:{user_input}"
        elif qr_type == "Phone":
            data = f"tel:{user_input}"
        else:
            data = user_input

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(
            fill_color=fill_color,
            back_color=bg_color
        )

        img = img.convert("RGB")

        if logo_file is not None:

            logo = Image.open(logo_file)

            qr_width, qr_height = img.size

            logo_size = qr_width // 4

            logo = logo.resize(
                (logo_size, logo_size)
            )

            pos = (
                (qr_width - logo_size) // 2,
                (qr_height - logo_size) // 2
            )

            img.paste(logo, pos)

        img.save("qr.png")

        st.success("✅ QR Code Generated Successfully!")

        st.image(
            "qr.png",
            caption="Generated QR Code"
        )

        with open("qr.png", "rb") as file:
            st.download_button(
                label="⬇️ Download QR Code",
                data=file,
                file_name="qr.png",
                mime="image/png"
            )