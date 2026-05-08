import base64

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# 1. Un solo set_page_config con el favicon correcto
st.set_page_config(
    page_title="BRISA",
    page_icon=Image.open("brisa_icon.png"),
    layout="wide"
)

# 2. Modo de apertura "rb", no el nombre del archivo
with open("titulo.png", "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode()

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

logo_src = f"data:image/png;base64,{logo_b64}"

html = html.replace("LOGO_SRC", logo_src)

st.components.v1.iframe(
    html,
    height=900,
    scrolling=False
)