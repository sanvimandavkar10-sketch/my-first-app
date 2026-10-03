import streamlit as st

st.set_page_config(page_title="Iris Flower Detector", layout="centered")

# Hide top menu
st.markdown("<style>header,footer,#MainMenu{display:none !important;}</style>", unsafe_allow_html=True)

st.write("")
st.write("")
st.image("https://iili.io/F5WvW7S.png", width=80)
st.markdown("### Iris Flower Detector")
st.caption("Identify Flowers. Explore Nature.")

st.write("")
st.image("https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=800&q=80", use_container_width=True)

st.write("")
st.caption("Loading...")
