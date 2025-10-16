import streamlit as st
import plotly.graph_objects as go

def show_lona_charts_go(df):
    if df.empty:
        st.warning("No hay datos para mostrar en el rango seleccionado.")
        return

    st.subheader("Visualización de Salidas de Lona")

    rollos_data = df.groupby("Codigo")["Rollos"].sum().sort_values()
    metros_data = df.groupby("Codigo")["Metros"].sum().sort_values()

    # Gráfico Rollos
    fig1 = go.Figure(go.Bar(
        x=rollos_data.values,
        y=rollos_data.index,
        orientation='h',
        text=rollos_data.values,
        textposition='outside'
    ))
    fig1.update_layout(
        title="Rollos totales por tipo de lona",
        xaxis_title="Cantidad de Rollos",
        yaxis_title="Código",
        height=max(400, len(rollos_data)*35),
        margin=dict(l=150, r=50, t=80, b=50)
    )
    st.plotly_chart(fig1, use_container_width=True)

    # Gráfico Metros
    fig2 = go.Figure(go.Bar(
        x=metros_data.values,
        y=metros_data.index,
        orientation='h',
        text=metros_data.values,
        textposition='outside',
        marker_color='orange'
    ))
    fig2.update_layout(
        title="Metros totales por tipo de lona",
        xaxis_title="Metros Totales",
        yaxis_title="Código",
        height=max(400, len(metros_data)*35),
        margin=dict(l=150, r=50, t=80, b=50)
    )
    st.plotly_chart(fig2, use_container_width=True)