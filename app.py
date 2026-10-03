import streamlit as st
from PIL import Image
from transformers import pipeline
import time

st.set_page_config(page_title="Iris Flower Detector", layout="centered")

st.markdown("""
<style>
.stApp { background: #f5f3ff!important; }
header, #MainMenu, footer {visibility: hidden;}
.block-container {
    background: white!important; border-radius: 25px!important;
    padding: 1rem!important; box-shadow: 0 8px 30px rgba(0,0,0,0.1)!important;
    max-width: 380px; margin: auto;
}
.center-box { display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding-top: 20px; }
.logo { width: 65px; height: 65px; background: #5b2cc4; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 32px; color: #ff9d00; margin-bottom: 15px; }
h2 { color: #2e1a6e!important; margin: 5px 0!important; }
.sub { color: #8a8a8a; font-size: 13px; margin-bottom: 20px; }
.stButton>button { background: #5b2cc4!important; color: white!important; border-radius: 10px!important; width: 100%!important; height: 45px!important; font-weight: 700!important; border: none!important; }
.card { background: #f8f7ff; border-radius: 14px; padding: 12px; margin: 8px 0; border: 1px solid #ede9fe; }
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'login'
    st.session_state.user = 'Sanvi'
    st.session_state.history = []
    st.session_state.result = None

def go(p): st.session_state.page = p; st.rerun()

@st.cache_resource
def load_model():
    return pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
classifier = load_model()

# 1. LOGIN - CENTER MADHE
if st.session_state.page == 'login':
    st.markdown("""
    <div class="center-box">
        <div class="logo">⚜️</div>
        <h2>Iris Flower Detector</h2>
        <p class="sub">Identify flowers using your camera or gallery</p>
    </div>
    """, unsafe_allow_html=True)
    st.text_input("Email", value="sanvi@gmail.com")
    st.text_input("Password", type="password", value="123456")
    if st.button("Login"):
        go('home')
    st.markdown('<p style="text-align:center; font-size:12px;">OR</p>', unsafe_allow_html=True)
    if st.button("Continue with Google"):
        go('home')

# 2. HOME
elif st.session_state.page == 'home':
    st.markdown(f"<h3>Hello, {st.session_state.user}! 👋</h3><p style='color:gray; font-size:13px;'>Discover the beauty of flowers around you.</p>", unsafe_allow_html=True)
    st.markdown('<div style="background:#a78bfa; height:140px; border-radius:16px; padding:15px; color:white;"><div style="background:#5b2cc4; border-radius:12px; padding:10px; margin-top:60px;">📷 Scan Flower<br><small>Identify an Iris flower</small></div></div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🕒 History"): go('history')
    with c2:
        if st.button("🖼️ Gallery"): go('camera')
    if st.button("📸 SCAN NOW"): go('camera')
    if st.button("👤 Profile"): go('profile')
    if st.button("⚙️ Settings"): go('settings')

# 3. CAMERA
elif st.session_state.page == 'camera':
    st.markdown("<b>← Scan Iris Flower</b>", unsafe_allow_html=True)
    st.markdown('<div style="border:2px dashed #a78bfa; border-radius:18px; height:300px; background:#111; color:white; display:flex; align-items:center; justify-content:center; text-align:center;">Place the iris flower within the frame<br>Make sure flower is clear</div>', unsafe_allow_html=True)
    file = st.file_uploader("Choose photo", type=["jpg","png","jpeg"])
    cam = st.camera_input("Take photo")
    final = cam if cam else file
    if final:
        img = Image.open(final)
        st.session_state.temp_img = img
        st.session_state.page = 'processing'
        st.rerun()
    if st.button("Back"): go('home')

# 4. PROCESSING
elif st.session_state.page == 'processing':
    st.markdown("<div style='text-align:center; padding-top:50px;'><h3>Analyzing the flower...</h3><p style='color:gray; font-size:12px;'>Please wait while we identify the iris species.</p><h1>⚜️</h1></div>", unsafe_allow_html=True)
    if 'temp_img' in st.session_state:
        res = classifier(st.session_state.temp_img, candidate_labels=["iris flower","rose flower","lily flower"])[0]
        st.session_state.result = {"img": st.session_state.temp_img, "score": res['score'], "label": res['label']}
        st.session_state.history.append({"name": "Iris germanica", "score": f"{int(res['score']*100)}%"})
        time.sleep(1)
        go('result')

# 5. RESULT
elif st.session_state.page == 'result':
    r = st.session_state.result
    st.markdown("<b>← Result</b>", unsafe_allow_html=True)
    if r:
        st.image(r['img'], use_container_width=True)
        st.markdown(f"<span style='background:#dcfce7; color:#166534; padding:4px 8px; border-radius:10px; font-size:11px;'>{int(r['score']*100)}% Match</span><h3>Iris germanica</h3><small>German Iris</small>", unsafe_allow_html=True)
        st.markdown('<div class="card"><b>Key Features</b><br><small>🎨 Purple with yellow markings<br>🌸 Spring - Early Summer<br>📏 60-90 cm<br>🌍 Gardens, meadows</small></div>', unsafe_allow_html=True)
        if st.button("View More Details"): go('details')
        if st.button("Scan Another"): go('camera')
    if st.button("Home"): go('home')

# 6. DETAILS
elif st.session_state.page == 'details':
    st.markdown("<b>← Flower Details</b>", unsafe_allow_html=True)
    if st.session_state.result: st.image(st.session_state.result['img'], use_container_width=True)
    st.markdown("<h3>Iris germanica</h3><small>German Iris - 98% Match</small>", unsafe_allow_html=True)
    st.markdown('<div class="card"><b>Description</b><br><small>Iris germanica, commonly known as the German iris, is a perennial flowering plant known for its striking purple blooms. It is widely grown in gardens and is native to Europe.</small><br><br><b>Quick Facts</b><br><small>🔬 Scientific: Iris germanica<br>🏷️ Family: Iridaceae<br>⏰ Bloom: Spring</small></div>', unsafe_allow_html=True)
    if st.button("Back"): go('result')

# 7. HISTORY
elif st.session_state.page == 'history':
    st.markdown("<b>← Scan History</b>", unsafe_allow_html=True)
    for h in st.session_state.history:
        st.markdown(f'<div class="card">🌸 {h["name"]} - {h["score"]} ›</div>', unsafe_allow_html=True)
    if not st.session_state.history:
        st.markdown('<div class="card">🌸 Iris germanica - 98% - 22 Sep 2026 ›</div><div class="card">🌸 Iris versicolor - 95% - 21 Sep 2026 ›</div>')
    if st.button("Home"): go('home')

# 8. PROFILE
elif st.session_state.page == 'profile':
    st.markdown("<b>← Profile</b>", unsafe_allow_html=True)
    st.markdown('<div style="text-align:center"><div style="width:65px; height:65px; background:#ede9fe; border-radius:50%; margin:0 auto; display:flex; align-items:center; justify-content:center; font-size:30px;">👤</div><h3>Sanvi Mandavkar</h3><small>sanvi@gmail.com</small></div>', unsafe_allow_html=True)
    st.markdown('<div class="card">Member Since: 12 Mar 2026<br>Total Scans: 32<br>Favorite: Iris germanica</div>', unsafe_allow_html=True)
    if st.button("Home"): go('home')

# 9. SETTINGS
else:
    st.markdown("<b>← Settings</b>", unsafe_allow_html=True)
    st.markdown('<div class="card">👤 Edit Profile ›<br><br>🔒 Change Password ›<br><br>🔔 Notifications ›</div><div class="card" style="color:red; text-align:center;">Log Out</div>', unsafe_allow_html=True)
    if st.button("Home"): go('home')
    if st.button("Logout"): go('login')
