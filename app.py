import streamlit as st
from PIL import Image
from transformers import pipeline
import time
from datetime import datetime

st.set_page_config(page_title="Iris Flower Detector", layout="centered")

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #ede9fe 0%, #f5f3ff 50%, #ede9fe 100%)!important; }
header, #MainMenu, footer {visibility: hidden;}
.block-container {
    background: white!important; border-radius: 28px!important;
    padding: 1.2rem!important; margin-top: 0.5rem!important;
    box-shadow: 0 10px 40px rgba(90, 60, 200, 0.15)!important;
    min-height: 90vh; max-width: 400px;
}
h1, h2, h3 { color: #2e1a6e!important; font-weight: 800!important; }
.sub { color: #6b7280!important; font-size: 13px; text-align: center; }
.purple-btn {
    background: linear-gradient(90deg, #6d28d9 0%, #8b5cf6 100%)!important;
    color: white!important; border-radius: 12px!important; width: 100%!important;
    height: 48px!important; font-weight: 700!important; border: none!important;
}
.white-btn { background: white!important; color: #6d28d9!important; border: 1.5px solid #6d28d9!important; border-radius: 12px!important; width: 100%!important; height: 48px!important; font-weight: 600!important;}
.card { background: #f8f7ff; border-radius: 16px; padding: 14px; margin: 10px 0; border: 1px solid #ede9fe; }
.purple-card { background: linear-gradient(135deg, #6d28d9 0%, #8b5cf6 100%); color: white; border-radius: 18px; padding: 18px; }
.badge-green { background: #dcfce7; color: #166534; padding: 3px 8px; border-radius: 12px; font-size: 10px; font-weight: 700;}
.tab-active { background: #6d28d9; color: white; padding: 6px 14px; border-radius: 20px; font-size: 12px; }
.tab { background: #f3f0ff; color: #6b7280; padding: 6px 14px; border-radius: 20px; font-size: 12px;}
.bottom-nav { display: flex; justify-content: space-around; background: white; border-radius: 18px; padding: 10px; box-shadow: 0 -2px 15px rgba(0,0,0,0.06); margin-top: 20px;}
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'splash'
    st.session_state.user = 'Sanvi'
    st.session_state.email = 'sanvi@gmail.com'
    st.session_state.history = [
        {"name": "Iris germanica", "time": "22 Sep 2026, 10:24 AM", "score": "98%"},
        {"name": "Iris versicolor", "time": "21 Sep 2026, 05:18 PM", "score": "95%"},
        {"name": "Iris pseudacorus", "time": "20 Sep 2026, 02:37 PM", "score": "93%"},
    ]
    st.session_state.result_data = None

def go(p): st.session_state.page = p; st.rerun()

@st.cache_resource
def load_model():
    return pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
classifier = load_model()

IRIS_INFO = {
    "name": "Iris germanica", "common": "German Iris", "match": "98% Match",
    "color": "Purple with yellow markings", "bloom": "Spring - Early Summer", "height": "60-90 cm", "habitat": "Gardens, meadows, wetlands",
    "desc": "Iris germanica, commonly known as the German iris, is a perennial flowering plant known for its striking purple, blue, and yellow blooms. It is widely grown in gardens and is native to Europe.",
    "sci": "Iris germanica", "family": "Iridaceae"
}

# 1. SPLASH
if st.session_state.page == 'splash':
    st.markdown('<div style="text-align:center; padding-top:40px;"><div style="width:80px;height:80px;background:#6d28d9;border-radius:18px;margin:0 auto;display:flex;align-items:center;justify-content:center;font-size:40px">⚜️</div><h1 style="margin-top:20px">Iris Flower Detector</h1><p class="sub">Identify Flowers. Explore Nature.</p></div>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1592150621744-aca64f48394a?w=500", use_container_width=True)
    st.markdown('<p style="text-align:center; font-size:12px; color:gray;">Loading...</p>', unsafe_allow_html=True)
    time.sleep(1)
    if st.button("Get Started →", key="splash_btn"): go('login')

# 2. LOGIN
elif st.session_state.page == 'login':
    st.markdown('<div style="text-align:center"><div style="width:60px;height:60px;background:#6d28d9;border-radius:14px;margin:0 auto;display:flex;align-items:center;justify-content:center;color:white;font-size:30px">⚜️</div><h2>Iris Flower Detector</h2><p class="sub">Identify flowers using your camera or gallery</p></div>', unsafe_allow_html=True)
    tab1, tab2 = st.columns(2)
    with tab1: st.markdown('<div style="background:#6d28d9;color:white;padding:8px;border-radius:8px;text-align:center;font-size:13px">Login</div>', unsafe_allow_html=True)
    with tab2: st.markdown('<div style="background:#f3f0ff;padding:8px;border-radius:8px;text-align:center;font-size:13px">Sign Up</div>', unsafe_allow_html=True)
    email = st.text
