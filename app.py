st.markdown("""
<style>
/* 1. Background - Exact like demo */
.stApp {
    background: #c7d2fe;
    background-image: 
        radial-gradient(at 20% 30%, #a5b4fc 0px, transparent 50%),
        radial-gradient(at 80% 20%, #818cf8 0px, transparent 50%),
        radial-gradient(at 40% 80%, #c084fc 0px, transparent 50%),
        radial-gradient(at 90% 90%, #60a5fa 0px, transparent 50%),
        linear-gradient(135deg, #ddd6fe 0%, #a5b4fc 100%);
    background-attachment: fixed;
}
header, #MainMenu, footer {visibility: hidden;}

/* 2. Glass Card - 100% same as demo image */
.glass-box, .glass-card {
    background: rgba(255, 255, 255, 0.72) !important;
    backdrop-filter: blur(25px) saturate(180%) !important;
    -webkit-backdrop-filter: blur(25px) saturate(180%) !important;
    border-radius: 28px !important;
    border: 1.5px solid rgba(255, 255, 255, 0.6) !important;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15) !important;
    padding: 30px !important;
}

/* Text color like demo - dark purple */
.glass-box h1, .glass-card h1 {
    color: #4c1d95 !important;
    font-weight: 800 !important;
    text-align: center;
}
.glass-box p, .glass-card p, label {
    color: #4b5563 !important;
    text-align: center;
}

/* Button style */
.stButton > button {
    background: linear-gradient(90deg, #8b8cf8 0%, #6d28d9 100%) !important;
    color: white !important;
    border-radius: 12px !important;
    border: none !important;
    width: 100% !important;
    font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)
