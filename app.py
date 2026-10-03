import streamlit as st
from PIL import Image
from transformers import pipeline
import time
import random

st.set_page_config(page_title="Iris Flower Detector", layout="centered")

st.markdown("""
<style>
.stApp { background: #e9e6ff!important; }
header, #MainMenu, footer { visibility: hidden; }
.block-container {
    background: white!important; border-radius: 28px!important;
    padding: 0px!important; max-width: 390px!important;
    box-shadow: 0 12px 40px rgba(80,40,180,0.18)!important;
    overflow: hidden;
}
.inner { padding: 18px; }
.logo-box { width: 62px; height: 62px; background: #4f33d1; border-radius: 16px; display:flex; align-items:center; justify-content:center; font-size:32px; margin: 0 auto; color:white; }
.pill { display:inline-block; background:#e8e0ff; color:#4f33d1; font-size:11px; font-weight:700; padding:4px 10px; border-radius:20px; }
.title { color:#1e1142!important; font-weight:800!important; font-size:22px!important; text-align:center; margin:8px 0 2px 0; }
.sub { color:#8a84a6; font-size:12px; text-align:center; margin-bottom:12px; }
.input { background:#f5f3ff; border:1.5px solid #e9e5ff; border-radius:12px; padding:12px; width:100%; font-size:13px; margin-bottom:10px; }
.btn-purple { background:#4f33d1; color:white; border:none; border-radius:12px; width:100%; height:46px; font-weight:700; }
.btn-white { background:white; color:#4f33d1; border:1.5px solid #4f33d1; border-radius:12px; width:100%; height:46px; font-weight:600; }
.hero-img { height:175px; border-radius:18px; background-size:cover; background-position:center; position:relative; margin:12px 0; }
.hero-btn { position:absolute; bottom:12px; left:12px; right:12px; background:rgba(79,51,209,0.92); backdrop-filter:blur(8px); border-radius:14px; padding:12px; color:white; display:flex; justify-content:space-between; align-items:center; }
.grid2 { display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:12px 0; }
.gcard { background:#f7f5ff; border:1px solid #ede8ff; border-radius:14px; padding:16px 8px; text-align:center; font-size:12px; font-weight:600; color:#2d2163; }
.badge { background:#d1fae5; color:#065f46; font-size:10px; font-weight:700; padding:3px 8px; border-radius:20px; }
.key-row { display:flex; justify-content:space-between; font-size:11px; margin:6px 0; color:#5a5575; }
.bottom { display:flex; justify-content:space-around; background:white; border-top:1px solid #f0ebff; padding:10px 0; position:sticky; bottom:0; }
.bottom div { font-size:10px; text-align:center; color:#8a84a6; }
.bottom.active { color:#4f33d1; font-weight:700; }
.stButton>button { background:#4f33d1!important; color:white!important; border-radius:12px!important; width:100%!important; height:46px!important; font-weight:700!important; border:none!important; }
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'splash'
    st.session_state.user = 'Sanvi'
    st.session_state.email = 'sanvi@gmail.com'
    st.session_state.history = [
        {"name":"Iris germanica","time":"22 Sep 2026, 10:24 AM","per":"98%"},
        {"name":"Iris versicolor","time":"21 Sep 2026, 05:18 PM","per":"95%"},
        {"name":"Iris pseudacorus","time":"20 Sep 2026, 02:37 PM","per":"93%"},
        {"name":"Iris sibirica","time":"18 Sep 2026, 11:02 AM","per":"90%"},
        {"name":"Iris germanica","time":"16 Sep 2026, 09:45 AM","per":"97%"},
    ]
    st.session_state.result_img = None
    st.session_state.result_score = 98

def go(p): st.session_state.page = p; st.rerun()

@st.cache_resource
def load_model():
    return pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
model = load_model()

IRIS_IMG = "https://images.unsplash.com/photo-1518895949257-7621c3c786d7?w=600"

# 1. SPLASH SCREEN
if st.session_state.page == 'splash':
    st.markdown(f"""
    <div class="inner" style="text-align:center; padding-top:25px;">
        <div class="logo-box">⚜️</div>
        <div class="title">Iris Flower Detector</div>
        <div class="sub">Identify Flowers. Explore Nature.</div>
        <div style="margin:18px -18px 0 -18px; height:420px; background: url('{IRIS_IMG}'); background-size:cover; background-position:center; display:flex; align-items:flex-end; justify-content:center;">
            <div style="color:white; font-size:11px; padding-bottom:12px; opacity:0.9;">Loading...</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Get Started →"): go('login')

# 2. LOGIN / SIGN UP
elif st.session_state.page == 'login':
    st.markdown("""
    <div class="inner" style="text-align:center;">
        <div class="logo-box">⚜️</div>
        <div class="title">Iris Flower Detector</div>
        <div class="sub">Identify flowers using your camera or gallery</div>
        <div style="display:flex; gap:8px; margin:14px 0;">
            <div style="flex:1; background:#4f33d1; color:white; padding:8px; border-radius:10px; font-size:12px; font-weight:700;">Login</div>
            <div style="flex:1; background:#f5f3ff; color:#5a5575; padding:8px; border-radius:10px; font-size:12px;">Sign Up</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="inner">', unsafe_allow_html=True)
        email = st.text_input("", placeholder="📧 Email or Phone Number", label_visibility="collapsed")
        pwd = st.text_input("", placeholder="🔒 Password", type="password", label_visibility="collapsed")
        if st.button("Login"): go('home')
        st.markdown('<div style="text-align:center; font-size:11px; color:#4f33d1; margin:6px 0;">Forgot Password?</div><div style="text-align:center; font-size:11px; color:gray; margin:6px 0;">OR</div>', unsafe_allow_html=True)
        if st.button("G Continue with Google"): go('home')
        st.markdown('<div style="text-align:center; font-size:11px; margin-top:10px;">Don\'t have an account? <b style="color:#4f33d1;">Sign Up</b></div></div>', unsafe_allow_html=True)

# 3. HOME / DASHBOARD
elif st.session_state.page == 'home':
    st.markdown(f"""
    <div class="inner">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <div>☰</div><div>🔔</div>
        </div>
        <div style="margin-top:8px;"><b style="font-size:16px; color:#1e1142;">Hello, {st.session_state.user}! 👋</b><br><small style="color:#8a84a6; font-size:11px;">Discover the beauty of flowers around you.</small></div>
        <div class="hero-img" style="background-image: url('{IRIS_IMG}');">
            <div class="hero-btn"><div><b style="font-size:13px;">📷 Scan Flower</b><br><small style="font-size:10px; opacity:0.9;">Identify an Iris flower</small></div><div>›</div></div>
        </div>
        <div class="grid2">
            <div class="gcard">🕒<br>History</div><div class="gcard">🖼️<br>Gallery</div>
            <div class="gcard">📚<br>Learn</div><div class="gcard">⚙️<br>Settings</div>
        </div>
    </div>
    <div class="bottom"><div class="active">🏠<br>Home</div><div>🕒<br>History</div><div>👤<br>Profile</div><div>⚙️<br>Settings</div></div>
    """, unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1:
        if st.button("History"): go('history')
        if st.button("Profile"): go('profile')
    with c2:
        if st.button("Scan Now"): go('camera')
        if st.button("Settings"): go('settings')

# 4. CAMERA / SCAN SCREEN
elif st.session_state.page == 'camera':
    st.markdown(f"""
    <div class="inner">
        <div style="display:flex; justify-content:space-between; font-size:13px; font-weight:600;"><span>✕</span><span>Scan Iris Flower</span><span>⚡</span></div>
    </div>
    <div style="height:520px; background: url('{IRIS_IMG}'); background-size:cover; background-position:center; position:relative; display:flex; align-items:center; justify-content:center;">
        <div style="width:240px; height:320px; border:2px solid rgba(255,255,255,0.8); border-radius:20px; position:relative;">
            <div style="position:absolute; top:-2px; left:-2px; width:30px; height:30px; border-top:3px solid white; border-left:3px solid white; border-radius:10px 0 0 0;"></div>
            <div style="position:absolute; top:-2px; right:-2px; width:30px; height:30px; border-top:3px solid white; border-right:3px solid white; border-radius:0 10px 0 0;"></div>
            <div style="position:absolute; bottom:-2px; left:-2px; width:30px; height:30px; border-bottom:3px solid white; border-left:3px solid white; border-radius:0 0 0 10px;"></div>
            <div style="position:absolute; bottom:-2px; right:-2px; width:30px; height:30px; border-bottom:3px solid white; border-right:3px solid white; border-radius:0 0 10px 0;"></div>
        </div>
        <div style="position:absolute; bottom:65px; left:0; right:0; text-align:center; color:white; font-size:11px; background:rgba(0,0,0,0.4); padding:10px;">Place the iris flower within the frame<br>Make sure the flower is clear and well lit</div>
        <div style="position:absolute; bottom:12px; left:0; right:0; display:flex; justify-content:space-between; padding:0 20px; align-items:center;">
            <div style="width:48px; height:48px; background:rgba(255,255,255,0.2); border-radius:12px; display:flex; align-items:center; justify-content:center;">🖼️</div>
            <div style="width:60px; height:60px; border:3px solid white; border-radius:50%; background:rgba(255,255,255,0.9);"></div>
            <div style="width:20px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    file = st.file_uploader("Upload or Camera", type=["jpg","png","jpeg"])
    cam = st.camera_input("Take")
    final = cam if cam else file
    if final:
        st.session_state.result_img = Image.open(final)
        st.session_state.page = 'processing'; st.rerun()
    if st.button("Back"): go('home')

# 5. PROCESSING SCREEN
elif st.session_state.page == 'processing':
    st.markdown("""
    <div class="inner" style="text-align:center; padding-top:110px;">
        <b style="color:#1e1142;">Analyzing the flower...</b><br>
        <small style="color:#8a84a6; font-size:11px;">Please wait while we identify the iris species.</small>
        <div style="margin:40px auto; width:140px; height:140px; border:2px solid #e9e5ff; border-top:2px solid #4f33d1; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:40px;">⚜️</div>
    </div>
    """, unsafe_allow_html=True)
    if st.session_state.result_img is not None:
        res = model(st.session_state.result_img, candidate_labels=["iris flower","rose","lily"])[0]
        st.session_state.result_score = int(res['score']*100)
        time.sleep(1.2)
        go('result')

# 6. RESULT SCREEN
elif st.session_state.page == 'result':
    img = st.session_state.result_img
    score = st.session_state.result_score
    if img is not None: st.image(img, use_container_width=True)
    else: st.image(IRIS_IMG, use_container_width=True)
    st.markdown(f"""
    <div class="inner">
        <div style="display:flex; justify-content:space-between; align-items:center;"><b style="font-size:14px;">Iris germanica</b><span class="badge">{score}% Match</span></div>
        <small style="color:#8a84a6;">German Iris</small>
        <div style="margin-top:12px;"><b style="font-size:12px;">Key Features</b>
            <div class="key-row"><span>🎨 Color</span><span>Purple with yellow markings</span></div>
            <div class="key-row"><span>🌼 Bloom Time</span><span>Spring - Early Summer</span></div>
            <div class="key-row"><span>📏 Height</span><span>60 - 90 cm</span></div>
            <div class="key-row"><span>🌍 Habitat</span><span>Gardens, meadows, wetlands</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("View More Details"): go('details')
    if st.button("Scan Another", key="scan2"): go('camera')
    if st.button("← Home"): go('home')

# 7. FLOWER DETAILS SCREEN
elif st.session_state.page == 'details':
    if st.session_state.result_img is not None: st.image(st.session_state.result_img, use_container_width=True)
    st.markdown("""
    <div class="inner">
        <b>Iris germanica</b><br><small style="color:gray;">German Iris</small> <span class="badge">98% Match</span>
        <div style="display:flex; gap:8px; margin:12px 0;">
            <span style="background:#4f33d1; color:white; padding:5px 12px; border-radius:20px; font-size:11px;">About</span>
            <span style="background:#f5f3ff; color:gray; padding:5px 12px; border-radius:20px; font-size:11px;">Care</span>
            <span style="background:#f5f3ff; color:gray; padding:5px 12px; border-radius:20px; font-size:11px;">More Photos</span>
        </div>
        <b style="font-size:12px;">Description</b><br><small style="font-size:11px; color:#5a5575;">Iris germanica, commonly known as the German Iris, is a perennial flowering plant known for its striking purple, blue, and yellow blooms. It is widely grown in gardens and is native to Europe.</small>
        <div style="margin-top:12px;"><b style="font-size:12px;">Quick Facts</b>
            <div class="key-row"><span>🔬 Scientific Name</span><span>Iris germanica</span></div>
            <div class="key-row"><span>🏷️ Family</span><span>Iridaceae</span></div>
            <div class="key-row"><span>⏰ Bloom Time</span><span>Spring - Early Summer</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("← Back to Result"): go('result')

# 8. SCAN HISTORY SCREEN
elif st.session_state.page == 'history':
    st.markdown('<div class="inner"><b>← Scan History</b></div>', unsafe_allow_html=True)
    for item in st.session_state.history:
        color = "#c4b5fd" if "germanica" in item["name"] else "#fde68a" if "pseudo" in item["name"] else "#a7f3d0"
        st.markdown(f"""
        <div style="display:flex; gap:10px; padding:10px 18px; border-bottom:1px solid #f5f3ff; align-items:center;">
            <div style="width:48px; height:48px; background:{color}; border-radius:10px; display:flex; align-items:center; justify-content:center;">🌸</div>
            <div><b style="font-size:12px;">{item["name"]}</b><br><small style="font-size:10px; color:gray;">{item["time"]}<br>{item["per"]}</small></div>
            <div style="margin-left:auto;">›</div>
        </div>
        """, unsafe_allow_html=True)
    if st.button("Home"): go('home')

# 9. USER PROFILE SCREEN
elif st.session_state.page == 'profile':
    st.markdown("""
    <div class="inner" style="text-align:center;">
        <div style="display:flex; justify-content:space-between;"><span>←</span><b>Profile</b><span>⚙️</span></div>
        <div style="width:64px; height:64px; background:#ede9fe; border-radius:50%; margin:18px auto 8px auto; display:flex; align-items:center; justify-content:center; font-size:28px;">👤</div>
        <b style="font-size:14px;">Sanvi Mandavkar</b><br><small style="color:gray;">sanvi@gmail.com</small>
        <div style="text-align:left; margin-top:18px;">
            <div class="key-row"><span>👤 Member Since</span><b>12 Mar 2026</b></div>
            <div class="key-row"><span>🔍 Total Scans</span><b>32</b></div>
            <div class="key-row"><span>⭐ Favorite Flower</span><b>🌸 Iris germanica</b></div>
            <div style="margin-top:16px; background:#f8f7ff; border-radius:12px; padding:12px;">
                <div style="padding:8px 0; border-bottom:1px solid #ede8ff; font-size:12px;">🌿 My Plants <span style="float:right;">›</span></div>
                <div style="padding:8px 0; border-bottom:1px solid #ede8ff; font-size:12px;">🔖 Saved Flowers <span style="float:right;">›</span></div>
                <div style="padding:8px 0; font-size:12px;">❓ Help & Support <span style="float:right;">›</span></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Home"): go('home')
    if st.button("Settings"): go('settings')

# 10. SETTINGS SCREEN
else:
    st.markdown("""
    <div class="inner">
        <div style="display:flex; gap:10px; align-items:center;"><span>←</span><b>Settings</b></div>
        <div style="margin-top:14px;"><small style="font-weight:700;">Account</small>
            <div style="background:#f8f7ff; border-radius:12px; padding:12px; margin-top:6px;">
                <div style="display:flex; justify-content:space-between; font-size:12px; padding:8px 0;">👤 Edit Profile <span>›</span></div>
                <div style="display:flex; justify-content:space-between; font-size:12px; padding:8px 0;">🔒 Change Password <span>›</span></div>
            </div>
        </div>
        <div style="margin-top:14px;"><small style="font-weight:700;">App Preferences</small>
            <div style="background:#f8f7ff; border-radius:12px; padding:12px; margin-top:6px;">
                <div style="display:flex; justify-content:space-between; font-size:12px; padding:8px 0;">🔔 Notifications <span style="color:#4f33d1;">●</span></div>
                <div style="display:flex; justify-content:space-between; font-size:12px; padding:8px 0;">📷 Camera Quality <span>High ›</span></div>
                <div style="display:flex; justify-content:space-between; font-size:12px; padding:8px 0;">🌐 Language <span>English ›</span></div>
            </div>
        </div>
        <div style="margin-top:14px;"><small style="font-weight:700;">About</small>
            <div style="background:#f8f7ff; border-radius:12px; padding:12px; margin-top:6px;">
                <div style="display:flex; justify-content:space-between; font-size:12px; padding:8px 0;">ℹ️ About App <span>›</span></div>
                <div style="display:flex; justify-content:space-between; font-size:12px; padding:8px 0;">🔐 Privacy Policy <span>›</span></div>
            </div>
        </div>
        <div style="text-align:center; margin-top:18px; color:#e11d48; font-size:13px; background:#fff1f2; padding:10px; border-radius:12px;">↪ Log Out</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Home"): go('home')
    if st.button("Logout"): go('splash')
