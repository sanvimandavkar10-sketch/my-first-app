import streamlit as st

st.set_page_config(page_title="Iris Flower Detector", layout="centered")

st.markdown("""
<style>
header, #MainMenu, footer, .stDeployButton, [data-testid="stHeader"] {display:none !important;}
.stApp {background:#f0f0f8 !important;}
.block-container{
    max-width:385px !important;
    padding:0 !important;
    margin:15px auto !important;
    background:white !important;
    border-radius:32px !important;
    border:2.5px solid #111 !important;
    overflow:hidden !important;
    box-shadow:0 12px 30px rgba(0,0,0,0.2) !important;
    height:810px !important;
}
.stButton>button{
    background:#4f33d1 !important; color:white !important; width:100% !important; border-radius:12px !important; height:48px !important; font-weight:700 !important; border:none !important; margin-top:10px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    width:100%; height:810px;
    background: url('https://images.unsplash.com/photo-1591958911259-bee2173bdccc?w=700&q=90');
    background-size:cover;
    background-position:center bottom;
    position:relative;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
">

    <!-- Top White Fade - like your photo -->
    <div style="
        position:absolute; top:0; left:0; right:0; height:58%;
        background: linear-gradient(to bottom, rgba(255,255,255,0.92) 0%, rgba(255,255,255,0.75) 40%, rgba(255,255,255,0.1) 100%);
    "></div>

    <!-- Logo - Purple with Iris Icon SAME AS PHOTO -->
    <div style="position:relative; z-index:2; text-align:center; padding-top:85px;">
        
        <div style="
            width:62px; height:62px;
            background:#5f32d3;
            border-radius:14px;
            margin:0 auto;
            display:flex; align-items:center; justify-content:center;
            box-shadow:0 4px 12px rgba(95,50,211,0.3);
        ">
            <!-- SAME IRIS ICON AS YOUR PHOTO -->
            <svg width="34" height="34" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2.5 C10.5 4.5 9 7 9 9.5 C9 11.2 10 12.5 12 14.5 C14 12.5 15 11.2 15 9.5 C15 7 13.5 4.5 12 2.5 Z" />
                <path d="M7 9 C5.5 10 4 11.5 4 13.5 C4 15 5.5 16.5 7.5 16.5 C8.5 16.5 9.5 16 10.5 15 C9 13 8.5 11 7 9 Z" />
                <path d="M17 9 C15.5 11 14 13 13.5 15 C14.5 16 15.5 16.5 16.5 16.5 C18.5 16.5 20 15 20 13.5 C20 11.5 18.5 10 17 9 Z" />
                <path d="M12 15.5 C11 17 10.2 18.5 10.2 20.5 L13.8 20.5 C13.8 18.5 13 17 12 15.5 Z" />
            </svg>
        </div>

        <div style="font-size:18.5px; font-weight:800; color:#22164d; margin-top:14px; letter-spacing:-0.2px;">Iris Flower Detector</div>
        <div style="font-size:11px; color:#6e6b84; margin-top:4px; font-weight:500;">Identify Flowers. Explore Nature.</div>
    </div>

    <!-- Loading - SAME AS PHOTO -->
    <div style="position:absolute; bottom:28px; left:0; right:0; text-align:center; z-index:2;">
        <div style="width:18px; height:18px; border:1.5px dotted #9a97ad; border-radius:50%; margin:0 auto; display:flex; align-items:center; justify-content:center; font-size:8px; color:#9a97ad;">◍</div>
        <div style="font-size:9.5px; color:#6e6b84; margin-top:6px;">Loading...</div>
    </div>

</div>
""", unsafe_allow_html=True)

# Navigation button - baher
if st.button("Get Started →"):
    st.balloons()
