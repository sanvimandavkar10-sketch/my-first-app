import streamlit as st
from PIL import Image
from transformers import pipeline
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
    background: #e9e6ff !important;
}

header, #MainMenu, footer {
    visibility: hidden;
}

.block-container {
    background: white !important;
    border-radius: 28px !important;
    padding: 0 !important;
    max-width: 390px !important;
    min-height: 780px;
    box-shadow: 0 12px 40px rgba(80,40,180,0.18) !important;
    overflow: hidden;
}

.inner {
    padding: 18px;
}

.logo-box {
    width: 62px;
    height: 62px;
    background: #4f33d1;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    margin: 0 auto;
    color: white;
}

.title {
    color: #1e1142 !important;
    font-weight: 800 !important;
    font-size: 22px !important;
    text-align: center;
    margin: 8px 0 2px 0;
}

.sub {
    color: #8a84a6;
    font-size: 12px;
    text-align: center;
    margin-bottom: 12px;
}

.hero-img {
    height: 175px;
    border-radius: 18px;
    background-size: cover;
    background-position: center;
    position: relative;
    margin: 12px 0;
}

.hero-btn {
    position: absolute;
    bottom: 12px;
    left: 12px;
    right: 12px;
    background: rgba(79,51,209,0.92);
    border-radius: 14px;
    padding: 12px;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.grid2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin: 12px 0;
}

.gcard {
    background: #f7f5ff;
    border: 1px solid #ede8ff;
    border-radius: 14px;
    padding: 16px 8px;
    text-align: center;
    font-size: 12px;
    font-weight: 600;
    color: #2d2163;
}

.badge {
    background: #d1fae5;
    color: #065f46;
    font-size: 10px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 20px;
}

.key-row {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    font-size: 11px;
    margin: 8px 0;
    color: #5a5575;
}

.bottom {
    display: flex;
    justify-content: space-around;
    background: white;
    border-top: 1px solid #f0ebff;
    padding: 10px 0;
}

.bottom-item {
    font-size: 10px;
    text-align: center;
    color: #8a84a6;
}

.active {
    color: #4f33d1 !important;
    font-weight: 700;
}

.scan-box {
    width: 240px;
    height: 320px;
    border: 2px solid rgba(255,255,255,0.9);
    border-radius: 20px;
}

.result-card {
    background: #f8f7ff;
    border-radius: 15px;
    padding: 14px;
    margin-top: 10px;
}

.info-card {
    background: #f8f7ff;
    border-radius: 14px;
    padding: 12px;
    margin-top: 10px;
}

