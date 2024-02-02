import streamlit as st
from PIL import Image

st.subheader("Image to Greyscale Converter")

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    camera_input = st.camera_input("Take a picture")

if camera_input:
    # Create a pillow Image instance
    img = Image.open(camera_input)

    # Convert the image to greyscale
    img = img.convert("L")

    # Render new image
    st.image(img)

elif uploaded_image:
    # Create a pillow Image instance
    img = Image.open(uploaded_image)

    # Convert the image to greyscale
    img = img.convert("L")

    # Render new image
    st.image(img)