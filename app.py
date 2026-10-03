import streamlit as st
from PIL import Image
import time

st.set_page_config(
    page_title="Iris Flower Detector",
    page_icon="🌸",
    layout="centered"
)

# =========================
# STYLE
# =========================
st.markdown("""
<style>
.stApp {
    background:#e9e6ff;
}
header, footer, #MainMenu {
    visibility:hidden;
}
.block-container {
    background:white;
    max-width:390px;
    padding:0 !important;
    border-radius:28px;
    overflow:hidden;
    box-shadow:0 10px 35px rgba(70,40,150,.18);
}
.inner {
    padding:18px;
}
.logo {
    width:65px;
    height:65px;
    background:#4f33d1;
    border-radius:17px;
    margin:auto;
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:32px;
}
.title {
    text-align:center;
    color:#20134b;
    font-size:22px;
    font-weight:800;
    margin-top:8px;
}
.sub {
    text-align:center;
    color:#8a84a6;
    font-size:12px;
}
.hero {
    height:180px;
    border-radius:18px;
    background-size:cover;
    background-position:center;
    margin:15px 0;
    position:relative;
}
.hero-button {
    position:absolute;
    bottom:12px;
    left:12px;
    right:12px;
    background:rgba(79,51,209,.92);
    color:white;
    padding:12px;
    border-radius:14px;
}
.grid {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:10px;
}
.card {
    background:#f7f5ff;
    border:1px solid #ebe6ff;
    border-radius:14px;
    padding:17px 8px;
    text-align:center;
    color:#302565;
    font-size:12px;
    font-weight:600;
}
.badge {
    background:#d1fae5;
    color:#065f46;
    border-radius:20px;
    padding:4px 9px;
    font-size:10px;
    font-weight:700;
}
.info {
    background:#f8f7ff;
    border-radius:14px;
    padding:13px;
    margin-top:10px;
}
.row {
    display:flex;
    justify-content:space-between;
    gap:8px;
    margin:8px 0;
    font-size:11px;
    color:#5a5575;
}
.scan-frame {
    width:240px;
    height:320px;
    border:2px solid white;
    border-radius:20px;
}
</style>
""", unsafe_allow_html=True)


# =========================
# SESSION
# =========================
if "page" not in st.session_state:
    st.session_state.page = "splash"

if "result_img" not in st.session_state:
    st.session_state.result_img = None

if "score" not in st.session_state:
    st.session_state.score = 98

if "history" not in st.session_state:
    st.session_state.history = [
        ["Iris germanica", "22 Sep 2026, 10:24 AM", "98%"],
        ["Iris versicolor", "21 Sep 2026, 05:18 PM", "95%"],
        ["Iris pseudacorus", "20 Sep 2026, 02:37 PM", "93%"],
        ["Iris sibirica", "18 Sep 2026, 11:02 AM", "90%"],
        ["Iris germanica", "16 Sep 2026, 09:45 AM", "97%"]
    ]


def go(page):
    st.session_state.page = page
    st.rerun()


IRIS_IMAGE = (
    "https://images.unsplash.com/"
    "photo-1518895949257-7621c3c786d7"
    "?auto=format&fit=crop&w=900&q=85"
)


# =========================
# 1 SPLASH
# =========================
if st.session_state.page == "splash":

    st.markdown(f"""
    <div style="
        height:650px;
        background:
        linear-gradient(
            rgba(35,10,80,.05),
            rgba(35,10,80,.35)
        ),
        url('{IRIS_IMAGE}');
        background-size:cover;
        background-position:center;
        text-align:center;
        padding-top:35px;
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
            bottom:90px;
            left:0;
            right:0;
            color:white;
            font-size:11px;
        ">
            Loading...
        </div>

    </div>
    """, unsafe_allow_html=True)

    if st.button("Get Started →", use_container_width=True):
        go("login")


# =========================
# 2 LOGIN
# =========================
elif st.session_state.page == "login":

    st.markdown("""
    <div class="inner" style="text-align:center">

        <div class="logo">🌸</div>

        <div class="title">
            Iris Flower Detector
        </div>

        <div class="sub">
            Identify flowers using your camera or gallery
        </div>

        <div style="
            display:flex;
            gap:8px;
            margin:15px 0;
        ">
            <div style="
                flex:1;
                background:#4f33d1;
                color:white;
                padding:9px;
                border-radius:10px;
                font-size:12px;
                font-weight:bold;
            ">
                Login
            </div>

            <div style="
                flex:1;
                background:#f5f3ff;
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
        "Email",
        placeholder="📧 Email or Phone Number"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="🔒 Password"
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
        color:gray;
        font-size:11px;
    ">
        OR
    </div>
    """, unsafe_allow_html=True)

    if st.button("G  Continue with Google", use_container_width=True):
        go("home")

    st.markdown("""
    <div style="
        text-align:center;
        font-size:11px;
        margin:10px;
    ">
        Don't have an account?
        <b style="color:#4f33d1">Sign Up</b>
    </div>
    """, unsafe_allow_html=True)


