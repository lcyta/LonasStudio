import streamlit as st
from app.sidebar import show_sidebar
from app.lona_studios import show_lona_page

# Configuración general de la página
st.set_page_config(
    page_title="Lona Studios",
    page_icon="🎨",
    layout="wide"
)

def main():
    selected = show_sidebar()

    if selected == "Lona Studios":
        show_lona_page()

if __name__ == "__main__":
    main()