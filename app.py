import streamlit as st
from PIL import Image
from transformers import pipeline
import time

st.set_page_config(page_title="Iris Flower Detector", layout="centered")
st.markdown("""
<style>
.stApp{background:#e9e6ff!important;}
header,#MainMenu,footer{visibility:hidden;}
.block-container{background:white!important; border-radius:28px!important; padding:0!important; max-width:390px!important; min-height:800px; box-shadow:0 12px 40px rgba(80,40,180,0.2)!important; overflow:hidden;}
.stButton>button{background:#4f33d1!important; color:white!important; border-radius:12px!important; width:100%!important; height:44px!important; font-weight:700!important; border:none!important; margin:4px 0!important;}
.small-btn>button{background:#f7f5ff!important; color:#2d2163!important; border:1px solid #ede8ff!important; border-radius:14px!important; height:70px!important;}
.badge{background:#d1fae5; color:#065f46; font-size:10px; padding:4px 8px; border-radius:20px; font-weight:700;}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="splash"
    st.session_state.img=None
    st.session_state.score=98
    st.session_state.history=[{"name":"Iris germanica","time":"22 Sep 2026, 10:24 AM","per":"98%"},{"name":"Iris versicolor","time":"21 Sep 2026, 05:18 PM","per":"95%"},{"name":"Iris pseudacorus","time":"20 Sep 2026, 02:37 PM","per":"93%"}]

def go(p):
    st.session_state.page=p
    st.rerun()

@st.cache_resource
def load_model():
    return pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
model = load_model()
IRIS="https://images.unsplash.com/photo-1518895949257-7621c3c786d7?w=800"

# 1 SPLASH
if st.session_state.page=="splash":
    st.markdown(f'<div style="height:750px; background:linear-gradient(to bottom, rgba(0,0,0,0.05), rgba(0,0,0,0.3)), url({IRIS}); background-size:cover; background-position:center; text-align:center; padding-top:80px;"><div style="width:64px; height:64px; background:#6c4dff; border-radius:16px; margin:0 auto; display:flex; align-items:center; justify-content:center; font-size:32px; color:white;">🌸</div><div style="color:white; font-size:22px; font-weight:800; margin-top:10px;">Iris Flower Detector</div><div style="color:white; font-size:12px;">Identify Flowers. Explore Nature.</div></div>', unsafe_allow_html=True)
    if st.button("Get Started →"): go("login")

# 2 LOGIN
elif st.session_state.page=="login":
    st.markdown('<div style="padding:20px; text-align:center;"><div style="width:64px; height:64px; background:#6c4dff; border-radius:16px; margin:0 auto; display:flex; align-items:center; justify-content:center; font-size:32px; color:white;">🌸</div><b style="font-size:18px; color:#1e1142;">Iris Flower Detector</b><br><small style="color:#8a84a6;">Identify flowers using your camera or gallery</small></div>', unsafe_allow_html=True)
    st.text_input("", placeholder="Email or Phone Number")
    st.text_input("", placeholder="Password", type="password")
    if st.button("Login"): go("home")
    if st.button("Continue with Google"): go("home")

# 3 HOME - SAGLE CLICKABLE
elif st.session_state.page=="home":
    st.markdown(f'<div style="padding:18px;"><div style="display:flex; justify-content:space-between;">☰ 🔔</div><b>Hello, Sanvi! 👋</b><br><small style="color:#8a84a6;">Discover the beauty of flowers around you.</small><div style="height:165px; border-radius:18px; margin:12px 0; background:url({IRIS}); background-size:cover; position:relative;"><div style="position:absolute; bottom:10px; left:10px; right:10px; background:#4f33d1; border-radius:12px; padding:10px; color:white; display:flex; justify-content:space-between;"><b>📷 Scan Flower</b><span>›</span></div></div></div>', unsafe_allow_html=True)
    st.markdown('<div style="padding:0 18px;">', unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        if st.button("🕒 History", key="h1"): go("history")
        if st.button("📚 Learn", key="h2"): go("learn")
    with c2:
        if st.button("🖼️ Gallery", key="h3"): go("gallery")
        if st.button("⚙️ Settings", key="h4"): go("settings")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="padding:10px 18px;">', unsafe_allow_html=True)
    if st.button("📷 SCAN NOW - Click to Open Camera", key="scan"): go("camera")
    st.markdown('</div>', unsafe_allow_html=True)
    # Bottom Nav Clickable
    b1,b2,b3,b4=st.columns(4)
    with b1:
        if st.button("🏠 Home", key="b1"): go("home")
    with b2:
        if st.button("🕒 History", key="b2"): go("history")
    with b3:
        if st.button("👤 Profile", key="b3"): go("profile")
    with b4:
        if st.button("⚙️ Settings", key="b4"): go("settings")

# 4 CAMERA
elif st.session_state.page=="camera":
    st.markdown('<div style="padding:12px; font-weight:700;">✕ Scan Iris Flower ⚡</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="height:400px; background:url({IRIS}); background-size:cover; display:flex; justify-content:center; align-items:center;"><div style="width:220px; height:300px; border:2px solid white; border-radius:20px;"></div></div>', unsafe_allow_html=True)
    f=st.file_uploader("Upload from Gallery", type=["jpg","png","jpeg"])
    cam=st.camera_input("Take Photo")
    final=cam if cam else f
    if final:
        st.session_state.img=Image.open(final).convert("RGB")
        go("processing")
    if st.button("← Back to Home"): go("home")

# 5 PROCESSING
elif st.session_state.page=="processing":
    st.markdown('<div style="height:600px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><b>Analyzing the flower...</b><small style="color:gray;">Please wait</small><div style="margin:30px; width:100px; height:100px; border:3px solid #eee; border-top:3px solid #4f33d1; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:30px;">🌸</div></div>', unsafe_allow_html=True)
    if st.session_state.img is not None:
        try:
            r=model(st.session_state.img, candidate_labels=["iris flower","rose","lily"])[0]
            st.session_state.score=int(r["score"]*100)
        except: st.session_state.score=98
        time.sleep(1.5)
        go("result")

# 6 RESULT - CLICKABLE
elif st.session_state.page=="result":
    if st.session_state.img: st.image(st.session_state.img, use_container_width=True)
    st.markdown(f'<div style="padding:18px;"><b>Iris germanica</b> <span class="badge">{st.session_state.score}% Match</span><br><small style="color:gray;">German Iris</small><div style="background:#f8f7ff; border-radius:12px; padding:12px; margin-top:10px; font-size:11px;">🎨 Purple with yellow<br>🌼 Spring - Early Summer<br>📏 60-90 cm</div></div>', unsafe_allow_html=True)
    if st.button("View More Details"): go("details")
    if st.button("Scan Another"): go("camera")
    if st.button("← Home"): go("home")

# 7 DETAILS
elif st.session_state.page=="details":
    if st.session_state.img: st.image(st.session_state.img, use_container_width=True)
    st.markdown('<div style="padding:18px;"><b>Iris germanica</b> <span class="badge">98% Match</span><p style="font-size:11px; color:#555;">German Iris is a perennial with beautiful purple blooms.</p></div>', unsafe_allow_html=True)
    if st.button("About"): st.info("Iris germanica is also called German Iris. Family: Iridaceae. Type: Perennial.")
    if st.button("Care"): st.info("Needs full sun, well-drained soil, water weekly.")
    if st.button("More Photos"): go("gallery")
    if st.button("← Back to Result"): go("result")

# 8 HISTORY - CLICKABLE
elif st.session_state.page=="history":
    st.markdown('<div style="padding:18px;"><b>← Scan History</b></div>', unsafe_allow_html=True)
    for i, item in enumerate(st.session_state.history):
        if st.button(f'🌸 {item["name"]} - {item["per"]} - {item["time"]}', key=f"hist{i}"):
            go("result")
    if st.button("← Home"): go("home")

# 9 PROFILE
elif st.session_state.page=="profile":
    st.markdown('<div style="padding:18px; text-align:center;"><b>Profile</b><div style="width:70px; height:70px; background:#ede9fe; border-radius:50%; margin:15px auto; display:flex; align-items:center; justify-content:center; font-size:30px;">👤</div><b>Sanvi Mandavkar</b><br><small>sanvi@gmail.com</small><div style="background:#f8f7ff; border-radius:12px; padding:12px; margin-top:10px; font-size:11px; text-align:left;">Member Since: 12 Mar 2026<br>Total Scans: 32<br>Favorite: Iris germanica</div></div>', unsafe_allow_html=True)
    if st.button("My Plants"): go("gallery")
    if st.button("Saved Flowers"): go("gallery")
    if st.button("Settings"): go("settings")
    if st.button("← Home"): go("home")

# GALLERY
elif st.session_state.page=="gallery":
    st.markdown('<div style="padding:18px;"><b>← Gallery</b><br><small style="color:gray;">Your saved flower photos</small></div>', unsafe_allow_html=True)
    st.image(IRIS, caption="Iris germanica")
    st.image("https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=400", caption="Iris versicolor")
    if st.button("← Home"): go("home")

# LEARN
elif st.session_state.page=="learn":
    st.markdown('<div style="padding:18px;"><b>← Learn</b><br><br><div style="background:#f8f7ff; border-radius:12px; padding:12px; font-size:11px;"><b>What is Iris?</b><br>Iris is a genus of 260–300 species of flowering plants with showy flowers.</div><br><div style="background:#f8f7ff; border-radius:12px; padding:12px; font-size:11px;"><b>Types of Iris</b><br>• Germanica<br>• Versicolor<br>• Sibirica<br>• Pseudacorus</div></div>', unsafe_allow_html=True)
    if st.button("← Home"): go("home")

# 10 SETTINGS - CLICKABLE
else:
    st.markdown('<div style="padding:18px;"><b>← Settings</b><div style="margin-top:10px; background:#f8f7ff; border-radius:12px; padding:12px; font-size:12px;">Account<br>App Preferences<br>About</div></div>', unsafe_allow_html=True)
    if st.button("Edit Profile"): go("profile")
    if st.button("Change Password"): st.success("Password change option - Demo")
    if st.button("About App"): st.info("Iris Flower Detector v1.0 - Made for Sanvi")
    if st.button("← Home"): go("home")
    if st.button("Log Out"): go("splash")
