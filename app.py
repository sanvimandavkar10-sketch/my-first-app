import streamlit as st

st.set_page_config(page_title="Iris Flower Detector", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@600;800&display=swap');
.stApp{background:#f2f3f9 !important;}
header, #MainMenu, footer, .stDeployButton, [data-testid="stHeader"], [data-testid="stToolbar"]{display:none !important;}
.block-container{padding:0 !important; margin:0 auto !important; max-width:395px !important;}
.viewerBadge_container__r5tak{display:none !important;}
</style>
""", unsafe_allow_html=True)

# EXACT SAME SPLASH SCREEN AS YOUR PHOTO
st.markdown("""
<div style="
width:100%;
max-width:385px;
height:810px;
margin:10px auto;
border:3px solid #111;
border-radius:36px;
overflow:hidden;
position:relative;
background-image: url('https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=600&q=90');
background-size: cover;
background-position: center bottom;
font-family:'Inter', sans-serif;
box-shadow: 0 10px 30px rgba(0,0,0,0.2);
background-color: #f7f3ff;
">
    
    <!-- Top Blur Overlay -->
    <div style="
    position:absolute; top:0; left:0; right:0; height:55%;
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    "></div>

    <!-- Status Bar -->
    <div style="position:relative; z-index:2; display:flex; justify-content:space-between; align-items:center; padding:18px 24px 10px 24px; font-size:13px; font-weight:600; color:#000;">
        <span>9:41</span>
        <div style="width:8px; height:8px; background:#111; border-radius:50%;"></div>
        <div style="display:flex; gap:4px; align-items:center; font-size:11px;">📶 📶 🔋</div>
    </div>

    <!-- Logo & Text - Center Top -->
    <div style="position:relative; z-index:3; text-align:center; margin-top:35px;">
        <div style="width:64px; height:64px; background:#5f32d3; border-radius:14px; margin:0 auto; display:flex; align-items:center; justify-content:center;">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2C11 4 9.5 6.5 9.5C9.5 11 10.2 12.2 12 14.5C13.8 12.2 14.5 11 14.5 9.5C14.5 6.5 13 4 12 2Z" opacity="0.95"/>
                <path d="M6.5 9.5C5.5 10.5 4 12 4 14C4 16 6 17.5 8 17.5C9 17.5 10 17 10.8 16C9.5 13.5 8.5 11 6.5 9.5Z" opacity="0.9"/>
                <path d="M17.5 9.5C15.5 11 14.5 13.5 13.2 16C14 17 15 17.5 16 17.5C18 17.5 20 16 20 14C20 12 18.5 10.5 17.5 9.5Z" opacity="0.9"/>
                <path d="M12 15.5C11 16.5 10 18 10 20H14C14 18 13 16.5 12 15.5Z" opacity="0.95"/>
            </svg>
        </div>
        <div style="font-size:19px; font-weight:800; color:#2b1a6b; margin-top:16px; letter-spacing:-0.2px;">Iris Flower Detector</div>
        <div style="font-size:11px; color:#6e6a86; margin-top:5px; font-weight:500;">Identify Flowers. Explore Nature.</div>
    </div>

    <!-- Loading at Bottom -->
    <div style="position:absolute; bottom:32px; left:0; right:0; text-align:center; z-index:3;">
        <div style="display:flex; justify-content:center; gap:3px; margin-bottom:8px;">
            <div style="width:3px; height:3px; background:#8a84a6; border-radius:50%;"></div>
            <div style="width:3px; height:3px; background:#8a84a6; border-radius:50%; opacity:0.6;"></div>
            <div style="width:3px; height:3px; background:#8a84a6; border-radius:50%; opacity:0.3;"></div>
            <div style="width:3px; height:3px; background:#8a84a6; border-radius:50%; opacity:0.6;"></div>
        </div>
        <div style="font-size:10px; color:#5a5675; font-weight:500; letter-spacing:0.2px;">Loading...</div>
    </div>

</div>
""", unsafe_allow_html=True)

# Button to go next
st.markdown("<div style='max-width:385px; margin:0 auto; padding-top:15px;'>", unsafe_allow_html=True)
if st.button("Get Started → Next Screen"):
    st.switch_page("app.py")
st.markdown("</div>", unsafe_allow_html=True)
