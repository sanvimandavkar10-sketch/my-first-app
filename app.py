import streamlit as st
from PIL import Image
from transformers import pipeline

st.set_page_config(page_title="Maza Glass App", layout="centered")

# --- GLASS BACKGROUND - DEMO SAME TO SAME ---
st.markdown("""
<style>
.stApp {
    background: #c7d2fe;
    background-image:
        radial-gradient(at 20% 30%, #a5b4fc 0px, transparent 50%),
        radial-gradient(at 80% 20%, #818cf8 0px, transparent 50%),
        radial-gradient(at 40% 80%, #c084fc 0px, transparent 50%),
        linear-gradient(135deg, #ddd6fe 0%, #a5b4fc 100%);
    background-attachment: fixed;
}
header, #MainMenu, footer {visibility: hidden;}
.glass-card {
    background: rgba(255, 255, 255, 0.72)!important;
    backdrop-filter: blur(25px) saturate(180%)!important;
    border-radius: 28px!important;
    border: 1.5px solid rgba(255, 255, 255, 0.6)!important;
    box-shadow: 0 8px 32px rgba(31, 38, 135, 0.15)!important;
    padding: 30px!important;
    text-align: center;
}
.glass-card h1 { color: #4c1d95!important; font-weight: 800!important; }
.stButton > button {
    background: linear-gradient(90deg, #8b8cf8, #6d28d9)!important;
    color: white!important; border-radius: 12px!important; width: 100%!important;
}
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'signin'
    st.session_state.user_name = ''
    st.session_state.last_result = ''

def next_page(p):
    st.session_state.page = p
    st.rerun()

@st.cache_resource
def load_model():
    return pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
classifier = load_model()

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

if st.session_state.page == 'signin':
    st.title("Maza Pahila App")
    name = st.text_input("Tujha naav:")
    if st.button("Submit / Sign In"):
        if name:
            st.session_state.user_name = name
            next_page('welcome')

elif st.session_state.page == 'welcome':
    st.title(f"Welcome {st.session_state.user_name}! 👋")
    if st.button("Next -> Upload Photo"): next_page('upload')

elif st.session_state.page == 'upload':
    st.title("Photo Taka 📸")
    file = st.file_uploader("Photo", type=["jpg","png","jpeg"])
    cam = st.camera_input("Camera")
    final_file = cam if cam else file
    if final_file:
        img = Image.open(final_file)
        st.image(img, use_container_width=True)
        with st.spinner("AI baghtoy..."):
            res = classifier(img, candidate_labels=["iris flower","adenium flower","rose flower","other flower","flower pot"])[0]
            st.session_state.last_result = res['label']
            if "iris" in res['label']: st.success(f"Ho! He IRIS aahe! ✅ {res['score']*100:.1f}%")
            else: st.warning(f"He {res['label']} aahe!")
        if st.button("Final Result Bagh"): next_page('final')

elif st.session_state.page == 'final':
    st.title("Final Result ✨")
    st.info(st.session_state.last_result)
    if st.button("Rating De"): next_page('rating')

else:
    st.title("Rating De ⭐")
    stars = st.slider("Stars",1,5,5)
    if st.button("Submit"):
        st.balloons()
        st.success(f"Thanks {st.session_state.user_name}! {stars} stars!")

st.markdown('</div>', unsafe_allow_html=True)
