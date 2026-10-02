import streamlit as st

st.title("Maza Pahila App")
st.write("Hello Sanvi! Ha app live aahe.")

name = st.text_input("Tujha naav lih:")
if name:
    st.success(f"Welcome {name}!")
    st.balloons()
