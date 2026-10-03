import streamlit as st

st.set_page_config(page_title="Iris Flower Detector", layout="centered")
st.markdown("""
<style>
.stApp{background:#eef0ff!important;}
header,#MainMenu,footer{visibility:hidden;}
.block-container{background:white!important; border-radius:32px!important; padding:0!important; max-width:390px!important; box-shadow:0 12px 40px rgba(0,0,0,0.15)!important; overflow:hidden; border:2px solid #111;}
</style>
""", unsafe_allow_html=True)

# SAME TO SAME SPLASH
st.markdown('''
<div style="height:820px; position:relative; background: url('https://images.unsplash.com/photo-1518895949257-7621c3c786d7?w=800&q=85'); background-size:cover; background-position:center; text-align:center;">

<!-- Status Bar -->
<div style="display:flex; justify-content:space-between; padding:14px 22px; color:black; font-size:14px; font-weight:600; background:rgba(255,255,255,0.6); backdrop-filter:blur(5px);">
<span>9:41</span><span>●</span><span>📶 📶 🔋</span>
</div>

<!-- Logo -->
<div style="margin-top:50px;">
<div style="width:78px; height:78px; background:#5b36cc; border-radius:18px; margin:0 auto; display:flex; align-items:center; justify-content:center; font-size:42px; color:white; box-shadow:0 6px 16px rgba(91,54,204,0.4);">🌸</div>
<div style="font-size:22px; font-weight:800; color:#2d2163; margin-top:18px; font-family:Arial;">Iris Flower Detector</div>
<div style="font-size:12px; color:#5a5575; margin-top:4px;">Identify Flowers. Explore Nature.</div>
</div>

<!-- Iris Flower Image Bottom -->
<div style="position:absolute; bottom:0; left:0; right:0; height:65%; background: linear-gradient(to top, rgba(255,255,255,0.1), transparent), url('https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=800&q=80'); background-size:cover; background-position:center bottom; pointer-events:none;"></div>

<!-- Loading -->
<div style="position:absolute; bottom:28px; left:0; right:0;">
<div style="width:22px; height:22px; border:2px dotted #888; border-radius:50%; margin:0 auto; animation:spin 1s linear infinite;"></div>
<div style="font-size:11px; color:#555; margin-top:8px;">Loading...</div>
</div>

</div>
''', unsafe_allow_html=True)

import time
time.sleep(2)
if st.button("Get Started →"):
    st.switch_page("pages/home.py")
