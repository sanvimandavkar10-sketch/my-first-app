import streamlit as st
from PIL import Image
from transformers import pipeline
import time
st.set_page_config(page_title='Iris Flower Detector', layout='centered')
st.markdown('''<style>
.stApp{background:#e9e6ff!important;} header,#MainMenu,footer{visibility:hidden;}
.block-container{background:white!important; border-radius:28px!important; padding:0!important; max-width:390px!important; box-shadow:0 12px 40px rgba(80,40,180,0.18)!important; overflow:hidden;}
.inner{padding:18px;}.logo-box{width:62px; height:62px; background:#4f33d1; border-radius:16px; display:flex; align-items:center; justify-content:center; font-size:32px; margin:0 auto; color:white;}
.stButton>button{background:#4f33d1!important; color:white!important; border-radius:12px!important; width:100%!important; height:46px!important; font-weight:700!important; border:none!important;}
.badge{background:#d1fae5; color:#065f46; font-size:10px; font-weight:700; padding:3px 8px; border-radius:20px;}
</style>''', unsafe_allow_html=True)
if 'page' not in st.session_state:
    st.session_state.page='splash'; st.session_state.user='Sanvi'; st.session_state.result_img=None; st.session_state.score=98
def go(p): st.session_state.page=p; st.rerun()
@st.cache_resource
def load_model(): return pipeline('zero-shot-image-classification', model='openai/clip-vit-base-patch32')
model=load_model()
IRIS='https://images.unsplash.com/photo-1518895949257-7621c3c786d7?w=600'
if st.session_state.page=='splash':
    st.markdown(f'<div style="height:680px; background: linear-gradient(to bottom, rgba(0,0,0,0.1), rgba(0,0,0,0.3)), url({IRIS}); background-size:cover; background-position:center; text-align:center; padding-top:40px;"><div class="logo-box">🌸</div><div style="color:white; font-size:24px; font-weight:800; margin-top:10px;">Iris Flower Detector</div><div style="color:white; font-size:12px;">Identify Flowers. Explore Nature.</div><div style="color:white; font-size:11px; margin-top:420px;">Loading...</div></div>', unsafe_allow_html=True)
    if st.button('Get Started →'): go('login')
elif st.session_state.page=='login':
    st.markdown('<div class="inner" style="text-align:center;"><div class="logo-box">🌸</div><div style="color:#1e1142; font-weight:800; font-size:20px; margin-top:8px;">Iris Flower Detector</div><div style="color:#8a84a6; font-size:11px;">Identify flowers using your camera or gallery</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="inner">', unsafe_allow_html=True)
    st.text_input('', placeholder='Email or Phone Number'); st.text_input('', placeholder='Password', type='password')
    if st.button('Login'): go('home')
    st.markdown('<div style="text-align:center; font-size:11px; color:#4f33d1; margin:6px;">Forgot Password? <br>OR</div>', unsafe_allow_html=True)
    if st.button('Continue with Google'): go('home')
    st.markdown('</div>', unsafe_allow_html=True)
