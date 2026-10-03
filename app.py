import streamlit as st
from PIL import Image
import time
from transformers import pipeline

st.set_page_config(page_title="Iris Flower Detector", layout="centered")

st.markdown("""
<style>
.stApp{background:#e9e6ff !important;}
header, #MainMenu, footer, .stDeployButton {visibility:hidden !important;}
.block-container{
 background:white !important;
 border-radius:28px !important;
 padding:0 !important;
 max-width:390px !important;
 min-height:840px !important;
 box-shadow:0 10px 30px rgba(0,0,0,0.2) !important;
 overflow:hidden !important;
 border:2px solid #000 !important;
}
.stButton>button{
 background:#4f33d1 !important;
 color:white !important;
 border-radius:12px !important;
 width:100% !important;
 height:46px !important;
 font-weight:700 !important;
 border:none !important;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "splash"
    st.session_state.img = None
    st.session_state.score = 98

def go(p):
    st.session_state.page = p
    st.rerun()

IRIS = "https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=800&q=90"
IRIS2 = "https://images.unsplash.com/photo-1518895949257-7621c3c786d7?w=800&q=85"

# 1 SPLASH
if st.session_state.page == "splash":
    st.markdown(f"""
    <div style='height:840px; background: linear-gradient(to bottom, rgba(255,255,255,0.75) 0%, rgba(255,255,255,0.2) 50%, rgba(0,0,0,0.1) 100%), url({IRIS}); background-size:cover; background-position:center; text-align:center; padding-top:40px;'>
        <div style='display:flex; justify-content:space-between; padding:0 22px; font-size:13px; font-weight:600;'> <span>9:41</span> <span>●</span> <span>📶 🔋</span> </div>
        <div style='width:68px; height:68px; background:#5f32d3; border-radius:14px; margin:50px auto 0 auto; display:flex; align-items:center; justify-content:center; font-size:34px; color:white;'>🌸</div>
        <div style='font-size:20px; font-weight:800; color:#2d2163; margin-top:15px;'>Iris Flower Detector</div>
        <div style='font-size:11px; color:#555;'>Identify Flowers. Explore Nature.</div>
        <div style='position:absolute; bottom:35px; left:0; right:0; text-align:center; font-size:10px; color:#555;'>Loading...</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Get Started →"):
        go("login")

# 2 LOGIN
elif st.session_state.page == "login":
    st.markdown("""
    <div style='padding:22px; text-align:center;'>
        <div style='width:60px; height:60px; background:#5f32d3; border-radius:14px; margin:auto; display:flex; align-items:center; justify-content:center; color:white; font-size:30px;'>🌸</div>
        <div style='font-size:16px; font-weight:800; color:#1e1142; margin-top:10px;'>Iris Flower Detector</div>
        <div style='font-size:10px; color:gray;'>Identify flowers using your camera or gallery</div>
        <div style='display:flex; gap:8px; margin-top:15px;'><div style='flex:1; background:#4f33d1; color:white; padding:8px; border-radius:8px; font-size:12px;'>Login</div><div style='flex:1; background:#f5f3ff; padding:8px; border-radius:8px; font-size:12px;'>Sign Up</div></div>
    </div>
    """, unsafe_allow_html=True)
    st.text_input("", placeholder="Email or Phone Number")
    st.text_input("", placeholder="Password", type="password")
    if st.button("Login"):
        go("home")
    st.markdown("<div style='text-align:center; font-size:11px; color:gray;'>OR<br>Continue with Google<br><br>Don't have an account? <b style='color:#4f33d1;'>Sign Up</b></div>", unsafe_allow_html=True)

# 3 HOME
elif st.session_state.page == "home":
    st.markdown(f"""
    <div style='padding:16px;'>
        <div style='display:flex; justify-content:space-between;'> <span>☰</span> <span>🔔</span> </div>
        <div style='margin-top:10px;'><b>Hello, Sanvi! 👋</b><br><small style='color:gray;'>Discover the beauty of flowers around you.</small></div>
        <div style='height:160px; border-radius:16px; background:url({IRIS}); background-size:cover; margin:12px 0; position:relative;'>
            <div style='position:absolute; bottom:10px; left:10px; right:10px; background:#4f33d1; border-radius:10px; padding:10px; color:white; font-size:12px; display:flex; justify-content:space-between;'><span>📷 Scan Flower<br><small style='font-size:9px;'>Identify an iris flower</small></span><span>›</span></div>
        </div>
        <div style='display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:11px; text-align:center;'>
            <div style='background:#f7f5ff; padding:14px; border-radius:12px;'>🕒<br>History</div>
            <div style='background:#f7f5ff; padding:14px; border-radius:12px;'>🖼️<br>Gallery</div>
            <div style='background:#f7f5ff; padding:14px; border-radius:12px;'>📚<br>Learn</div>
            <div style='background:#f7f5ff; padding:14px; border-radius:12px;'>⚙️<br>Settings</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("📷 SCAN NOW"): go("camera")
    c1,c2,c3,c4 = st.columns(4)
    with c1:
        if st.button("🏠"): go("home")
    with c2:
        if st.button("🕒"): go("history")
    with c3:
        if st.button("👤"): go("profile")
    with c4:
        if st.button("⚙️"): go("settings")

# 4 CAMERA
elif st.session_state.page == "camera":
    st.markdown(f"<div style='padding:12px; font-weight:700; display:flex; justify-content:space-between;'><span>✕</span><span>Scan Iris Flower</span><span>⚡</span></div><div style='height:420px; background:url({IRIS}); background-size:cover; display:flex; align-items:center; justify-content:center;'><div style='width:200px; height:280px; border:2px solid white; border-radius:18px;'></div></div><div style='padding:10px; text-align:center; font-size:10px; background:black; color:white;'>Place the iris flower within the frame</div>", unsafe_allow_html=True)
    f = st.file_uploader("Upload", type=["jpg","png","jpeg"])
    cam = st.camera_input("Take Photo")
    final = cam if cam else f
    if final:
        st.session_state.img = Image.open(final).convert("RGB")
        go("result")
    if st.button("← Home"): go("home")

# 6 RESULT
else:
    if st.session_state.img is not None:
        st.image(st.session_state.img, use_container_width=True)
    else:
        st.image(IRIS, use_container_width=True)
    st.markdown(f"""
    <div style='padding:16px;'>
        <div style='display:flex; justify-content:space-between;'><div><b>Iris germanica</b><br><small style='color:gray;'>German Iris</small></div><span style='background:#d1fae5; padding:4px 8px; border-radius:12px; font-size:10px;'>{st.session_state.score}% Match</span></div>
        <div style='background:#f8f7ff; border-radius:12px; padding:10px; margin-top:10px; font-size:11px;'>
        🎨 Color: Purple with yellow<br>🌼 Bloom: Spring<br>📏 Height: 60-90 cm<br>🌍 Habitat: Gardens
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("View More Details"): go("home")
    if st.button("Scan Another"): go("camera")
