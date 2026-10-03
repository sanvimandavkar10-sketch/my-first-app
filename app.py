import streamlit as st
from PIL import Image
import time

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Iris Flower Detector",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>

.stApp {
    background: #e9e6ff;
}

header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.block-container {
    max-width: 420px !important;
    padding: 0 !important;
    margin: auto !important;
    background: white;
    min-height: 100vh;
    overflow: hidden;
}

.logo {
    width: 64px;
    height: 64px;
    background: #4f33d1;
    border-radius: 17px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    margin: auto;
}

.title {
    color: #1e1142;
    font-size: 23px;
    font-weight: 800;
    text-align: center;
    margin-top: 10px;
}

.subtitle {
    color: #8a84a6;
    font-size: 12px;
    text-align: center;
}

.inner {
    padding: 18px;
}

.card {
    background: #f7f5ff;
    border: 1px solid #ede8ff;
    border-radius: 15px;
    padding: 16px;
    text-align: center;
    color: #302565;
    font-size: 12px;
    font-weight: 600;
}

.info-card {
    background: #f8f7ff;
    border-radius: 14px;
    padding: 14px;
    margin-top: 12px;
}

.row {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    margin: 9px 0;
    font-size: 11px;
    color: #5a5575;
}

.badge {
    display: inline-block;
    background: #d1fae5;
    color: #065f46;
    padding: 4px 9px;
    border-radius: 20px;
    font-size: 10px;
    font-weight: 700;
}

.hero {
    height: 190px;
    border-radius: 18px;
    background-size: cover;
    background-position: center;
    position: relative;
    margin: 16px 0;
    overflow: hidden;
}

.hero-button {
    position: absolute;
    bottom: 12px;
    left: 12px;
    right: 12px;
    background: rgba(79, 51, 209, 0.92);
    color: white;
    padding: 12px;
    border-radius: 14px;
}

.scan-box {
    width: 235px;
    height: 310px;
    border: 2px solid white;
    border-radius: 20px;
}

.stButton > button {
    background: #4f33d1 !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    min-height: 45px !important;
    font-weight: 700 !important;
}

.stTextInput input {
    border-radius: 12px !important;
}

