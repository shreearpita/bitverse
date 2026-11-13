
from io import BytesIO
from pathlib import Path

import streamlit as st
from PIL import Image

from src.core.density_renderer import generate_density_artwork


# configuration
st.set_page_config(
    page_title="BITVERSE",
    page_icon="◈",
    layout="centered"
)

MAX_IMAGE_SIZE = (200, 200)


# interface
st.title("BITVERSE")
st.caption("Transform images into binary artwork.")

uploaded_file = st.file_uploader(
    "Upload your image",
    type=["png", "jpg", "jpeg", "webp"]
)


# image upload
if uploaded_file is not None:

    original_image = Image.open(uploaded_file).convert("RGB")

    st.subheader("Original image")
    st.image(original_image, width="stretch")

    # generate artwork
    if st.button("Generate artwork", type="primary"):

        with st.spinner("Generating your binary artwork..."):

            # work on a copy; preserve original image
            image = original_image.copy()
            image.thumbnail(MAX_IMAGE_SIZE)

            # generate
            artwork = generate_density_artwork(
                image,
                output_name="bitverse_output"
            )

            # prepare PNG
            png_buffer = BytesIO()
            artwork.save(png_buffer, format="PNG")

            # prepare TXT
            txt_path = Path("output/bitverse_output.txt")
            txt_data = txt_path.read_bytes()

        # display result
        st.success("Your artwork is ready!")

        st.subheader("Generated artwork")
        st.image(artwork, width="stretch")

        # downloads
        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                "Download PNG",
                data=png_buffer.getvalue(),
                file_name="bitverse_artwork.png",
                mime="image/png"
            )

        with col2:
            st.download_button(
                "Download TXT",
                data=txt_data,
                file_name="bitverse_artwork.txt",
                mime="text/plain"
            )
