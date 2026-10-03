import streamlit as st
from PIL import Image
from datetime import datetime

st.set_page_config(
    page_title="Iris Flower Detector",
    page_icon="🌸",
    layout="centered"
)

# =========================
# DATA
# =========================

FLOWERS = {
    "Iris germanica": {
        "common": "German Iris",
        "match": 98,
        "color": "Purple with yellow markings",
        "bloom": "Spring – Early Summer",
        "height": "60 – 90 cm",
        "habitat": "Gardens, meadows, wetlands",
        "description": "Iris germanica is a perennial iris known for its beautiful purple flowers with yellow markings.",
        "family": "Iridaceae"
    },
    "Iris versicolor": {
        "common": "Northern Blue Flag",
        "match": 95,
        "color": "Blue-violet",
        "bloom": "Late Spring – Summer",
        "height": "50 – 90 cm",
        "habitat": "Wetlands and marshes",
        "description": "A beautiful blue-violet iris commonly found in moist habitats.",
        "family": "Iridaceae"
    },
    "Iris pseudacorus": {
        "common": "Yellow Iris",
        "match": 93,
        "color": "Bright yellow",
        "bloom": "Late Spring – Summer",
        "height": "80 – 120 cm",
        "habitat": "Wetlands and riverbanks",
        "description": "A tall iris species with bright yellow flowers.",
        "family": "Iridaceae"
    },
    "Iris sibirica": {
        "common": "Siberian Iris",
        "match": 90,
        "color": "Blue-purple",
        "bloom": "Late Spring",
        "height": "60 – 100 cm",
        "habitat": "Meadows and moist soils",
        "description": "A graceful iris with narrow leaves and blue-purple flowers.",
        "family": "Iridaceae"
    }
}

# =========================
# SESSION
# =========================

if "page" not in st.session_state:
    st.session_state.page = "splash"

if "name" not in st.session_state:
    st.session_state.name = "Sanvi"

if "email" not in st.session_state:
    st.session_state.email = "sanvi@gmail.com"

if "flower" not in st.session_state:
    st.session_state.flower = "Iris germanica"

if "history" not in st.session_state:
    st.session_state.history = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "image" not in st.session_state:
    st.session_state.image = None


# =========================
# CSS
# =========================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap'
);

* {
    font-family:Poppins,sans-serif;
}

.stApp {
    background:linear-gradient(
        180deg,
        #ffffff,
        #f8f5ff
    );
}

.block-container {
    max-width:430px;
    padding:20px 16px 90px;
}

.logo {
    width:82px;
    height:82px;
    margin:10px auto 18px;
    border-radius:22px;
    background:linear-gradient(
        135deg,
        #4d22a8,
        #7645d7
    );
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:45px;
    box-shadow:0 8px 25px #5c3ab340;
}

.title {
    text-align:center;
    color:#17134d;
    font-size:27px;
    font-weight:700;
}

.subtitle {
    text-align:center;
    color:#66647a;
    font-size:13px;
}

.card {
    background:white;
    border:1px solid #e8e4f2;
    border-radius:18px;
    padding:15px;
    margin:10px 0;
    box-shadow:0 5px 18px #35206010;
}

.hero {
    background:linear-gradient(
        135deg,
        #ece5ff,
        #ffffff
    );
    border-radius:20px;
    padding:18px;
    margin:18px 0;
}

.badge {
    background:#d8f8e8;
    color:#15804b;
    padding:5px 9px;
    border-radius:8px;
    font-size:12px;
    font-weight:600;
}

.center {
    text-align:center;
}

.small {
    color:#77758a;
    font-size:12px;
}

div.stButton > button {
    border-radius:12px;
    min-height:43px;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)


# =========================
# FUNCTIONS
# =========================

def page(p):
    st.session_state.page = p
    st.rerun()


