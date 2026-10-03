import streamlit as st

st.set_page_config(
    page_title="Iris Flower Classification",
    page_icon="🌸",
    layout="centered"
)

st.title("🌸 Iris Flower Classification")
st.write("Welcome to Iris Flower Classification App")

st.subheader("Upload or Take a Photo")

photo = st.file_uploader(
    "📷 Select photo",
    type=["jpg", "jpeg", "png"]
)

if photo is not None:
    st.success("Photo selected successfully! ✅")
    st.image(photo, caption="Selected Photo", use_container_width=True)
