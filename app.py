import streamlit as st
from PIL import Image
from datetime import datetime

st.set_page_config(
    page_title="Iris Flower Detector",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# -------------------- STYLE --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.stApp {
    background: linear-gradient(180deg, #fbfaff 0%, #f4f1ff 100%);
}
.block-container {
    max-width: 430px;
    padding: 18px 14px 90px 14px;
}
header, footer, #MainMenu {visibility:hidden;}

.logo-box {
    width:72px;height:72px;border-radius:20px;
    margin:8px auto 12px auto;
    background:linear-gradient(135deg,#5b31c8,#7b50e8);
    display:flex;align-items:center;justify-content:center;
    color:white;font-size:38px;box-shadow:0 8px 24px rgba(91,49,200,.22);
}
.title {text-align:center;color:#17155b;font-size:25px;font-weight:700;margin-bottom:4px;}
.subtitle {text-align:center;color:#65648a;font-size:14px;margin-bottom:18px;}
.hero {
    border-radius:20px;overflow:hidden;position:relative;
    background:#ddd;box-shadow:0 8px 24px rgba(30,20,80,.12);
}
.hero img {width:100%;display:block;}
.card {
    background:rgba(255,255,255,.96);border:1px solid #e8e4f4;
    border-radius:18px;padding:15px;box-shadow:0 5px 18px rgba(35,25,85,.06);
    margin-bottom:12px;
}
.section-title {color:#17155b;font-size:18px;font-weight:700;margin:5px 0 12px;}
.small {color:#777594;font-size:12px;}
.result-title {color:#17155b;font-size:20px;font-weight:700;margin:7px 0 2px;}
.badge {
    display:inline-block;background:#d9f7e9;color:#14865b;
    border-radius:9px;padding:5px 9px;font-size:12px;font-weight:700;
}
.nav-label {font-size:11px;color:#66658a;text-align:center;}
.stButton > button {
    border-radius:14px !important;
    min-height:43px !important;
    font-weight:600 !important;
    border:1px solid #ddd8ee !important;
    background:white !important;
    color:#2e226d !important;
}
.primary .stButton > button {
    background:linear-gradient(90deg,#5630c5,#7249d9) !important;
    color:white !important;border:none !important;
}
div[data-testid="stFileUploader"] {
    background:white;border:1px dashed #b9acd9;border-radius:14px;padding:8px;
}
input {
    border-radius:12px !important;
}
hr {border-color:#e8e4f4;}
</style>
""", unsafe_allow_html=True)

FLOWER_IMG = "https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=1000&q=85"
IRIS_IMG = "https://images.unsplash.com/photo-1597848212624-a19eb35e2651?w=1000&q=85"
IRIS_IMG_2 = "https://images.unsplash.com/photo-1588007375246-3f5e0a4b2f4b?w=1000&q=85"

# -------------------- STATE --------------------
if "screen" not in st.session_state:
    st.session_state.screen = "splash"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "history" not in st.session_state:
    st.session_state.history = [
        ("Iris germanica", "98%", "22 Sep 2026, 10:24 AM", IRIS_IMG),
        ("Iris versicolor", "95%", "21 Sep 2026, 05:12 PM", IRIS_IMG_2),
        ("Iris pseudacorus", "93%", "20 Sep 2026, 02:37 PM", IRIS_IMG),
        ("Iris sibirica", "90%", "18 Sep 2026, 11:03 AM", IRIS_IMG_2),
        ("Iris germanica", "97%", "16 Sep 2026, 09:45 AM", IRIS_IMG),
    ]
if "selected_flower" not in st.session_state:
    st.session_state.selected_flower = "Iris germanica"

# -------------------- HELPERS --------------------
def go(screen):
    st.session_state.screen = screen
    st.rerun()

def logo():
    st.markdown('<div class="logo-box">🌸</div>', unsafe_allow_html=True)

def bottom_nav(active="home"):
    st.markdown("<hr>", unsafe_allow_html=True)
    cols = st.columns(4)
    items = [("home","⌂","Home"),("history","◷","History"),("profile","●","Profile"),("settings","⚙","Settings")]
    for col,(key,icon,label) in zip(cols,items):
        with col:
            if st.button(f"{icon}\n{label}", key=f"nav_{key}"):
                go(key)

def image_card(url, height=210):
    st.markdown(
        f'<div class="hero"><img src="{url}" style="height:{height}px;object-fit:cover;"></div>',
        unsafe_allow_html=True
    )

def flower_result():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    image_card(IRIS_IMG, 190)
    st.markdown('<div class="result-title">Iris germanica</div><div class="small">German Iris</div><br><span class="badge">98% Match</span>', unsafe_allow_html=True)
    st.markdown("### Key Features")
    st.markdown("**Color** — Purple with yellow markings  \n**Bloom Time** — Spring – Early Summer  \n**Height** — 60–90 cm  \n**Habitat** — Gardens, meadows, wetlands")
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("View More Details", key="more_details", use_container_width=True):
        go("details")
    if st.button("Scan Another", key="scan_another", use_container_width=True):
        go("camera")

# -------------------- SPLASH --------------------
if st.session_state.screen == "splash":
    st.write("")
    logo()
    st.markdown('<div class="title">Iris Flower Detector</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Identify Flowers. Explore Nature.</div>', unsafe_allow_html=True)
    image_card(FLOWER_IMG, 360)
    st.markdown("<br><div style='text-align:center;color:#666;font-size:12px;'>Loading...</div>", unsafe_allow_html=True)
    if st.button("Continue", key="splash_continue", use_container_width=True):
        go("login")

# -------------------- LOGIN --------------------
elif st.session_state.screen == "login":
    logo()
    st.markdown('<div class="title" style="font-size:21px;">Iris Flower Detector</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Identify flowers using your camera<br>or gallery</div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    with tab1:
        st.text_input("Email or Phone Number", placeholder="Email or Phone Number")
        st.text_input("Password", type="password", placeholder="Password")
        st.markdown('<div class="primary">', unsafe_allow_html=True)
        if st.button("Login", use_container_width=True):
            st.session_state.logged_in = True
            go("home")
        st.markdown('</div>', unsafe_allow_html=True)
        st.caption("Forgot Password?")
        st.markdown("<div style='text-align:center;'>OR</div>", unsafe_allow_html=True)
        if st.button("🌈  Continue with Google", use_container_width=True):
            st.session_state.logged_in = True
            go("home")
        st.markdown("<div style='text-align:center;color:#777;'>Don't have an account? <b>Sign Up</b></div>", unsafe_allow_html=True)
    with tab2:
        st.text_input("Full Name", key="signup_name")
        st.text_input("Email", key="signup_email")
        st.text_input("Create Password", type="password", key="signup_password")
        if st.button("Create Account", use_container_width=True):
            st.session_state.logged_in = True
            go("home")

# -------------------- HOME --------------------
elif st.session_state.screen == "home":
    c1,c2,c3 = st.columns([1,5,1])
    with c1:
        if st.button("☰", key="menu"):
            st.info("Menu")
    with c2:
        st.markdown("### Hello, Sanvi! 👋")
        st.markdown('<div class="small">Discover the beauty of flowers around you.</div>', unsafe_allow_html=True)
    with c3:
        st.markdown("🔔")
    st.write("")
    st.markdown(
        f'<div class="hero"><img src="{IRIS_IMG}" style="height:165px;object-fit:cover;"><div style="position:absolute;left:50%;bottom:18px;transform:translateX(-50%);width:72%;background:linear-gradient(90deg,#5a31c7,#7549db);color:white;border-radius:28px;padding:12px;text-align:center;font-weight:700;">📷 &nbsp; Scan Flower<br><span style="font-size:11px;font-weight:400;">Identify an iris flower</span></div></div>',
        unsafe_allow_html=True
    )
    st.write("")
    grid = st.columns(2)
    buttons = [("◷","History","history"),("▧","Gallery","gallery"),("▢","Learn","learn"),("⚙","Settings","settings")]
    for col,(ic,label,target) in zip(grid*2,buttons):
        with col:
            if st.button(f"{ic}\n{label}", key=f"home_{target}", use_container_width=True):
                go(target)
    st.write("")
    if st.button("📷  Scan Flower", key="home_scan", use_container_width=True):
        go("camera")
    bottom_nav("home")

# -------------------- CAMERA / SCAN --------------------
elif st.session_state.screen == "camera":
    c1,c2 = st.columns([1,6])
    with c1:
        if st.button("×", key="close_camera"):
            go("home")
    with c2:
        st.markdown("### Scan Iris Flower")
    st.markdown('<div style="background:#111;border-radius:18px;padding:8px;">', unsafe_allow_html=True)
    camera = st.camera_input("Take a flower photo")
    st.markdown("</div>", unsafe_allow_html=True)
    st.caption("Place the iris flower within the frame\nMake sure the flower is clear and well lit")
    if camera is not None:
        go("processing")
    uploaded = st.file_uploader("Or choose from gallery", type=["jpg","jpeg","png"], label_visibility="collapsed")
    if uploaded is not None:
        go("processing")

# -------------------- PROCESSING --------------------
elif st.session_state.screen == "processing":
    st.write("")
    st.write("")
    st.markdown("<div style='text-align:center;font-size:20px;font-weight:700;color:#17155b;'>Analyzing the flower...</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;color:#777;font-size:13px;margin-top:8px;'>Please wait while we identify<br>the iris species.</div>", unsafe_allow_html=True)
    st.markdown("<br><div style='text-align:center;font-size:80px;'>🌸</div>", unsafe_allow_html=True)
    st.progress(0.82)
    if st.button("Show Result", use_container_width=True):
        st.session_state.history.insert(0, ("Iris germanica","98%",datetime.now().strftime("%d %b %Y, %I:%M %p"),IRIS_IMG))
        go("result")

# -------------------- RESULT --------------------
elif st.session_state.screen == "result":
    if st.button("‹  Result", key="result_back"):
        go("home")
    flower_result()

# -------------------- DETAILS --------------------
elif st.session_state.screen == "details":
    if st.button("‹  Flower Details", key="details_back"):
        go("result")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    image_card(IRIS_IMG, 180)
    st.markdown("### Iris germanica")
    st.markdown('<div class="small">German Iris</div><br><span class="badge">98% Match</span>', unsafe_allow_html=True)
    st.write("")
    t1,t2,t3 = st.tabs(["About","Care","More Photos"])
    with t1:
        st.markdown("**Description**")
        st.write("Iris germanica, commonly known as the German Iris, is a perennial flowering plant known for its striking purple, blue, and yellow blooms. It is widely grown in gardens and native to Europe.")
        st.markdown("**Quick Facts**")
        st.write("Scientific Name — Iris germanica")
        st.write("Family — Iridaceae")
        st.write("Bloom Time — Spring – Early Summer")
    with t2:
        st.write("Give the plant bright light, well-drained soil and moderate watering.")
    with t3:
        image_card(IRIS_IMG_2, 170)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------- HISTORY --------------------
elif st.session_state.screen == "history":
    if st.button("‹  Scan History", key="history_back"):
        go("home")
    st.markdown('<div class="section-title">Scan History</div>', unsafe_allow_html=True)
    for i,(name,match,date,img) in enumerate(st.session_state.history):
        c1,c2,c3 = st.columns([1.2,4.5,0.7])
        with c1:
            st.image(img, width=62)
        with c2:
            st.markdown(f"**{name}**")
            st.markdown(f'<div class="small">{date}<br>{match}</div>', unsafe_allow_html=True)
        with c3:
            if st.button("›", key=f"hist_{i}"):
                st.session_state.selected_flower = name
                go("details")
        st.markdown("---")
    bottom_nav("history")

# -------------------- PROFILE --------------------
elif st.session_state.screen == "profile":
    if st.button("‹  Profile", key="profile_back"):
        go("home")
    st.markdown("<div style='text-align:center;font-size:64px;'>👤</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;font-size:20px;font-weight:700;color:#17155b;'>Sanvi Mandavkar</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;color:#777;'>sanvi@gmail.com</div>", unsafe_allow_html=True)
    st.write("")
    for label,value in [("Member Since","12 Mar 2026"),("Total Scans","32"),("Favorite Flower","Iris germanica")]:
        st.markdown(f'<div class="card"><b>{label}</b><span style="float:right;color:#555;">{value}</span></div>', unsafe_allow_html=True)
    for label,target in [("My Plants","learn"),("Saved Flowers","details"),("Help & Support","settings")]:
        if st.button(f"♧  {label}  ›", key=f"profile_{label}", use_container_width=True):
            go(target)
    bottom_nav("profile")

# -------------------- SETTINGS --------------------
elif st.session_state.screen == "settings":
    if st.button("‹  Settings", key="settings_back"):
        go("home")
    st.markdown('<div class="section-title">Account</div>', unsafe_allow_html=True)
    if st.button("♙  Edit Profile  ›", use_container_width=True):
        go("profile")
    if st.button("🔒  Change Password  ›", use_container_width=True):
        st.info("Password settings opened.")
    st.markdown('<div class="section-title">App Preferences</div>', unsafe_allow_html=True)
    st.toggle("Notifications", value=True)
    st.selectbox("Camera Quality", ["High","Medium","Low"])
    st.selectbox("Language", ["English","Marathi","Hindi"])
    st.markdown('<div class="section-title">About</div>', unsafe_allow_html=True)
    if st.button("ⓘ  About App  ›", use_container_width=True):
        st.info("Iris Flower Detector helps identify iris flowers from camera or gallery photos.")
    if st.button("▣  Privacy Policy  ›", use_container_width=True):
        st.info("Your demo data is kept only in this Streamlit session.")
    if st.button("Log Out", use_container_width=True):
        st.session_state.logged_in = False
        go("login")
    bottom_nav("settings")

# -------------------- GALLERY / LEARN --------------------
elif st.session_state.screen == "gallery":
    if st.button("‹  Gallery", key="gallery_back"):
        go("home")
    st.markdown('<div class="section-title">Flower Gallery</div>', unsafe_allow_html=True)
    cols = st.columns(2)
    for i,img in enumerate([IRIS_IMG,IRIS_IMG_2,FLOWER_IMG,IRIS_IMG]):
        with cols[i%2]:
            st.image(img, use_container_width=True)
            st.caption(["Iris germanica","Iris versicolor","Garden flowers","Iris sibirica"][i])

elif st.session_state.screen == "learn":
    if st.button("‹  Learn", key="learn_back"):
        go("home")
    st.markdown('<div class="section-title">Learn About Irises</div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><b>🌸 Iris Flowers</b><br><span class="small">Irises are known for their colorful petals and distinctive flower shape. Explore different species and learn how to care for them.</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><b>💧 Basic Care</b><br><span class="small">Use well-drained soil, provide suitable sunlight, and avoid overwatering.</span></div>', unsafe_allow_html=True)
