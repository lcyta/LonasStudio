import streamlit as st

def show_sidebar():
    st.sidebar.title("Menú Principal")

    # Solo una opción disponible
    option = st.sidebar.radio("Selecciona una opción:", ["Lona Studios"])

    return option