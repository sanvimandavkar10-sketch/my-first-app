import streamlit as st

st.set_page_config(page_title="Iris Flower Detector", layout="centered")

# Hide Streamlit menu
st.markdown("""
<style>
header, footer, #MainMenu, .stDeployButton {display:none !important;}
</style>
""", unsafe_allow_html=True)

# ----- SAME TO SAME SPLASH - NO HTML CODE -----

# 1. Logo
st.write("")
st.write("")
col1, col2, col3 = st.columns([1,1,1])
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/11742/11742615.png", width=75)

# 2. Title - same as your photo
st.markdown("<h3 style='text-align:center; color:#22164d; margin-bottom:2px;'>Iris Flower Detector</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray; font-size:12px; margin-top:0px;'>Identify Flowers. Explore Nature.</p>", unsafe_allow_html=True)

st.write("")

# 3. Main Iris Flower Image - SAME AS YOUR PHOTO
st.image("https://images.unsplash.com/photo-1591958911259-bee2173bdccc?w=700&q=90", use_container_width=True)

# 4. Loading
st.write("")
st.markdown("<p style='text-align:center; color:gray; font-size:11px;'>Loading...</p>", unsafe_allow_html=True)

st.write("")
if st.button("Get Started →", use_container_width=True):
    st.balloons()
    st.success("Splash ready! Ata next screen deu?")
