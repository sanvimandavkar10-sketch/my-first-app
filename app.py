import streamlit as st
from PIL import Image
from transformers import pipeline
import random

st.set_page_config(page_title="Flower Identifier", layout="centered")

# --- PROPER PURPLE GLASS THEME LIKE YOUR PHOTOS ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #6a0f3c 0%, #a81e5c 50%, #d63384 100%)!important;
    background-attachment: fixed!important;
}
header, #MainMenu, footer {visibility: hidden;}
.block-container {
    background: rgba(255,255,255,0.95)!important;
    backdrop-filter: blur(20px)!important;
    border-radius: 25px!important;
    padding: 1.5rem!important;
    margin-top: 1rem!important;
    box-shadow: 0 15px 35px rgba(0,0,0,0.2)!important;
    min-height: 85vh;
}
h1, h2, h3 { color: #2d0a1e!important; font-weight: 800!important; }
.sub-text { color: #6c757d!important; text-align: center; font-size: 14px;}
.badge {
    background: #f8d7e6; color: #a81e5c; padding: 4px 12px; border-radius: 20px;
    font-size: 11px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase;
    display: inline-block; margin: 0 auto;
}
.purple-card {
    background: linear-gradient(135deg, #a81e5c 0%, #d63384 100%);
    border-radius: 18px; padding: 18px; color: white; margin: 15px 0;
}
.white-card {
    background: white; border-radius: 16px; padding: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.06); border: 1px solid #f1e5ea; margin: 12px 0;
}
.conf-bar { background: #ffe6f0; height: 8px; border-radius: 10px; }
.conf-fill { background: #a81e5c; height: 8px; border-radius: 10px; }
.google-btn {
    background: white; border: 1px solid #ddd; border-radius: 10px;
    padding: 12px; display: flex; align-items: center; justify-content: center; gap: 10px;
    font-weight: 600; cursor: pointer;
}
.nav-bar {
    position: fixed; bottom: 20px; left: 5%; right: 5%;
    background: white; border-radius: 20px; padding: 10px;
    display: flex; justify-content: space-around; box-shadow: 0 5px 20px rgba(0,0,0,0.15);
}
.stButton > button {
    background: #a81e5c!important; color: white!important; border-radius: 12px!important;
    width: 100%!important; height: 50px!important; font-weight: 700!important; border: none!important;
}
[data-testid="stFileUploader"] { background: white!important; border-radius: 12px!important; }
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'signin'
    st.session_state.user = 'User'
    st.session_state.result = None
    st.session_state.collection = []

FLOWER_DB = {
    "iris flower": {"common": "Iris", "sci": "Iris germanica", "about": "A tall perennial with sword-like leaves and showy purple blooms. Symbol of wisdom.", "water": "Moderate watering weekly", "light": "Full sun to partial shade"},
    "adenium flower": {"common": "Adenium", "sci": "Adenium obesum", "about": "Desert rose with thick stem and vibrant pink flowers. Drought tolerant.", "water": "Low water, drought tolerant", "light": "Full sun"},
    "rose flower": {"common": "Garden Rose", "sci": "Rosa rubiginosa", "about": "Classic fragrant flower with layered petals. Most loved flower worldwide.", "water": "Regular watering", "light": "Full sun 6+ hours"},
    "garden cosmos": {"common": "Garden Cosmos", "sci": "Cosmos bipinnatus", "about": "A tall Mexican annual with feathery foliage and simple saucer flowers in white, pink and crimson. Exceptionally easy from seed.", "water": "Drought tolerant once established", "light": "Full sun"},
}

def go(p): st.session_state.page = p; st.rerun()

@st.cache_resource
def load_model():
    return pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
classifier = load_model()

# 1. SIGN IN
if st.session_state.page == 'signin':
    st.markdown('<div style="text-align:center"><span class="badge">AI FLOWER IDENTIFIER</span><h1>Identify Any Flower<br>in Seconds</h1><p class="sub-text">Snap a photo and let the AI do the rest</p></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""<div style="background:white; border-radius:15px; padding:20px; text-align:center;"><img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" width="22"><br><b>Flower Identifier</b><p style="font-size:13px;color:gray">Your Pocket Flower Guide</p></div>""", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    name = st.text_input("Name")
    email = st.text_input("Email")
    if st.button("Continue with Google"):
        if name:
            st.session_state.user = name
            go('home')
        else: st.warning("Enter Name")

# 2. HOME - LIKE YOUR 4th PHOTO
elif st.session_state.page == 'home':
    st.markdown('<h3 style="text-align:center">Flower Identifier</h3>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="purple-card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <div><small>Your Collection</small><h2 style="margin:0;color:white">{len(st.session_state.collection)} Flowers</h2><small>{len(st.session_state.collection)} Saved • {random.randint(1,3)} This Week</small></div>
            <div style="background:rgba(255,255,255,0.2); width:70px; height:70px; border-radius:50%; display:flex; align-items:center; justify-content:center; flex-direction:column;"><b>33%</b><small style="font-size:9px">confident</small></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="display:flex; justify-content:space-around; text-align:center; margin:10px 0;">
        <div><b>3</b><br><small>Total Scans</small></div><div><b>3</b><br><small>Saved</small></div><div><b>3</b><br><small>Species</small></div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("📸 Identify a Flower - Snap a photo and let the model do the rest >"):
        go('upload')
    st.markdown('<div class="white-card">📁 Choose from gallery →</div>', unsafe_allow_html=True)

    st.write("**Recent Identifications**")
    if st.session_state.collection:
        for item in st.session_state.collection[-2:]:
            st.markdown(f'<div class="white-card">🌸 {item["common"]} - {item["conf"]}% • 1 hr ago →</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="white-card">🌸 Garden Cosmos - 97% • 1 hr ago →</div>', unsafe_allow_html=True)

    cols = st.columns(4)
    if cols[0].button("🏠"): go('home')
    if cols[1].button("🗂️"): go('collection')
    if cols[2].button("📸"): go('upload')
    if cols[3].button("⚙️"): st.info("Settings")

# 3. UPLOAD
elif st.session_state.page == 'upload':
    st.markdown('<h3>
