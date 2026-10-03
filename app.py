import streamlit as st
import time

st.set_page_config(
    page_title="Iris Flower",
    page_icon="🌸",
    layout="centered"
)

# Splash Screen
st.markdown(
    """
    <style>
    .splash {
        text-align: center;
        padding-top: 180px;
    }

    .flower {
        font-size: 90px;
    }

    .title {
        font-size: 38px;
        font-weight: bold;
        margin-top: 15px;
    }

    .subtitle {
        font-size: 18px;
        margin-top: 10px;
    }
    </style>

    <div class="splash">
        <div class="flower">🌸</div>
        <div class="title">Iris Flower</div>
        <div class="subtitle">Classification App</div>
    </div>
    """,
    unsafe_allow_html=True
)

time.sleep(2)

st.switch_page("pages/login.py")