def detect(img):

    if img is None:
        return "Iris germanica"

    img = img.convert("RGB").resize((60,60))

    pixels = list(img.getdata())

    r = sum(x[0] for x in pixels) / len(pixels)
    g = sum(x[1] for x in pixels) / len(pixels)
    b = sum(x[2] for x in pixels) / len(pixels)

    if r > b * 1.2 and r > g * 1.2:
        return "Iris pseudacorus"

    if b > r * 1.15:
        return "Iris germanica"

    if b > g:
        return "Iris sibirica"

    return "Iris versicolor"


def add_history(name):

    st.session_state.history.insert(
        0,
        {
            "name": name,
            "match": FLOWERS[name]["match"],
            "time": datetime.now().strftime(
                "%d %b %Y, %I:%M %p"
            )
        }
    )


# =========================
# 1 SPLASH
# =========================

if st.session_state.page == "splash":

    st.markdown(
        '<div class="logo">🌸</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Iris Flower Detector</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Identify Flowers. Explore Nature.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="hero"
         style="
         height:360px;
         text-align:center;
         padding-top:45px;
         background:
         linear-gradient(
             135deg,
             #dcd2fa,
             #ffffff
         );
         ">
        <div style="font-size:150px;margin-top:50px;">
            🌸
        </div>
        <div style="
            color:#555;
            margin-top:30px;
            ">
            Loading...
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Start",
        type="primary",
        use_container_width=True
    ):
        page("login")


# =========================
# 2 LOGIN / SIGN UP
# =========================

