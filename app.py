import streamlit as st
from PIL import Image
from transformers import pipeline
import time

st.set_page_config(page_title="Iris Flower Detector", layout="centered")
st.markdown("""
<style>
.stApp{background:#e9e6ff!important;}
header,#MainMenu,footer{visibility:hidden;}
.block-container{background:white!important; border-radius:32px!important; padding:0!important; max-width:390px!important; min-height:850px; box-shadow:0 15px 45px rgba(0,0,0,0.18)!important; overflow:hidden; border:1.5px solid #e9e4ff;}
.stButton>button{background:#4f33d1!important; color:white!important; border-radius:12px!important; width:100%!important; height:48px!important; font-weight:700!important; border:none!important; margin:5px 0!important; font-size:13px!important;}
.outline>button{background:white!important; color:#4f33d1!important; border:1.5px solid #e9e4ff!important;}
.small>button{background:#f7f5ff!important; color:#2d2163!important; border:1px solid #ede8ff!important; height:78px!important; border-radius:16px!important;}
.badge{background:#dcfce7; color:#15803d; font-size:10px; font-weight:800; padding:4px 10px; border-radius:20px; border:1px solid #bbf7d0;}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="splash"
    st.session_state.img=None
    st.session_state.score=98

def go(p):
    st.session_state.page=p
    st.rerun()

@st.cache_resource
def load_model():
    return pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
model = load_model()

IRIS="https://images.unsplash.com/photo-1518895949257-7621c3c786d7?w=800&q=85"
IRIS2="https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=800&q=80"

# 1. SPLASH - Photo 1
if st.session_state.page=="splash":
    st.markdown(f'<div style="height:850px; background:linear-gradient(to bottom, rgba(0,0,0,0.0), rgba(0,0,0,0.4)), url({IRIS}); background-size:cover; background-position:center; text-align:center; padding-top:90px; position:relative;"><div style="width:64px; height:64px; background:white; border-radius:18px; margin:0 auto; display:flex; align-items:center; justify-content:center; font-size:32px; box-shadow:0 4px 12px rgba(0,0,0,0.15);">🌸</div><div style="color:#1e1142; background:white; display:inline-block; margin-top:18px; padding:6px 16px; border-radius:10px; font-weight:800; font-size:16px;">Iris Flower Detector</div><div style="color:white; font-size:11px; margin-top:8px; text-shadow:0 1px 4px black;">Identify Flowers. Explore Nature.</div><div style="position:absolute; bottom:30px; left:0; right:0; color:white; font-size:10px; opacity:0.9;">Loading...</div></div>', unsafe_allow_html=True)
    if st.button("Get Started →"): go("login")

# 2. LOGIN - Photo 2
elif st.session_state.page=="login":
    st.markdown('<div style="padding:22px 18px 0 18px; text-align:center;"><div style="width:60px; height:60px; background:#4f33d1; border-radius:16px; margin:0 auto; display:flex; align-items:center; justify-content:center; font-size:28px; color:white;">🌸</div><div style="font-weight:800; font-size:16px; color:#1e1142; margin-top:10px;">Iris Flower Detector</div><div style="font-size:10px; color:#8a84a6; margin-top:2px;">Identify flowers using your camera or gallery</div><div style="display:flex; gap:8px; margin:16px 0;"><div style="flex:1; background:#4f33d1; color:white; padding:10px; border-radius:10px; font-weight:700; font-size:12px;">Login</div><div style="flex:1; background:#f5f3ff; color:#6b6a80; padding:10px; border-radius:10px; font-size:12px;">Sign Up</div></div></div>', unsafe_allow_html=True)
    st.markdown('<div style="padding:0 18px;">', unsafe_allow_html=True)
    st.text_input("", placeholder="📧 Email or Phone Number")
    st.text_input("", placeholder="🔒 Password", type="password")
    if st.button("Login"): go("home")
    st.markdown('<div style="text-align:center; font-size:11px; color:#4f33d1; margin:4px;">Forgot Password?</div><div style="text-align:center; font-size:11px; color:#aaa; margin:6px;">OR</div><div style="border:1px solid #eee; border-radius:10px; padding:11px; text-align:center; font-size:12px; background:white;">G Continue with Google</div><div style="text-align:center; font-size:11px; margin-top:12px;">Don\'t have an account? <b style="color:#4f33d1;">Sign Up</b></div></div>', unsafe_allow_html=True)

# 3. HOME - Photo 3
elif st.session_state.page=="home":
    st.markdown(f'<div style="padding:16px 18px 0 18px;"><div style="display:flex; justify-content:space-between; font-size:18px;"><span>☰</span><span>🔔</span></div><div style="margin-top:14px;"><b style="font-size:15px; color:#1e1142;">Hello, Sanvi! 👋</b><br><span style="font-size:11px; color:#8a84a6;">Discover the beauty of flowers around you.</span></div><div style="height:170px; border-radius:18px; margin:14px 0; background:url({IRIS}); background-size:cover; position:relative; border:1px solid #eee;"><div style="position:absolute; bottom:12px; left:12px; right:12px; background:#4f33d1; border-radius:12px; padding:12px; color:white; display:flex; justify-content:space-between; align-items:center;"><div><div style="font-size:12px; font-weight:700;">📷 Scan Flower</div><div style="font-size:10px; opacity:0.9;">Identify an iris flower</div></div><div style="font-size:20px;">›</div></div></div></div>', unsafe_allow_html=True)
    st.markdown('<div style="padding:0 18px; display:grid; grid-template-columns:1fr 1fr; gap:10px;">', unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        if st.button("🕒\nHistory", key="hh1"): go("history")
    with c2:
        if st.button("🖼️\nGallery", key="hh2"): go("gallery")
    c3,c4=st.columns(2)
    with c3:
        if st.button("📚\nLearn", key="hh3"): go("learn")
    with c4:
        if st.button("⚙️\nSettings", key="hh4"): go("settings")
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("📷 SCAN NOW"): go("camera")
    st.markdown('<div style="display:flex; justify-content:space-around; border-top:1px solid #f1edff; padding:10px 0; margin-top:10px; font-size:10px; text-align:center;"><div style="color:#4f33d1; font-weight:700;">🏠<br>Home</div><div style="color:#aaa;">🕒<br>History</div><div style="color:#aaa;">👤<br>Profile</div><div style="color:#aaa;">⚙️<br>Settings</div></div>', unsafe_allow_html=True)
    # hidden nav for working
    b1,b2,b3,b4=st.columns(4)
    with b1:
        if st.button(" ", key="nav1"): go("home")
    with b2:
        if st.button(" ", key="nav2"): go("history")
    with b3:
        if st.button(" ", key="nav3"): go("profile")
    with b4:
        if st.button(" ", key="nav4"): go("settings")

# 4. CAMERA - Photo 4
elif st.session_state.page=="camera":
    st.markdown(f'<div style="height:600px; background:url({IRIS}); background-size:cover; background-position:center; position:relative; padding:14px;"><div style="display:flex; justify-content:space-between; color:white; font-weight:600; font-size:13px;"><span>✕</span><span>Scan Iris Flower</span><span>⚡</span></div><div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:220px; height:300px; border:2px solid rgba(255,255,255,0.8); border-radius:20px;"><div style="position:absolute; top:-2px; left:-2px; width:30px; height:30px; border-top:3px solid white; border-left:3px solid white; border-radius:8px 0 0 0;"></div><div style="position:absolute; bottom:-2px; right:-2px; width:30px; height:30px; border-bottom:3px solid white; border-right:3px solid white; border-radius:0 0 8px 0;"></div></div><div style="position:absolute; bottom:70px; left:0; right:0; text-align:center; color:white; font-size:10px; background:rgba(0,0,0,0.4); padding:8px;">Place the iris flower within the frame<br>Make sure the flower is clear and well lit</div><div style="position:absolute; bottom:15px; left:0; right:0; display:flex; justify-content:space-around; align-items:center;"><div style="width:48px; height:48px; background:rgba(255,255,255,0.2); border-radius:12px; display:flex; align-items:center; justify-content:center; color:white;">🖼️</div><div style="width:60px; height:60px; border:3px solid white; border-radius:50%; background:rgba(255,255,255,0.9);"></div><div style="width:20px;"></div></div></div>', unsafe_allow_html=True)
    f=st.file_uploader("Upload", type=["jpg","png","jpeg"], label_visibility="collapsed")
    cam=st.camera_input(" ", label_visibility="collapsed")
    final=cam if cam else f
    if final:
        st.session_state.img=Image.open(final).convert("RGB")
        go("processing")
    if st.button("← Back to Home"): go("home")

# 5. PROCESSING - Photo 5
elif st.session_state.page=="processing":
    st.markdown('<div style="height:750px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:20px;"><div style="color:#4f33d1; font-weight:800; font-size:14px;">Analyzing the flower...</div><div style="color:#8a84a6; font-size:11px; margin-top:6px;">Please wait while we identify<br>the iris species.</div><div style="margin:40px; width:130px; height:130px; border-radius:50%; border:3px solid #ede9ff; border-top-color:#4f33d1; display:flex; align-items:center; justify-content:center;"><div style="width:90px; height:90px; background:#f5f3ff; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:32px;">🌸</div></div><div style="width:180px; height:6px; background:#f0ebff; border-radius:10px;"><div style="width:70%; height:6px; background:#4f33d1; border-radius:10px;"></div></div><div style="color:#8a84a6; font-size:10px; margin-top:10px;">Identifying flower...</div></div>', unsafe_allow_html=True)
    if st.session_state.img is not None:
        try:
            r=model(st.session_state.img, candidate_labels=["iris flower","rose","lily"])[0]
            st.session_state.score=int(r["score"]*100)
        except: st.session_state.score=98
        time.sleep(1.8)
        go("result")

# 6. RESULT - Photo 6
elif st.session_state.page=="result":
    if st.session_state.img: st.image(st.session_state.img, use_container_width=True)
    else: st.image(IRIS, use_container_width=True)
    st.markdown(f'<div style="padding:16px 18px;"><div style="display:flex; justify-content:space-between; align-items:flex-start;"><div><b style="font-size:14px; color:#1e1142;">Iris germanica</b><br><small style="color:#8a84a6; font-size:11px;">German Iris</small></div><span class="badge">{st.session_state.score}% Match</span></div><div style="margin-top:14px;"><b style="font-size:11px;">Key Features</b><div style="background:#f8f7ff; border-radius:12px; padding:12px; margin-top:8px; font-size:11px; color:#5a5575; line-height:2;">🔵 Color &nbsp;&nbsp;&nbsp; Purple with yellow markings<br>🕒 Bloom Time &nbsp;&nbsp;&nbsp; Spring - Early Summer<br>📏 Height &nbsp;&nbsp;&nbsp;&nbsp; 60 - 90 cm<br>📍 Habitat &nbsp;&nbsp;&nbsp;&nbsp; Gardens, meadows, wetlands</div></div></div>', unsafe_allow_html=True)
    if st.button("View More Details"): go("details")
    if st.button("Scan Another", key="scan2"): go("camera")

# 7. DETAILS - Photo 7
elif st.session_state.page=="details":
    if st.session_state.img: st.image(st.session_state.img, use_container_width=True)
    else: st.image(IRIS, use_container_width=True)
    st.markdown(f'<div style="padding:16px 18px;"><div style="display:flex; justify-content:space-between;"><div><b style="font-size:14px;">Iris germanica</b><br><small style="color:#8a84a6;">German Iris</small></div><span class="badge">{st.session_state.score}% Match</span></div><div style="display:flex; gap:6px; margin:14px 0;"><span style="background:#4f33d1; color:white; padding:7px 14px; border-radius:20px; font-size:11px;">About</span><span style="background:#f5f3ff; color:#666; padding:7px 14px; border-radius:20px; font-size:11px;">Care</span><span style="background:#f5f3ff; color:#666; padding:7px 14px; border-radius:20px; font-size:11px;">More Photos</span></div><div style="background:#f8f7ff; border-radius:14px; padding:12px; font-size:11px; color:#5a5575;"><b>Description</b><br>Iris germanica, commonly known as the German Iris, is a perennial flowering plant known for its striking purple, blue, and yellow blooms. It is widely grown in gardens and is native to Europe.<br><br><b>Quick Facts</b><br>🔬 Scientific Name: Iris germanica<br>🏷️ Family: Iridaceae<br>⏰ Bloom Time: Spring - Early Summer</div></div>', unsafe_allow_html=True)
    if st.button("← Back to Result"): go("result")

# 8. HISTORY - Photo 8
elif st.session_state.page=="history":
    st.markdown('<div style="padding:16px 18px;"><div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;"><span>←</span><b>Scan History</b></div></div>', unsafe_allow_html=True)
    for name, date, per, color in [("Iris germanica","22 Sep 2026, 10:24 AM","98%","#ede9fe"),("Iris versicolor","21 Sep 2026, 05:18 PM","95%","#fef3c7"),("Iris pseudacorus","20 Sep 2026, 02:37 PM","93%","#fef9c3"),("Iris sibirica","18 Sep 2026, 11:02 AM","90%","#dcfce7"),("Iris germanica","16 Sep 2026, 09:45 AM","97%","#ede9fe")]:
        st.markdown(f'<div style="display:flex; gap:12px; padding:12px 18px; border-bottom:1px solid #f5f3ff; align-items:center;"><div style="width:48px; height:48px; background:{color}; border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:20px;">🌸</div><div><b style="font-size:12px;">{name}</b><br><small style="font-size:10px; color:#999;">{date}</small><br><span style="background:#dcfce7; color:#15803d; font-size:9px; padding:2px 6px; border-radius:10px;">{per}</span></div><div style="margin-left:auto; color:#ccc;">›</div></div>', unsafe_allow_html=True)
    if st.button("Home"): go("home")

# 9. PROFILE - Photo 9
elif st.session_state.page=="profile":
    st.markdown('<div style="padding:18px;"><div style="display:flex; justify-content:space-between; align-items:center;"><span>←</span><b>Profile</b><span>⚙️</span></div><div style="text-align:center; margin-top:18px;"><div style="width:64px; height:64px; background:#ede9fe; border-radius:50%; margin:0 auto; display:flex; align-items:center; justify-content:center; font-size:28px;">👤</div><b style="font-size:13px; display:block; margin-top:10px;">Sanvi Mandavkar</b><small style="color:#8a84a6;">sanvi@gmail.com</small></div><div style="background:#f8f7ff; border-radius:12px; padding:12px; margin-top:16px; font-size:11px;"><div style="display:flex; justify-content:space-between; padding:6px 0;"><span>👤 Member Since</span><b>12 Mar 2026</b></div><div style="display:flex; justify-content:space-between; padding:6px 0;"><span>🔍 Total Scans</span><b>32</b></div><div style="display:flex; justify-content:space-between; padding:6px 0;"><span>⭐ Favorite Flower</span><b>Iris germanica</b></div></div><div style="background:#f8f7ff; border-radius:12px; padding:12px; margin-top:12px; font-size:11px;"><div style="padding:8px 0; border-bottom:1px solid #eee;">🌿 My Plants <span style="float:right;">›</span></div><div style="padding:8px 0; border-bottom:1px solid #eee;">🔖 Saved Flowers <span style="float:right;">›</span></div><div style="padding:8px 0;">❓ Help & Support <span style="float:right;">›</span></div></div></div>', unsafe_allow_html=True)
    if st.button("Home"): go("home")

# 10. SETTINGS - Photo 10
else:
    st.markdown('<div style="padding:18px;"><div style="display:flex; align-items:center; gap:10px;"><span>←</span><b>Settings</b></div><div style="margin-top:18px;"><b style="font-size:11px;">Account</b><div style="background:#f8f7ff; border-radius:12px; padding:12px; margin-top:6px; font-size:11px;"><div style="padding:8px 0;">👤 Edit Profile <span style="float:right;">›</span></div><div style="padding:8px 0;">🔒 Change Password <span style="float:right;">›</span></div></div></div><div style="margin-top:14px;"><b style="font-size:11px;">App Preferences</b><div style="background:#f8f7ff; border-radius:12px; padding:12px; margin-top:6px; font-size:11px;"><div style="padding:8px 0; display:flex; justify-content:space-between;">🔔 Notifications <span style="color:#4f33d1;">●</span></div><div style="padding:8px 0; display:flex; justify-content:space-between;">📷 Camera Quality <span>High ›</span></div><div style="padding:8px 0; display:flex; justify-content:space-between;">🌐 Language <span>English ›</span></div></div></div><div style="margin-top:14px;"><b style="font-size:11px;">About</b><div style="background:#f8f7ff; border-radius:12px; padding:12px; margin-top:6px; font-size:11px;"><div style="padding:8px 0;">ℹ️ About App <span style="float:right;">›</span></div><div style="padding:8px 0;">🔐 Privacy Policy <span style="float:right;">›</span></div></div></div><div style="margin-top:18px; text-align:center; color:#ef4444; background:#fff1f2; padding:12px; border-radius:12px; font-size:11px;">↪ Log Out</div></div>', unsafe_allow_html=True)
    if st.button("Home"): go("home")
    if st.button("Log Out"): go("splash")
