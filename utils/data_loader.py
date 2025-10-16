import pandas as pd
import os
import streamlit as st

def load_lona_data():
    """
    Carga el dataset de LonaHistorial.csv desde la carpeta data.
    Convierte la columna 'Date' a datetime y la renombra a 'Fecha'.
    Mantiene Fecha como datetime para filtros, sin formatear a string.
    Maneja distintos tipos de codificación y devuelve un DataFrame.
    """
    csv_path = os.path.join("data", "LonaHistorial.csv")

    try:
        # Intentamos leer con distintos encodings
        try:
            df = pd.read_csv(csv_path, sep=";", encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(csv_path, sep=";", encoding="latin-1")
        
        # Renombramos la columna Date a Fecha
        if "Date" in df.columns:
            df = df.rename(columns={"Date": "Fecha"})
            df["Fecha"] = pd.to_datetime(df["Fecha"], format="%d/%m/%y", errors="coerce")
        else:
            st.warning("No se encontró la columna 'Date' en el CSV. Las fechas no se podrán filtrar.")
        
        return df

    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo en la ruta: {csv_path}")
    except Exception as e:
        raise RuntimeError(f"Ocurrió un error al leer el archivo: {e}")