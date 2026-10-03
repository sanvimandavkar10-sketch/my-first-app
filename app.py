import streamlit as st
from PIL import Image
from transformers import pipeline

st.set_page_config(page_title="Flower Classifier", layout="centered")

# --- PROPER GLASS UI - LIKE OTHER APPS ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%)!important;
    background-attachment: fixed!important;
}
header, #MainMenu, footer {visibility: hidden;}
.block-container {
    background: rgba(255, 255, 255, 0.85)!important;
    backdrop-filter: blur(20px)!important;
    border-radius: 20px!important;
    padding: 2.5rem!important;
    margin-top: 2rem!important;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1)!important;
    border: 1px solid rgba(255,255,255,0.5)!important;
}
h1, h2, h3 { color: #2d3748!important; text-align: center!important; }
p, label { color: #4a5568!important; }
input {
    background: white!important;
    color: black!important;
}
.stButton > button {
    background: #6c5ce7!important;
    color: white!important;
    border-radius: 10px!important;
    width: 100%!important;
    height: 45px!important;
    font-weight: 600!important;
    border: none!important;
}
.stButton > button:hover { background: #5a4bd1!important; }
[data-testid="stFileUploader"] {
    background: white!important;
    border-radius: 10px!important;
}
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'signin'
    st.session_state.user = ''
    st.session_state.result = ''

def go(p):
    st.session_state.page = p
    st.rerun()

@st.cache_resource
def load_model():
    return pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
classifier = load_model()

# PAGE 1
if st.session_state.page == 'signin':
    st.title("Flower AI App")
    st.write("Welcome to Smart Flower Detection")
    name = st.text_input("Enter Your Name")
    if st.button("Sign In"):
        if name:
            st.session_state.user = name
            go('welcome')
        else:
            st.warning("Please enter name")

# PAGE 2
elif st.session_state.page == 'welcome':
    st.title(f"Welcome, {st.session_state.user}! 👋")
    st.write("This app detects flower type using AI.")
    st.write("Click Next to continue.")
    if st.button("Next - Upload Photo"): go('upload')

# PAGE 3
elif st.session_state.page == 'upload':
    st.title("Upload Photo 📸")
    st.write("Upload a flower image")
    file = st.file_uploader("Choose Image", type=["jpg","png","jpeg"])
    camera = st.camera_input("Or Take Photo")
    final = camera if camera else file

    if final:
        img = Image.open(final)
        st.image(img, caption="Your Photo", use_container_width=True)
        with st.spinner("Analyzing with AI..."):
            res = classifier(img, candidate_labels=["iris flower","adenium flower","rose flower","sunflower","tulip"])[0]
            st.session_state.result = res
            if "iris" in res['label'].lower():
                st.success(f"Detected: IRIS FLOWER ✅ Confidence: {res['score']*100:.1f}%")
            else:
                st.info(f"Detected: {res['label'].upper()} - {res['score']*100:.1f}%")
        if st.button("View Final Result"): go('final')

# PAGE 4
elif st.session_state.page == 'final':
    st.title("Final Result")
    r = st.session_state.result
    if r:
        st.metric("Flower Type", r['label'])
        st.metric("Confidence", f"{r['score']*100:.1f}%")
    if st.button("Give Rating"): go('rating')
    if st.button("Upload Another"): go('upload')

# PAGE 5
else:
    st.title("Rate Us ⭐")
    st.write("How was your experience?")
    stars = st.slider("Rating", 1, 5, 5)
    feedback = st.text_area("Feedback (Optional)")
    if st.button("Submit Feedback"):
        st.balloons()
        st.success(f"Thank you {st.session_state.user}! You rated {stars} stars.")
        if st.button("Go to Home"): go('signin')
