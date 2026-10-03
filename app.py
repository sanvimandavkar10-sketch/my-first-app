import streamlit as st
from PIL import Image
from transformers import pipeline

st.set_page_config(page_title="Maza Photo App", layout="centered")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
.glass-box {
    background: rgba(255, 255, 255, 0.25);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 30px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
}
h1, p, label { color: white!important; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return pipeline("image-classification", model="google/vit-base-patch16-224")
classifier = load_model()

st.markdown('<div class="glass-box">', unsafe_allow_html=True)
st.title("Maza Glass Photo App ✨")
st.write("Photo upload kar - mi sangto to Iris aahe ka!")

file = st.file_uploader("Ithe photo tak", type=["jpg","png","jpeg"])
if file:
    image = Image.open(file)
    st.image(image, use_container_width=True)
    with st.spinner("Baghtoy..."):
        res = classifier(image)[0]
        if "iris" in res['label'].lower():
            st.success(f"Ho! He IRIS aahe! ✅ {res['score']*100:.1f}%")
        else:
            st.warning(f"He Iris nahi, he {res['label']} aahe!")
st.markdown('</div>', unsafe_allow_html=True)