elif st.session_state.page=='home':
    st.markdown(f'<div class="inner"><b>Hello, Sanvi! 👋</b><br><small style="color:#8a84a6; font-size:11px;">Discover the beauty of flowers around you.</small><div style="height:165px; border-radius:18px; margin:12px 0; background:url({IRIS}); background-size:cover; position:relative;"><div style="position:absolute; bottom:10px; left:10px; right:10px; background:#4f33d1; border-radius:12px; padding:10px; color:white; display:flex; justify-content:space-between;"><div><b>📷 Scan Flower</b><br><small style="font-size:10px;">Identify an Iris flower</small></div><div>›</div></div></div><div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;"><div style="background:#f7f5ff; border-radius:12px; padding:14px; text-align:center; font-size:12px;">🕒<br>History</div><div style="background:#f7f5ff; border-radius:12px; padding:14px; text-align:center; font-size:12px;">🖼️<br>Gallery</div><div style="background:#f7f5ff; border-radius:12px; padding:14px; text-align:center; font-size:12px;">📚<br>Learn</div><div style="background:#f7f5ff; border-radius:12px; padding:14px; text-align:center; font-size:12px;">⚙️<br>Settings</div></div></div>', unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        if st.button('History'): go('history')
        if st.button('Profile'): go('profile')
    with c2:
        if st.button('Scan Now'): go('camera')
        if st.button('Settings'): go('settings')
elif st.session_state.page=='camera':
    st.markdown('<div class="inner"><b>← Scan Iris Flower</b></div>', unsafe_allow_html=True)
    file=st.file_uploader('Upload', type=['jpg','png','jpeg']); cam=st.camera_input('Take photo')
    final=cam if cam else file
    if final: st.session_state.result_img=Image.open(final).convert('RGB'); go('processing')
    if st.button('Back'): go('home')
elif st.session_state.page=='processing':
    st.markdown('<div style="text-align:center; padding-top:100px;"><b>Analyzing the flower...</b><br><small style="color:gray;">Please wait</small><div style="margin:30px auto; width:120px; height:120px; border:3px solid #eee; border-top:3px solid #4f33d1; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:40px;">🌸</div></div>', unsafe_allow_html=True)
    if st.session_state.result_img is not None:
        try: r=model(st.session_state.result_img, candidate_labels=['iris flower','rose','lily'])[0]; st.session_state.score=int(r['score']*100)
        except: st.session_state.score=98
        time.sleep(1.2); go('result')
elif st.session_state.page=='result':
    if st.session_state.result_img is not None: st.image(st.session_state.result_img, use_container_width=True)
    st.markdown(f'<div class="inner"><div style="display:flex; justify-content:space-between;"><b>Iris germanica</b><span class="badge">{st.session_state.score}% Match</span></div><small style="color:gray;">German Iris</small><div style="background:#f8f7ff; border-radius:12px; padding:12px; margin-top:10px; font-size:11px;">🎨 Purple with yellow<br>🌼 Spring - Early Summer<br>📏 60-90 cm</div></div>', unsafe_allow_html=True)
    if st.button('View More Details'): go('details')
    if st.button('Scan Another'): go('camera')
    if st.button('Home'): go('home')
elif st.session_state.page=='details':
    if st.session_state.result_img is not None: st.image(st.session_state.result_img, use_container_width=True)
    st.markdown('<div class="inner"><b>Iris germanica</b> <span class="badge">98% Match</span><br><small style="color:gray;">German Iris</small><div style="background:#f8f7ff; border-radius:12px; padding:12px; margin-top:10px; font-size:11px;">German Iris is a perennial with striking purple blooms.</div></div>', unsafe_allow_html=True)
    if st.button('Back to Result'): go('result')
elif st.session_state.page=='history':
    st.markdown('<div class="inner"><b>← Scan History</b><br><br>🌸 Iris germanica - 98% - 22 Sep 2026<br><br>🌸 Iris versicolor - 95% - 21 Sep 2026<br><br>🌸 Iris pseudacorus - 93% - 20 Sep 2026</div>', unsafe_allow_html=True)
    if st.button('Home'): go('home')
elif st.session_state.page=='profile':
    st.markdown('<div class="inner" style="text-align:center;"><b>Profile</b><div style="width:60px; height:60px; background:#ede9fe; border-radius:50%; margin:20px auto; display:flex; align-items:center; justify-content:center; font-size:30px;">👤</div><b>Sanvi Mandavkar</b><br><small style="color:gray;">sanvi@gmail.com</small><div style="text-align:left; background:#f8f7ff; border-radius:12px; padding:12px; margin-top:15px; font-size:12px;">Member Since: 12 Mar 2026<br>Total Scans: 32<br>Favorite: Iris germanica</div></div>', unsafe_allow_html=True)
    if st.button('Home'): go('home')
else:
    st.markdown('<div class="inner"><b>Settings</b><div style="background:#f8f7ff; border-radius:12px; padding:12px; margin-top:12px; font-size:12px;">👤 Edit Profile ›<br><br>🔒 Change Password ›<br><br>🔔 Notifications ›</div><div style="text-align:center; color:red; margin-top:15px; background:#fff1f2; padding:10px; border-radius:12px;">Log Out</div></div>', unsafe_allow_html=True)
    if st.button('Home'): go('home')
    if st.button('Logout'): go('splash')
