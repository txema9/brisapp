import base64

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="BRISA",
    page_icon="brisa_icon.png",
    layout="wide"
)


BASE_DIR = (
    Path(__file__)
    .resolve()
    .parent
)


# =========================
# HTML
# =========================

html_path = (
    BASE_DIR
    / "frontend"
    / "index.html"
)

with open(
    html_path,
    "r",
    encoding="utf-8"
) as f:

    html = f.read()


# =========================
# LOGO
# =========================

logo_path = (
    BASE_DIR
    / "frontend"
    / "assets"
    / "titulo.png"
)

with open(
    logo_path,
    "rb"
) as f:

    logo_b64 = base64.b64encode(
        f.read()
    ).decode()


logo_src = (
    f"data:image/png;base64,{logo_b64}"
)


# =========================
# BACKGROUND
# =========================

background_path = (
    BASE_DIR
    / "frontend"
    / "assets"
    / "santander.png"
)

with open(
    background_path,
    "rb"
) as f:

    bg_b64 = base64.b64encode(
        f.read()
    ).decode()


bg_src = (
    f"data:image/png;base64,{bg_b64}"
)


# =========================
# REPLACE
# =========================

html = html.replace(
    "LOGO_SRC",
    logo_src
)

html = html.replace(
    "BACKGROUND_SRC",
    bg_src
)


# =========================
# RENDER
# =========================

components.html(
    html,
    height=900,
    scrolling=False
)