elif st.session_state.page == "login":

    st.markdown(
        '<div class="logo">🌸</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Iris Flower Detector</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Identify flowers using your camera<br>'
        'or gallery'
        '</div>',
        unsafe_allow_html=True
    )

    login, signup = st.tabs(
        ["Login", "Sign Up"]
    )

    with login:

        email = st.text_input(
            "Email or Phone Number"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button(
            "Login",
            type="primary",
            use_container_width=True
        ):
            st.session_state.email = (
                email or "sanvi@gmail.com"
            )
            page("home")

        st.markdown(
            '<div class="center small">'
            'Forgot Password?'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="center small">'
            'OR'
            '</div>',
            unsafe_allow_html=True
        )

        if st.button(
            "🌈 Continue with Google",
            use_container_width=True
        ):
            page("home")

    with signup:

        name = st.text_input(
            "Full Name"
        )

        email = st.text_input(
            "Email",
            key="signup_email"
        )

        password = st.text_input(
            "Create Password",
            type="password",
            key="signup_password"
        )

        if st.button(
            "Create Account",
            type="primary",
            use_container_width=True
        ):
            st.session_state.name = (
                name or "Sanvi"
            )
            st.session_state.email = (
                email or "sanvi@gmail.com"
            )
            page("home")


# =========================
# 3 HOME
# =========================

elif st.session_state.page == "home":

    st.markdown(
        "<div style='font-size:25px'>☰"
        "<span style='float:right'>🔔</span>"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"## Hello, {st.session_state.name}! 👋"
    )

    st.markdown(
        '<div class="small">'
        'Discover the beauty of flowers around you.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="hero">

        <div style="
        font-size:100px;
        text-align:center;">
        🌸
        </div>

        <div style="
        text-align:center;
        font-size:20px;
        font-weight:700;
        color:#32156f;">
        Scan Flower
        </div>

        <div style="
        text-align:center;
        font-size:12px;
        color:#777;">
        Identify an iris flower
        </div>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "📷  Scan Flower",
        type="primary",
        use_container_width=True
    ):
        page("camera")

    c1, c2 = st.columns(2)

    with c1:
        if st.button(
            "🕘 History",
            use_container_width=True
        ):
            page("history")

    with c2:
        if st.button(
            "🖼️ Gallery",
            use_container_width=True
        ):
            page("camera")

    c3, c4 = st.columns(2)

    with c3:
        if st.button(
            "📖 Learn",
            use_container_width=True
        ):
            page("details")

    with c4:
        if st.button(
            "⚙️ Settings",
            use_container_width=True
        ):
            page("settings")

    st.markdown("""
    <div style="
    position:fixed;
    bottom:0;
    left:50%;
    transform:translateX(-50%);
    width:min(430px,100%);
    background:white;
    border-top:1px solid #e5e1ef;
    padding:10px;
    text-align:center;
    z-index:10;">
    🏠 Home　　🕘 History　　👤 Profile　　⚙️ Settings
    </div>
    """, unsafe_allow_html=True)


# =========================
# 4 CAMERA
# =========================

elif st.session_state.page == "camera":

    if st.button("← Back"):
        page("home")

    st.markdown(
        "### 📷 Scan Iris Flower"
    )

    st.markdown("""
    <div style="
    background:#111;
    color:white;
    border-radius:20px;
    min-height:260px;
    padding:30px;
    text-align:center;
    display:flex;
    align-items:center;
    justify-content:center;
    ">
    <div>
    <div style="font-size:80px">🌸</div>
    <b>Place the iris flower within the frame</b>
    <br>
    <small>Make sure the flower is clear and well lit.</small>
    </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    photo = st.camera_input(
        "Take a photo"
    )

    st.markdown(
        "**OR choose an image from Gallery**"
    )

    upload = st.file_uploader(
        "Upload Flower Image",
        type=["jpg", "jpeg", "png"]
    )

    if photo:

        st.session_state.image = Image.open(
            photo
        )

        page("processing")

    if upload:

        st.session_state.image = Image.open(
            upload
        )

        page("processing")


# =========================
# 5 PROCESSING
# =========================

elif st.session_state.page == "processing":

    st.markdown(
        "<br><br>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="center">

    <div style="
    font-size:22px;
    font-weight:700;
    color:#17134d;">
    Analyzing the flower...
    </div>

    <div class="small"
    style="margin-top:10px;">
    Please wait while we identify<br>
    its iris species.
    </div>

    <div style="
    width:150px;
    height:150px;
    border-radius:50%;
    border:12px solid #ddd8f6;
    border-top-color:#542db8;
    margin:45px auto;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:55px;">
    🌸
    </div>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "View Result",
        type="primary",
        use_container_width=True
    ):

        result = detect(
            st.session_state.image
        )

        st.session_state.flower = result

        add_history(result)

        page("result")


# =========================
# 6 RESULT
# =========================

elif st.session_state.page == "result":

    if st.button("← Back"):
        page("home")

    st.markdown(
        "### Result"
    )

    flower = st.session_state.flower

    data = FLOWERS[flower]

    if st.session_state.image:

        st.image(
            st.session_state.image,
            use_container_width=True
        )

    else:

        st.markdown("""
        <div style="
        height:230px;
        background:#eee8ff;
        border-radius:18px;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size:120px;">
        🌸
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        f"## {flower}"
    )

    st.write(
        f"**{data['common']}**"
    )

    st.markdown(
        f'<span class="badge">'
        f'{data["match"]}% Match'
        f'</span>',
        unsafe_allow_html=True
    )

    st.markdown(
        "### Key Features"
    )

    st.markdown(
        f"""
        <div class="card">

        🎨 <b>Color</b><br>
        {data['color']}

        <br><br>

        🌱 <b>Bloom Time</b><br>
        {data['bloom']}

        <br><br>

        📏 <b>Height</b><br>
        {data['height']}

        <br><br>

        🌿 <b>Habitat</b><br>
        {data['habitat']}

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "View More Details",
        type="primary",
        use_container_width=True
    ):
        page("details")

    if st.button(
        "Scan Another",
        use_container_width=True
    ):

        st.session_state.image = None

        page("camera")


# =========================
# 7 FLOWER DETAILS
# =========================

elif st.session_state.page == "details":

    if st.button("← Back"):
        page("result")

    st.markdown(
        "### Flower Details"
    )

    flower = st.session_state.flower

    data = FLOWERS[flower]

    st.markdown("""
    <div style="
    height:190px;
    background:#e9e2ff;
    border-radius:18px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:100px;">
    🌸
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([5,1])

    with c1:

        st.markdown(
            f"### {flower}"
        )

        st.write(
            data["common"]
        )

    with c2:

        if st.button("♡"):

            if flower in st.session_state.favorites:
                st.session_state.favorites.remove(
                    flower
                )
            else:
                st.session_state.favorites.append(
                    flower
                )

    about, care, photos = st.tabs(
        ["About", "Care", "More Photos"]
    )

    with about:

        st.markdown(
            "#### Description"
        )

        st.write(
            data["description"]
        )

        st.markdown(
            "#### Quick Facts"
        )

        st.write(
            f"**Scientific Name:** {flower}"
        )

        st.write(
            f"**Family:** {data['family']}"
        )

        st.write(
            f"**Bloom Time:** {data['bloom']}"
        )

    with care:

        st.markdown(
            "#### Care"
        )

        st.write(
            "Provide suitable sunlight, "
            "well-drained soil and regular watering."
        )

    with photos:

        st.info(
            "More flower photos can be added here."
        )


# =========================
# 8 HISTORY
# =========================

elif st.session_state.page == "history":

    if st.button("← Back"):
        page("home")

    st.markdown(
        "### Scan History"
    )

    if not st.session_state.history:

        st.info(
            "No scans yet."
        )

    else:

        for i, item in enumerate(
            st.session_state.history
        ):

            with st.container(border=True):

                c1, c2 = st.columns(
                    [1, 4]
                )

                with c1:
                    st.markdown(
                        "<div style='font-size:45px'>🌸</div>",
                        unsafe_allow_html=True
                    )

                with c2:

                    st.markdown(
                        f"**{item['name']}**"
                    )

                    st.caption(
                        item["time"]
                    )

                    st.markdown(
                        f'<span class="badge">'
                        f'{item["match"]}%'
                        f'</span>',
                        unsafe_allow_html=True
                    )

                    if st.button(
                        "Open",
                        key=f"history_{i}"
                    ):

                        st.session_state.flower = (
                            item["name"]
                        )

                        page("details")


# =========================
# 9 PROFILE
# =========================

elif st.session_state.page == "profile":

    if st.button("← Back"):
        page("home")

    st.markdown(
        "### Profile"
    )

    st.markdown(
        "<div style='text-align:center;"
        "font-size:75px'>👤</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='center'><b>"
        f"{st.session_state.name}"
        f"</b></div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='center small'>"
        f"{st.session_state.email}"
        f"</div>",
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Scans",
            len(st.session_state.history)
        )

    with c2:
        st.metric(
            "Favorites",
            len(st.session_state.favorites)
        )

    with c3:
        st.metric(
            "Year",
            "2026"
        )

    st.markdown(
        "### Saved Flowers"
    )

    if st.session_state.favorites:

        for f in st.session_state.favorites:
            st.write("🌸", f)

    else:

        st.info(
            "No favorite flowers yet."
        )


# =========================
# 10 SETTINGS
# =========================

elif st.session_state.page == "settings":

    if st.button("← Back"):
        page("home")

    st.markdown(
        "### Settings"
    )

    st.markdown(
        "#### Account"
    )

    new_name = st.text_input(
        "Edit Profile",
        value=st.session_state.name
    )

    if st.button(
        "Save Profile",
        use_container_width=True
    ):

        st.session_state.name = new_name

        st.success(
            "Profile updated"
        )

    if st.button(
        "🔒 Change Password",
        use_container_width=True
    ):

        st.info(
            "Password change feature is available "
            "in the full backend version."
        )

    st.markdown(
        "#### App Preferences"
    )

    st.toggle(
        "🔔 Notifications",
        value=True
    )

    st.selectbox(
        "📷 Camera Quality",
        ["High", "Medium", "Low"]
    )

    st.selectbox(
        "🌐 Language",
        ["English", "Marathi"]
    )

    st.markdown(
        "#### About"
    )

    if st.button(
        "ⓘ About App",
        use_container_width=True
    ):

        st.info(
            "Iris Flower Detector\n\n"
            "Identify and explore iris flowers."
        )

    if st.button(
        "🔐 Privacy Policy",
        use_container_width=True
    ):

        st.info(
            "This demo stores data only during "
            "the current Streamlit session."
        )

    if st.button(
        "🚪 Log Out",
        use_container_width=True
    ):

        st.session_state.page = "login"

        st.rerun()
