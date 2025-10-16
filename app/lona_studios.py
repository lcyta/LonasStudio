import streamlit as st
from utils.data_loader import load_lona_data
from utils.visualizations import show_lona_charts_go
from utils.daily_charts import show_lona_daily_chart
import pandas as pd


def show_lona_page():
    st.title("Salidas de Lona")

    try:
        df = load_lona_data()

        with st.expander("Ver detalles de las salidas de lona", expanded=False):
            st.dataframe(df, width="stretch")
            #st.dataframe(df.assign(Fecha=df["Fecha"].dt.strftime("%Y-%m-%d")), width="stretch", height=500)

        with st.expander("Ver gráficos de las salidas de lona", expanded=False):
            if "Fecha" in df.columns:
                # Selector de fechas dentro del expander
                min_date = df["Fecha"].min()
                max_date = df["Fecha"].max()
                start_date = st.date_input("Fecha inicio", min_date, key="start_date")
                end_date = st.date_input("Fecha fin", max_date, key="end_date")

                # Filtramos el dataframe según fechas
                mask = (df["Fecha"] >= pd.to_datetime(start_date)) & (df["Fecha"] <= pd.to_datetime(end_date))
                df_filtered = df[mask]
            else:
                df_filtered = df
                st.warning("No se encontró la columna 'Fecha' en el dataset.")

            # Mostramos los gráficos con el df filtrado
            show_lona_charts_go(df_filtered)

        with st.expander("Ver gráficos de las salidas de lona Diaria", expanded=False):
            if "Fecha" in df.columns:
                min_date = df["Fecha"].min()
                max_date = df["Fecha"].max()
                start_date = st.date_input("Fecha inicio", min_date, key="start_date_daily")
                end_date = st.date_input("Fecha fin", max_date, key="end_date_daily")

                df_filtered = df[(df["Fecha"] >= pd.to_datetime(start_date)) & (df["Fecha"] <= pd.to_datetime(end_date))]
            else:
                df_filtered = df
                st.warning("No se encontró la columna 'Fecha' en el dataset.")

            show_lona_daily_chart(df_filtered)

        with st.expander("Ver gráficos Salida de Lona Mensual", expanded=False):
            if "Fecha" in df.columns:
                min_date = df["Fecha"].min()
                max_date = df["Fecha"].max()
                start_date = st.date_input("Fecha inicio", min_date, key="start_date_daily")
                end_date = st.date_input("Fecha fin", max_date, key="end_date_daily")

                df_filtered = df[(df["Fecha"] >= pd.to_datetime(start_date)) & (df["Fecha"] <= pd.to_datetime(end_date))]
            else:
                df_filtered = df
                st.warning("No se encontró la columna 'Fecha' en el dataset.")

            show_lona_daily_chart(df_filtered)


    except FileNotFoundError as e:
        st.error(str(e))
    except Exception as e:
        st.error(f"Ocurrió un error: {e}")