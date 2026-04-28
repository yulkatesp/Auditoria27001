import streamlit as st
from pathlib import Path

# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Auditoría ISO 27001",
    page_icon="🫆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Ocultar elementos por defecto de Streamlit ──────────────────────────────
hide_streamlit_style = """
<style>
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    .stAppDeployButton { display: none; }
    /* Quitar padding por defecto de Streamlit */
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    [data-testid="stAppViewContainer"] {
        background: #F5F3F0;
    }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ── Cargar el HTML del portafolio ────────────────────────────────────────────
html_file = Path(__file__).parent / "templates/menu.html"

# Lee solo el contenido del <body> para embeber en Streamlit
with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

# ── Renderizar el HTML ────────────────────────────────────────────────────────
# Usamos st.components para embeber HTML con alto personalizado
import streamlit.components.v1 as components

components.html(
    html_content,
    height=730,          # Ajusta según la altura de tu diseño
    scrolling=False,
)