.stFileUploader {
    background: #f7f5ff;
    border-radius: 14px;
    padding: 5px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "splash"

if "result_img" not in st.session_state:
    st.session_state.result_img = None

if "score" not in st.session_state:
    st.session_state.score = 98

if "history" not in st.session_state:
    st.session_state.history = [
        {
            "name": "Iris germanica",
            "time": "22 Sep 2026, 10:24 AM",
            "score": "98%"
        },
        {
            "name": "Iris versicolor",
            "time": "21 Sep 2026, 05:18 PM",
            "score": "95%"
        },
        {
            "name": "Iris pseudacorus",
            "time": "20 Sep 2026, 02:37 PM",
            "score": "93%"
        },
        {
            "name": "Iris sibirica",
            "time": "18 Sep 2026, 11:02 AM",
            "score": "90%"
        }
    ]

# =========================================================
# FUNCTIONS
# =========================================================
def go(page):
    st.session_state.page = page
    st.rerun()


IRIS_IMAGE = (
    "https://images.unsplash.com/"
    "photo-1518895949257-7621c3c786d7"
    "?auto=format&fit=crop&w=900&q=85"
)

# =========================================================
# 1. SPLASH SCREEN
# =========================================================
if st.session_state.page == "splash":

    splash_html = f"""
<div style="
height:650px;
background:
linear-gradient(
rgba(35,10,80,.12),
rgba(35,10,80,.45)
),
url('{IRIS_IMAGE}');
background-size:cover;
background-position:center;
text-align:center;
padding-top:35px;
position:relative;
">

<div class="logo">🌸</div>

<div style="
color:white;
font-size:25px;
font-weight:800;
margin-top:10px;
">
Iris Flower Detector
</div>

<div style="
color:white;
font-size:13px;
margin-top:5px;
">
Identify Flowers. Explore Nature.
</div>

<div style="
position:absolute;
bottom:95px;
left:0;
right:0;
color:white;
font-size:11px;
">
Identify beautiful Iris flowers easily
</div>

</div>
"""

    st.markdown(
        splash_html,
        unsafe_allow_html=True
    )

    if st.button(
        "Get Started →",
        use_container_width=True
    ):
        go("login")

# =========================================================
# 2. LOGIN / SIGN UP
# =========================================================
elif st.session_state.page == "login":

    st.markdown("""
<div class="inner" style="text-align:center;">

<div class="logo">🌸</div>

<div class="title">
Iris Flower Detector
</div>

<div class="subtitle">
Identify flowers using your camera or gallery
</div>

<div style="
display:flex;
gap:8px;
margin:16px 0;
">

<div style="
flex:1;
background:#4f33d1;
color:white;
padding:9px;
border-radius:10px;
font-size:12px;
font-weight:700;
">
Login
</div>

<div style="
flex:1;
background:#f5f3ff;
color:#5a5575;
padding:9px;
border-radius:10px;
font-size:12px;
">
Sign Up
</div>

</div>

</div>
""", unsafe_allow_html=True)

    email = st.text_input(
        "Email or Phone Number",
        placeholder="📧 Email or Phone Number"
    )

    password = st.text_input(
        "Password",
        placeholder="🔒 Password",
        type="password"
    )

    if st.button("Login", use_container_width=True):
        go("home")

    st.markdown("""
<div style="
text-align:center;
color:#4f33d1;
font-size:11px;
margin:8px;
">
Forgot Password?
</div>

<div style="
text-align:center;
color:#999;
font-size:11px;
margin:8px;
">
OR
</div>
""", unsafe_allow_html=True)

    if st.button(
        "G  Continue with Google",
        use_container_width=True
    ):
        go("home")

    st.markdown("""
<div style="
text-align:center;
font-size:11px;
margin:12px;
">
Don't have an account?
<b style="color:#4f33d1;">
Sign Up
</b>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 3. HOME
# =========================================================
elif st.session_state.page == "home":

    st.markdown("""
<div class="inner">

<div style="
display:flex;
justify-content:space-between;
font-size:20px;
">
<span>☰</span>
<span>🔔</span>
</div>

<div style="margin-top:12px;">

<b style="
font-size:17px;
color:#1e1142;
">
Hello, Sanvi! 👋
</b>

<br>

<small style="
color:#8a84a6;
font-size:11px;
">
Discover the beauty of flowers around you.
</small>

</div>

</div>
""", unsafe_allow_html=True)

    hero_html = f"""
<div class="inner">

<div class="hero"
style="background-image:url('{IRIS_IMAGE}');">

<div class="hero-button">

<b style="font-size:14px;">
📷 Scan Flower
</b>

<br>

<small>
Identify an Iris flower
</small>

</div>

</div>

</div>
"""

    st.markdown(
        hero_html,
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            '<div class="card">🕒<br>History</div>',
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            '<div class="card">🖼️<br>Gallery</div>',
            unsafe_allow_html=True
        )

    st.write("")

    c3, c4 = st.columns(2)

    with c3:
        st.markdown(
            '<div class="card">📚<br>Learn</div>',
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            '<div class="card">⚙️<br>Settings</div>',
            unsafe_allow_html=True
        )

    st.write("")

    c5, c6 = st.columns(2)

    with c5:
        if st.button(
            "🕒 History",
            use_container_width=True
        ):
            go("history")

    with c6:
        if st.button(
            "📷 Scan Now",
            use_container_width=True
        ):
            go("camera")

    c7, c8 = st.columns(2)

    with c7:
        if st.button(
            "👤 Profile",
            use_container_width=True
        ):
            go("profile")

    with c8:
        if st.button(
            "⚙️ Settings",
            use_container_width=True
        ):
            go("settings")

# =========================================================
# 4. CAMERA / SCAN
# =========================================================
elif st.session_state.page == "camera":

    st.markdown("""
<div class="inner">

<div style="
display:flex;
justify-content:space-between;
font-size:13px;
font-weight:700;
">
<span>✕</span>
<span>Scan Iris Flower</span>
<span>⚡</span>
</div>

</div>
""", unsafe_allow_html=True)

    camera_html = f"""
<div style="
height:430px;
background:url('{IRIS_IMAGE}');
background-size:cover;
background-position:center;
display:flex;
align-items:center;
justify-content:center;
position:relative;
">

<div class="scan-box"></div>

<div style="
position:absolute;
bottom:12px;
left:10px;
right:10px;
text-align:center;
color:white;
background:rgba(0,0,0,.5);
padding:10px;
border-radius:10px;
font-size:11px;
">
Place the iris flower within the frame
<br>
Make sure the flower is clear and well lit
</div>

</div>
"""

    st.markdown(
        camera_html,
        unsafe_allow_html=True
    )

    st.markdown("""
<div class="inner">

<b style="font-size:13px;">
Upload Flower Image
</b>

</div>
""", unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Upload",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

    camera_file = st.camera_input(
        "Take a Photo"
    )

    selected_file = (
        camera_file
        if camera_file is not None
        else uploaded_file
    )

    if selected_file is not None:

        image = Image.open(
            selected_file
        ).convert("RGB")

        st.session_state.result_img = image

        go("processing")

    if st.button(
        "← Back to Home",
        use_container_width=True
    ):
        go("home")

# =========================================================
# 5. PROCESSING
# =========================================================
elif st.session_state.page == "processing":

    st.markdown("""
<div style="
height:650px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
text-align:center;
">

<div style="
font-size:17px;
font-weight:800;
color:#1e1142;
">
Analyzing the flower...
</div>

<div style="
font-size:11px;
color:#8a84a6;
margin-top:7px;
">
Please wait while we identify the iris species.
</div>

<div style="
margin:40px;
width:135px;
height:135px;
border:3px solid #e9e5ff;
border-top:3px solid #4f33d1;
border-radius:50%;
display:flex;
align-items:center;
justify-content:center;
font-size:45px;
">
🌸
</div>

<div style="
font-size:11px;
color:#8a84a6;
">
Scanning image...
</div>

</div>
""", unsafe_allow_html=True)

    time.sleep(1.5)

    st.session_state.score = 98

    go("result")

# =========================================================
# 6. RESULT
# =========================================================
elif st.session_state.page == "result":

    if st.session_state.result_img is not None:

        st.image(
            st.session_state.result_img,
            use_container_width=True
        )

    else:

        st.image(
            IRIS_IMAGE,
            use_container_width=True
        )

    score = st.session_state.score

    st.markdown(f"""
<div class="inner">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<div>

<b style="
font-size:17px;
color:#1e1142;
">
Iris germanica
</b>

<br>

<small style="
color:#8a84a6;
">
German Iris
</small>

</div>

<span class="badge">
{score}% Match
</span>

</div>

<div class="info-card">

<b style="font-size:12px;">
Key Features
</b>

<div class="row">
<span>🎨 Color</span>
<span>Purple with yellow markings</span>
</div>

<div class="row">
<span>🌼 Bloom Time</span>
<span>Spring - Early Summer</span>
</div>

<div class="row">
<span>📏 Height</span>
<span>60 - 90 cm</span>
</div>

<div class="row">
<span>🌍 Habitat</span>
<span>Gardens, meadows, wetlands</span>
</div>

</div>

</div>
""", unsafe_allow_html=True)

    if st.button(
        "View More Details",
        use_container_width=True
    ):
        go("details")

    if st.button(
        "Scan Another",
        use_container_width=True
    ):
        go("camera")

    if st.button(
        "← Home",
        use_container_width=True
    ):
        go("home")

# =========================================================
# 7. FLOWER DETAILS
# =========================================================
elif st.session_state.page == "details":

    if st.session_state.result_img is not None:

        st.image(
            st.session_state.result_img,
            use_container_width=True
        )

    st.markdown("""
<div class="inner">

<b style="
font-size:18px;
color:#1e1142;
">
Iris germanica
</b>

<br>

<small style="color:#8a84a6;">
German Iris
</small>

<span class="badge">
98% Match
</span>

<div style="
display:flex;
gap:8px;
margin:15px 0;
">

<span style="
background:#4f33d1;
color:white;
padding:6px 13px;
border-radius:20px;
font-size:11px;
">
About
</span>

<span style="
background:#f5f3ff;
color:#5a5575;
padding:6px 13px;
border-radius:20px;
font-size:11px;
">
Care
</span>

<span style="
background:#f5f3ff;
color:#5a5575;
padding:6px 13px;
border-radius:20px;
font-size:11px;
">
More Photos
</span>

</div>

<div class="info-card">

<b style="font-size:12px;">
Description
</b>

<p style="
font-size:11px;
color:#5a5575;
line-height:1.7;
">
Iris germanica, commonly known as the German Iris,
is a perennial flowering plant known for its striking
purple, blue and yellow blooms. It is widely grown
in gardens.
</p>

</div>

<div class="info-card">

<b style="font-size:12px;">
Quick Facts
</b>

<div class="row">
<span>🔬 Scientific Name</span>
<span>Iris germanica</span>
</div>

<div class="row">
<span>🏷️ Family</span>
<span>Iridaceae</span>
</div>

<div class="row">
<span>⏰ Bloom Time</span>
<span>Spring - Early Summer</span>
</div>

<div class="row">
<span>🌍 Habitat</span>
<span>Gardens and meadows</span>
</div>

</div>

</div>
""", unsafe_allow_html=True)

    if st.button(
        "← Back to Result",
        use_container_width=True
    ):
        go("result")

# =========================================================
# 8. HISTORY
# =========================================================
elif st.session_state.page == "history":

    st.markdown("""
<div class="inner">

<b style="
font-size:18px;
color:#1e1142;
">
🕒 Scan History
</b>

</div>
""", unsafe_allow_html=True)

    for item in st.session_state.history:

        st.markdown(f"""
<div style="
display:flex;
gap:10px;
align-items:center;
padding:12px 18px;
border-bottom:1px solid #f0ecff;
">

<div style="
width:50px;
height:50px;
background:#eee8ff;
border-radius:12px;
display:flex;
align-items:center;
justify-content:center;
font-size:24px;
">
🌸
</div>

<div>

<b style="
font-size:12px;
color:#302565;
">
{item["name"]}
</b>

<br>

<small style="
font-size:10px;
color:#999;
">
{item["time"]}
</small>

<br>

<span class="badge">
{item["score"]}
</span>

</div>

<div style="
margin-left:auto;
color:#999;
font-size:20px;
">
›
</div>

</div>
""", unsafe_allow_html=True)

    st.write("")

    if st.button(
        "← Home",
        use_container_width=True
    ):
        go("home")

# =========================================================
# 9. PROFILE
# =========================================================
elif st.session_state.page == "profile":

    st.markdown("""
<div class="inner">

<div style="
display:flex;
justify-content:space-between;
font-size:14px;
font-weight:700;
">
<span>←</span>
<span>Profile</span>
<span>⚙️</span>
</div>

<div style="
width:70px;
height:70px;
background:#ede9fe;
border-radius:50%;
margin:20px auto 10px;
display:flex;
align-items:center;
justify-content:center;
font-size:30px;
">
👤
</div>

<div style="text-align:center;">

<b style="font-size:15px;">
Sanvi Mandavkar
</b>

<br>

<small style="color:#8a84a6;">
sanvi@gmail.com
</small>

</div>

<div class="info-card">

<div class="row">
<span>👤 Member Since</span>
<b>12 Mar 2026</b>
</div>

<div class="row">
<span>🔍 Total Scans</span>
<b>32</b>
</div>

<div class="row">
<span>⭐ Favorite Flower</span>
<b>Iris germanica</b>
</div>

</div>

<div class="info-card">

<div style="
padding:10px 0;
border-bottom:1px solid #e9e5ff;
font-size:12px;
">
🌿 My Plants
<span style="float:right;">›</span>
</div>

<div style="
padding:10px 0;
border-bottom:1px solid #e9e5ff;
font-size:12px;
">
🔖 Saved Flowers
<span style="float:right;">›</span>
</div>

<div style="
padding:10px 0;
font-size:12px;
">
❓ Help & Support
<span style="float:right;">›</span>
</div>

</div>

</div>
""", unsafe_allow_html=True)

    if st.button(
        "⚙️ Settings",
        use_container_width=True
    ):
        go("settings")

    if st.button(
        "← Home",
        use_container_width=True
    ):
        go("home")

# =========================================================
# 10. SETTINGS
# =========================================================
elif st.session_state.page == "settings":

    st.markdown("""
<div class="inner">

<b style="
font-size:18px;
color:#1e1142;
">
⚙️ Settings
</b>

<div style="margin-top:20px;">

<b style="font-size:12px;">
Account
</b>

<div class="info-card">

<div style="
padding:10px 0;
border-bottom:1px solid #e9e5ff;
font-size:12px;
">
👤 Edit Profile
<span style="float:right;">›</span>
</div>

<div style="
padding:10px 0;
font-size:12px;
">
🔒 Change Password
<span style="float:right;">›</span>
</div>

</div>

</div>

<div style="margin-top:18px;">

<b style="font-size:12px;">
App Preferences
</b>

<div class="info-card">

<div style="
padding:10px 0;
border-bottom:1px solid #e9e5ff;
font-size:12px;
">
🔔 Notifications
<span style="
float:right;
color:#4f33d1;
">
●
</span>
</div>

<div style="
padding:10px 0;
border-bottom:1px solid #e9e5ff;
font-size:12px;
">
📷 Camera Quality
<span style="float:right;">
High ›
</span>
</div>

<div style="
padding:10px 0;
font-size:12px;
">
🌐 Language
<span style="float:right;">
English ›
</span>
</div>

</div>

</div>

<div style="margin-top:18px;">

<b style="font-size:12px;">
About
</b>

<div class="info-card">

<div style="
padding:10px 0;
border-bottom:1px solid #e9e5ff;
font-size:12px;
">
ℹ️ About App
<span style="float:right;">›</span>
</div>

<div style="
padding:10px 0;
font-size:12px;
">
🔐 Privacy Policy
<span style="float:right;">›</span>
</div>

</div>

</div>

</div>
""", unsafe_allow_html=True)

    if st.button(
        "← Home",
        use_container_width=True
    ):
        go("home")

    if st.button(
        "↪ Log Out",
        use_container_width=True
    ):
        st.session_state.result_img = None
        go("splash")