# =========================
# 3 HOME
# =========================
elif st.session_state.page == "home":

    st.markdown("""
    <div class="inner">

        <div style="
            display:flex;
            justify-content:space-between;
            font-size:18px;
        ">
            <span>☰</span>
            <span>🔔</span>
        </div>

        <div style="margin-top:12px">

            <b style="
                color:#1e1142;
                font-size:17px;
            ">
                Hello, Sanvi! 👋
            </b>

            <br>

            <span style="
                color:#8a84a6;
                font-size:11px;
            ">
                Discover the beauty of flowers around you.
            </span>

        </div>

        <div class="hero"
             style="background-image:url(
             '""" + IRIS_IMAGE + """'
             );">

            <div class="hero-button">

                <b>📷 Scan Flower</b>

                <br>

                <small>
                    Identify an Iris flower
                </small>

            </div>

        </div>

        <div class="grid">

            <div class="card">
                🕒<br>History
            </div>

            <div class="card">
                🖼️<br>Gallery
            </div>

            <div class="card">
                📚<br>Learn
            </div>

            <div class="card">
                ⚙️<br>Settings
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        if st.button("🕒 History", use_container_width=True):
            go("history")

        if st.button("👤 Profile", use_container_width=True):
            go("profile")

    with c2:
        if st.button("📷 Scan Now", use_container_width=True):
            go("camera")

        if st.button("⚙️ Settings", use_container_width=True):
            go("settings")


# =========================
# 4 CAMERA / SCAN
# =========================
elif st.session_state.page == "camera":

    st.markdown("""
    <div class="inner">

        <div style="
            display:flex;
            justify-content:space-between;
            font-weight:bold;
            font-size:13px;
        ">
            <span>✕</span>
            <span>Scan Iris Flower</span>
            <span>⚡</span>
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
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

        <div class="scan-frame"></div>

        <div style="
            position:absolute;
            bottom:15px;
            left:0;
            right:0;
            text-align:center;
            color:white;
            background:rgba(0,0,0,.45);
            padding:10px;
            font-size:11px;
        ">
            Place the iris flower within the frame
            <br>
            Make sure the flower is clear and well lit
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<div class='inner'><b>Upload Flower Image</b></div>",
        unsafe_allow_html=True
    )

    uploaded = st.file_uploader(
        "Choose image",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

    camera = st.camera_input("Take Flower Photo")

    selected = camera if camera else uploaded

    if selected:

        st.session_state.result_img = Image.open(
            selected
        ).convert("RGB")

        go("processing")

    if st.button("← Back to Home", use_container_width=True):
        go("home")


# =========================
# 5 PROCESSING
# =========================
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

        <b style="
            color:#1e1142;
            font-size:16px;
        ">
            Analyzing the flower...
        </b>

        <small style="
            color:#8a84a6;
            margin-top:6px;
        ">
            Please wait while we identify
            the iris species.
        </small>

        <div style="
            margin:40px;
            width:140px;
            height:140px;
            border:3px solid #e9e5ff;
            border-top:3px solid #4f33d1;
            border-radius:50%;
            display:flex;
            justify-content:center;
            align-items:center;
            font-size:45px;
        ">
            🌸
        </div>

        <div style="
            width:180px;
            height:7px;
            background:#eeeaff;
            border-radius:10px;
        ">
            <div style="
                width:70%;
                height:7px;
                background:#4f33d1;
                border-radius:10px;
            "></div>
        </div>

    </div>
    """, unsafe_allow_html=True)

    time.sleep(1.5)

    go("result")


# =========================
# 6 RESULT
# =========================
elif st.session_state.page == "result":

    if st.session_state.result_img:

        st.image(
            st.session_state.result_img,
            use_container_width=True
        )

    else:

        st.image(
            IRIS_IMAGE,
            use_container_width=True
        )

    st.markdown("""
    <div class="inner">

        <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
        ">

            <div>

                <b style="
                    color:#1e1142;
                    font-size:17px;
                ">
                    Iris germanica
                </b>

                <br>

                <small style="color:#8a84a6">
                    German Iris
                </small>

            </div>

            <span class="badge">
                98% Match
            </span>

        </div>

        <div class="info">

            <b style="font-size:12px">
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


# =========================
# 7 DETAILS
# =========================
elif st.session_state.page == "details":

    if st.session_state.result_img:

        st.image(
            st.session_state.result_img,
            use_container_width=True
        )

    st.markdown("""
    <div class="inner">

        <b style="
            color:#1e1142;
            font-size:17px;
        ">
            Iris germanica
        </b>

        <br>

        <small style="color:#8a84a6">
            German Iris
        </small>

        <span class="badge">
            98% Match
        </span>

        <div style="
            display:flex;
            gap:7px;
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
                padding:6px 13px;
                border-radius:20px;
                font-size:11px;
            ">
                Care
            </span>

            <span style="
                background:#f5f3ff;
                padding:6px 13px;
                border-radius:20px;
                font-size:11px;
            ">
                More Photos
            </span>

        </div>

        <div class="info">

            <b>Description</b>

            <p style="
                font-size:11px;
                color:#5a5575;
                line-height:1.6;
            ">
                Iris germanica, commonly known as the
                German Iris, is a perennial flowering
                plant known for its striking purple,
                blue and yellow blooms.
            </p>

        </div>

        <div class="info">

            <b>Quick Facts</b>

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

        </div>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "← Back to Result",
        use_container_width=True
    ):
        go("result")


# =========================
# 8 HISTORY
# =========================
elif st.session_state.page == "history":

    st.markdown("""
    <div class="inner">

        <b style="
            color:#1e1142;
            font-size:16px;
        ">
            ← Scan History
        </b>

    </div>
    """, unsafe_allow_html=True)

    for item in st.session_state.history:

        st.markdown(f"""
        <div style="
            display:flex;
            align-items:center;
            gap:10px;
            padding:12px 18px;
            border-bottom:1px solid #f0ecff;
        ">

            <div style="
                width:48px;
                height:48px;
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
                    color:#302565;
                    font-size:12px;
                ">
                    {item[0]}
                </b>

                <br>

                <small style="
                    color:#999;
                    font-size:10px;
                ">
                    {item[1]}
                </small>

                <br>

                <span class="badge">
                    {item[2]}
                </span>

            </div>

            <span style="
                margin-left:auto;
                color:#999;
            ">
                ›
            </span>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "← Home",
        use_container_width=True
    ):
        go("home")


# =========================
# 9 PROFILE
# =========================
elif st.session_state.page == "profile":

    st.markdown("""
    <div class="inner">

        <div style="
            display:flex;
            justify-content:space-between;
        ">
            <span>←</span>
            <b>Profile</b>
            <span>⚙️</span>
        </div>

        <div style="
            width:70px;
            height:70px;
            background:#ede9fe;
            border-radius:50%;
            margin:20px auto 10px;
            display:flex;
            justify-content:center;
            align-items:center;
            font-size:30px;
        ">
            👤
        </div>

        <div style="text-align:center">

            <b>Sanvi Mandavkar</b>

            <br>

            <small style="color:#8a84a6">
                sanvi@gmail.com
            </small>

        </div>

        <div class="info">

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

        <div class="info">

            <div style="
                padding:9px 0;
                border-bottom:1px solid #eee;
                font-size:12px;
            ">
                🌿 My Plants
                <span style="float:right">›</span>
            </div>

            <div style="
                padding:9px 0;
                border-bottom:1px solid #eee;
                font-size:12px;
            ">
                🔖 Saved Flowers
                <span style="float:right">›</span>
            </div>

            <div style="
                padding:9px 0;
                font-size:12px;
            ">
                ❓ Help & Support
                <span style="float:right">›</span>
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


# =========================
# 10 SETTINGS
# =========================
elif st.session_state.page == "settings":

    st.markdown("""
    <div class="inner">

        <b style="
            color:#1e1142;
            font-size:16px;
        ">
            ← Settings
        </b>

        <div style="margin-top:20px">

            <b style="font-size:12px">
                Account
            </b>

            <div class="info">

                <div style="
                    padding:9px 0;
                    font-size:12px;
                ">
                    👤 Edit Profile
                    <span style="float:right">›</span>
                </div>

                <div style="
                    padding:9px 0;
                    font-size:12px;
                ">
                    🔒 Change Password
                    <span style="float:right">›</span>
                </div>

            </div>

        </div>

        <div style="margin-top:18px">

            <b style="font-size:12px">
                App Preferences
            </b>

            <div class="info">

                <div style="
                    padding:9px 0;
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
                    padding:9px 0;
                    font-size:12px;
                ">
                    📷 Camera Quality
                    <span style="float:right">
                        High ›
                    </span>
                </div>

                <div style="
                    padding:9px 0;
                    font-size:12px;
                ">
                    🌐 Language
                    <span style="float:right">
                        English ›
                    </span>
                </div>

            </div>

        </div>

        <div style="margin-top:18px">

            <b style="font-size:12px">
                About
            </b>

            <div class="info">

                <div style="
                    padding:9px 0;
                    font-size:12px;
                ">
                    ℹ️ About App
                    <span style="float:right">›</span>
                </div>

                <div style="
                    padding:9px 0;
                    font-size:12px;
                ">
                    🔐 Privacy Policy
                    <span style="float:right">›</span>
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
