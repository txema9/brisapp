import base64

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title="BRISA",
    page_icon="brisa_icon.png",
    layout="wide"
)

# 1. leer HTML
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 2. favicon/logo
with open("titulo.png", "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode()

logo_src = f"data:image/png;base64,{logo_b64}"

# 3. reemplazo
html = html.replace("LOGO_SRC", logo_src)

# 4. render
components.html(
    html,
    height=900,
    scrolling=False)