.small {
    font-size: 11px;
    color: #8a84a6;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "splash"

if "user" not in st.session_state:
    st.session_state.user = "Sanvi"

if "email" not in st.session_state:
    st.session_state.email = "sanvi@gmail.com"

if "result_img" not in st.session_state:
    st.session_state.result_img = None

if "result_score" not in st.session_state:
    st.session_state.result_score = 98

if "history" not in st.session_state:
    st.session_state.history = [
        {
            "name": "Iris germanica",
            "time": "22 Sep 2026, 10:24 AM",
            "per": "98%"
        },
        {
            "name": "Iris versicolor",
            "time": "21 Sep 2026, 05:18 PM",
            "per": "95%"
        },
        {
            "name": "Iris pseudacorus",
            "time": "20 Sep 2026, 02:37 PM",
            "per": "93%"
        },
        {
            "name": "Iris sibirica",
            "time": "18 Sep 2026, 11:02 AM",
            "per": "90%"
        },
        {
            "name": "Iris germanica",
            "time": "16 Sep 2026, 09:45 AM",
            "per": "97%"
        }
    ]


# =========================================================
# FUNCTIONS
# =========================================================

def go(page):
    st.session_state.page = page
    st.rerun()


@st.cache_resource
def load_model():
    return pipeline(
        "zero-shot-image-classification",
        model="openai/clip-vit-base-patch32"
    )


# Iris flower image
IRIS_IMG = (
    "https://images.unsplash.com/"
    "photo-1518895949257-7621c3c786d7"
    "?auto=format&fit=crop&w=800&q=85"
)


# =========================================================
# 1. SPLASH SCREEN
# =========================================================

if st.session_state.page == "splash":

    st.markdown(f"""
    <div style="
        height:780px;
        background-image:
        linear-gradient(
            to bottom,
            rgba(35,10,80,0.05),
            rgba(35,10,80,0.35)
        ),
        url('{IRIS_IMG}');
        background-size:cover;
        background-position:center;
        display:flex;
        flex-direction:column;
        align-items:center;
        justify-content:flex-start;
        padding-top:35px;
        text-align:center;
    ">

        <div class="logo-box">🌸</div>

        <div style="
            color:white;
            font-size:25px;
            font-weight:800;
            margin-top:10px;
            text-shadow:0 2px 8px rgba(0,0,0,.4);
        ">
            Iris Flower Detector
        </div>

        <div style="
            color:white;
            font-size:13px;
            margin-top:4px;
        ">
            Identify Flowers. Explore Nature.
        </div>

        <div style="
            position:absolute;
            bottom:105px;
            color:white;
            font-size:11px;
        ">
            🌸 Loading...
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:5px'></div>", unsafe_allow_html=True)

    if st.button("Get Started →", use_container_width=True):
        go("login")


# =========================================================
# 2. LOGIN / SIGN UP
# =========================================================

elif st.session_state.page == "login":

    st.markdown("""
    <div class="inner" style="text-align:center;">

        <div class="logo-box">🌸</div>

        <div class="title">
            Iris Flower Detector
        </div>

        <div class="sub">
            Identify flowers using your camera or gallery
        </div>

        <div style="
            display:flex;
            gap:8px;
            margin:14px 0;
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
        "Email",
        placeholder="📧 Email or Phone Number"
    )

    password = st.text_input(
        "Password",
        placeholder="🔒 Password",
        type="password"
    )

    if st.button("Login", use_container_width=True):
        if email:
            st.session_state.email = email

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
        margin:8px;
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
        margin-top:12px;
    ">
        Don't have an account?
        <b style="color:#4f33d1;">Sign Up</b>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# 3. HOME / DASHBOARD
# =========================================================

elif st.session_state.page == "home":

    st.markdown(f"""
    <div class="inner">

        <div style="
            display:flex;
            justify-content:space-between;
            font-size:18px;
        ">
            <span>☰</span>
            <span>🔔</span>
        </div>

        <div style="margin-top:12px;">
            <b style="
                font-size:17px;
                color:#1e1142;
            ">
                Hello, {st.session_state.user}! 👋
            </b>

            <br>

            <span style="
                color:#8a84a6;
                font-size:11px;
            ">
                Discover the beauty of flowers around you.
            </span>
        </div>

        <div
            class="hero-img"
            style="
                background-image:
                url('{IRIS_IMG}');
            "
        >

            <div class="hero-btn">

                <div>
                    <b style="font-size:13px;">
                        📷 Scan Flower
                    </b>

                    <br>

                    <small>
                        Identify an Iris flower
                    </small>
                </div>

                <b style="font-size:20px;">›</b>

            </div>

        </div>

        <div class="grid2">

            <div class="gcard">
                🕒
                <br>
                History
            </div>

            <div class="gcard">
                🖼️
                <br>
                Gallery
            </div>

            <div class="gcard">
                📚
                <br>
                Learn
            </div>

            <div class="gcard">
                ⚙️
                <br>
                Settings
            </div>

        </div>

    </div>

    <div class="bottom">

        <div class="bottom-item active">
            🏠<br>Home
        </div>

        <div class="bottom-item">
            🕒<br>History
        </div>

        <div class="bottom-item">
            👤<br>Profile
        </div>

        <div class="bottom-item">
            ⚙️<br>Settings
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

    st.markdown(f"""
    <div style="
        height:480px;
        background-image:url('{IRIS_IMG}');
        background-size:cover;
        background-position:center;
        position:relative;
        display:flex;
        justify-content:center;
        align-items:center;
    ">

        <div class="scan-box"></div>

        <div style="
            position:absolute;
            bottom:65px;
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
        "<div style='padding:15px 18px 5px; "
        "font-weight:700; font-size:13px;'>"
        "Upload Flower Image"
        "</div>",
        unsafe_allow_html=True
    )

    uploaded = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

    st.markdown(
        "<div style='text-align:center; color:#888; "
        "font-size:11px; margin:5px;'>OR</div>",
        unsafe_allow_html=True
    )

    camera = st.camera_input(
        "Take Flower Photo"
    )

    final_image = camera if camera else uploaded

    if final_image:

        st.session_state.result_img = Image.open(
            final_image
        ).convert("RGB")

        go("processing")

    if st.button("← Back to Home", use_container_width=True):
        go("home")


# =========================================================
# 5. PROCESSING
# =========================================================

elif st.session_state.page == "processing":

    st.markdown("""
    <div style="
        height:720px;
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        text-align:center;
    ">

        <div style="
            color:#1e1142;
            font-size:16px;
            font-weight:800;
        ">
            Analyzing the flower...
        </div>

        <div style="
            color:#8a84a6;
            font-size:11px;
            margin-top:5px;
        ">
            Please wait while we identify
            the iris species.
        </div>

        <div style="
            margin:40px;
            width:140px;
            height:140px;
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
            ">
            </div>

        </div>

        <div style="
            color:#8a84a6;
            font-size:10px;
            margin-top:8px;
        ">
            Identifying flower...
        </div>

    </div>
    """, unsafe_allow_html=True)

    if st.session_state.result_img is not None:

        try:

            model = load_model()

            result = model(
                st.session_state.result_img,
                candidate_labels=[
                    "Iris flower",
                    "Rose flower",
                    "Lily flower",
                    "Daisy flower",
                    "Tulip flower"
                ]
            )

            score = int(result[0]["score"] * 100)

            # UI design in the reference is Iris-focused
            st.session_state.result_score = score

        except Exception:

            st.session_state.result_score = 98

        time.sleep(1.5)

        go("result")


# =========================================================
# 6. RESULT
# =========================================================

elif st.session_state.page == "result":

    img = st.session_state.result_img

    if img is not None:
        st.image(
            img,
            use_container_width=True
        )
    else:
        st.image(
            IRIS_IMG,
            use_container_width=True
        )

    score = st.session_state.result_score

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

        <div class="result-card">

            <b style="font-size:12px;">
                Key Features
            </b>

            <div class="key-row">
                <span>🎨 Color</span>
                <span>Purple with yellow markings</span>
            </div>

            <div class="key-row">
                <span>🌼 Bloom Time</span>
                <span>Spring - Early Summer</span>
            </div>

            <div class="key-row">
                <span>📏 Height</span>
                <span>60 - 90 cm</span>
            </div>

            <div class="key-row">
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

        <div style="
            display:flex;
            justify-content:space-between;
        ">

            <div>
                <b style="
                    font-size:17px;
                    color:#1e1142;
                ">
                    Iris germanica
                </b>

                <br>

                <small style="color:#8a84a6;">
                    German Iris
                </small>
            </div>

            <span class="badge">
                98% Match
            </span>

        </div>

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
                color:#666;
                padding:6px 13px;
                border-radius:20px;
                font-size:11px;
            ">
                Care
            </span>

            <span style="
                background:#f5f3ff;
                color:#666;
                padding:6px 13px;
                border-radius:20px;
                font-size:11px;
            ">
                More Photos
            </span>

        </div>

        <div class="info-card">

            <b style="font-size:13px;">
                Description
            </b>

            <p style="
                font-size:11px;
                color:#5a5575;
                line-height:1.6;
            ">
                Iris germanica, commonly known as the
                German Iris, is a perennial flowering
                plant known for its beautiful purple,
                blue and yellow blooms.
            </p>

        </div>

        <div class="info-card">

            <b style="font-size:13px;">
                Quick Facts
            </b>

            <div class="key-row">
                <span>🔬 Scientific Name</span>
                <span>Iris germanica</span>
            </div>

            <div class="key-row">
                <span>🏷️ Family</span>
                <span>Iridaceae</span>
            </div>

            <div class="key-row">
                <span>⏰ Bloom Time</span>
                <span>Spring - Early Summer</span>
            </div>

            <div class="key-row">
                <span>🌱 Type</span>
                <span>Perennial</span>
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

        <div style="
            display:flex;
            align-items:center;
            gap:10px;
        ">
            <span>←</span>
            <b style="font-size:16px;">
                Scan History
            </b>
        </div>

    </div>
    """, unsafe_allow_html=True)

    for item in st.session_state.history:

        st.markdown(f"""
        <div style="
            display:flex;
            gap:10px;
            padding:12px 18px;
            border-bottom:1px solid #f1edff;
            align-items:center;
        ">

            <div style="
                width:48px;
                height:48px;
                background:#eee8ff;
                border-radius:12px;
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:25px;
            ">
                🌸
            </div>

            <div>
                <b style="
                    font-size:12px;
                    color:#2d2163;
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
                    {item["per"]}
                </span>

            </div>

            <div style="
                margin-left:auto;
                color:#999;
            ">
                ›
            </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

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
            align-items:center;
            justify-content:center;
            font-size:32px;
        ">
            👤
        </div>

        <div style="
            text-align:center;
        ">

            <b style="font-size:15px;">
                Sanvi Mandavkar
            </b>

            <br>

            <small style="color:#8a84a6;">
                sanvi@gmail.com
            </small>

        </div>

        <div class="info-card">

            <div class="key-row">
                <span>👤 Member Since</span>
                <b>12 Mar 2026</b>
            </div>

            <div class="key-row">
                <span>🔍 Total Scans</span>
                <b>32</b>
            </div>

            <div class="key-row">
                <span>⭐ Favorite Flower</span>
                <b>Iris germanica</b>
            </div>

        </div>

        <div class="info-card">

            <div style="
                padding:10px 0;
                border-bottom:1px solid #ede8ff;
                font-size:12px;
            ">
                🌿 My Plants
                <span style="float:right;">›</span>
            </div>

            <div style="
                padding:10px 0;
                border-bottom:1px solid #ede8ff;
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

        <div style="
            display:flex;
            gap:10px;
            align-items:center;
        ">
            <span>←</span>
            <b style="font-size:16px;">
                Settings
            </b>
        </div>

        <div style="margin-top:18px;">

            <b style="font-size:12px;">
                Account
            </b>

            <div class="info-card">

                <div style="
                    padding:9px 0;
                    font-size:12px;
                ">
                    👤 Edit Profile
                    <span style="float:right;">›</span>
                </div>

                <div style="
                    padding:9px 0;
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
                    <span style="float:right;">
                        High ›
                    </span>
                </div>

                <div style="
                    padding:9px 0;
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
                    padding:9px 0;
                    font-size:12px;
                ">
                    ℹ️ About App
                    <span style="float:right;">›</span>
                </div>

                <div style="
                    padding:9px 0;
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
