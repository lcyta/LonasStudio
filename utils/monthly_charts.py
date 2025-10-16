import streamlit as st
import pandas as pd
import plotly.express as px

def show_lona_monthly_chart(df):
    """
    Muestra un gráfico mensual de consumo de metros por tipo de movimiento (solo Para Fabrica y Para Venta).
    """
    st.subheader("Consumo Mensual de Lona (metros)")

    if "Para" not in df.columns or "Metros" not in df.columns or "Fecha" not in df.columns:
        st.warning("El dataset no tiene las columnas necesarias ('Fecha', 'Para', 'Metros').")
        return

    # Filtramos solo los movimientos de salida
    df_filtered = df[df["Para"].isin(["Para Fabrica", "Para Venta"])].copy()

    # Creamos columna Año-Mes para agrupar
    df_filtered["Mes"] = df_filtered["Fecha"].dt.to_period("M").astype(str)

    # Agrupamos por Mes y Código (tipo de lona)
    monthly_data = df_filtered.groupby(["Mes", "Codigo"], as_index=False)["Metros"].sum()

    # Gráfico de línea
    fig = px.line(
        monthly_data,
        x="Mes",
        y="Metros",
        color="Codigo",
        markers=True,
        title="Consumo Mensual de Lona (metros)"
    )

    fig.update_layout(
        xaxis_title="Mes",
        yaxis_title="Metros",
        hovermode="x unified",
        height=500,
        margin=dict(l=50, r=50, t=50, b=50)
    )

    st.plotly_chart(fig, use_container_width=True)