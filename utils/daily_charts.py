import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show_lona_daily_chart(df):
    """
    Muestra un gráfico de línea con las salidas diarias de metros de lona,
    filtrable por fecha, tipo de lona y tipo de movimiento.
    """
    if df.empty:
        st.warning("No hay datos para mostrar.")
        return

    # --- Selector de tipo de lona ---
    tipos_lona = df["Codigo"].unique().tolist()
    selected_lona = st.selectbox("Selecciona el tipo de lona", tipos_lona)

    # --- Selector de tipo de movimiento ---
    tipos_movimiento = df["Para"].unique().tolist()
    selected_mov = st.selectbox("Selecciona el tipo de movimiento", tipos_movimiento)

    # --- Filtrar dataframe ---
    df_filtered = df[(df["Codigo"] == selected_lona) & (df["Para"] == selected_mov)]

    # --- Agrupar por fecha ---
    daily_data = df_filtered.groupby("Fecha").agg({"Metros": "sum"}).reset_index()

    if daily_data.empty:
        st.warning("No hay datos para los filtros seleccionados.")
        return

    # --- Gráfico de línea ---
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=daily_data["Fecha"],
        y=daily_data["Metros"],
        mode="lines+markers",
        name="Metros diarios",
        hovertemplate="<b>Fecha:</b> %{x}<br><b>Metros:</b> %{y}<extra></extra>"
    ))

    fig.update_layout(
        title=f"Metros diarios de lona: {selected_lona} ({selected_mov})",
        xaxis_title="Fecha",
        yaxis_title="Metros",
        margin=dict(l=80, r=50, t=80, b=50),
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)