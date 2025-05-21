import streamlit as st
import pandas as pd
import altair as alt

# Configuración inicial de la página
st.set_page_config(page_title="Dashboard LATAM - Mercado del Cacao", layout="wide")
st.title("🌍 Análisis de Mercados y Barreras en América Latina - Industria del Cacao")

# ============================
# DATOS
# ============================

# 1. Barreras de entrada
barreras_data = {
    "País": ["Brasil", "Argentina", "Chile", "Colombia", "Ecuador"],
    "Barrera de Entrada": [
        "Regulaciones Comerciales",
        "Impuestos Altos",
        "Barreras Culturales",
        "Competencia Local",
        "Desafíos Logísticos"
    ],
    "Nivel de Dificultad (1-10)": [7, 6, 5, 8, 6]
}
df_barreras = pd.DataFrame(barreras_data)

# 2. Clientes
clientes_data = {
    "Cliente": ["Chocolate & Co", "Cocoa Kingdom", "Sweet Delights", "Cocoa Trading", "Chocolate World"],
    "País": ["Argentina", "Brasil", "Chile", "Colombia", "Ecuador"],
    "Tamaño de la Empresa": ["Mediana", "Grande", "Pequeña", "Mediana", "Grande"],
    "Demanda Anual (Toneladas)": [150, 300, 50, 100, 250]
}
df_clientes = pd.DataFrame(clientes_data)

# 3. Exportaciones
exportaciones_data = {
    "País": ["Brasil", "Argentina", "Chile", "Colombia", "Ecuador"],
    "Exportaciones (USD millones)": [4000, 1500, 1200, 3000, 2500]
}
df_exportaciones = pd.DataFrame(exportaciones_data)

# 4. Tamaño de Mercado
mercado_data = {
    "País": ["Brasil", "Argentina", "Chile", "Colombia", "Ecuador"],
    "Segmento de Clientes": [
        "Supermercados",
        "Tiendas Especializadas",
        "Comercios Minoristas",
        "Distribuidores",
        "Mayoristas"
    ],
    "Tamaño del Mercado (USD millones)": [5000, 1500, 1200, 3000, 2000]
}
df_mercado = pd.DataFrame(mercado_data)

# ============================
# FILTRO INTERACTIVO
# ============================

paises = df_barreras["País"].unique()
paises_seleccionados = st.sidebar.multiselect("🌎 Selecciona país(es):", options=paises, default=paises)

# ============================
# SECCIÓN 1: Barreras de Entrada
# ============================

st.subheader("🚧 Barreras de Entrada")

df_barreras_filtrado = df_barreras[df_barreras["País"].isin(paises_seleccionados)]

st.dataframe(df_barreras_filtrado, use_container_width=True)

chart_barreras = alt.Chart(df_barreras_filtrado).mark_bar().encode(
    x=alt.X("País:N", sort="-y"),
    y=alt.Y("Nivel de Dificultad (1-10):Q"),
    color="Barrera de Entrada:N",
    tooltip=["País", "Barrera de Entrada", "Nivel de Dificultad (1-10)"]
).properties(width=700, height=400)

st.altair_chart(chart_barreras, use_container_width=True)

# ============================
# SECCIÓN 2: Clientes Potenciales
# ============================

st.subheader("🧑‍💼 Clientes Potenciales")

df_clientes_filtrado = df_clientes[df_clientes["País"].isin(paises_seleccionados)]

st.dataframe(df_clientes_filtrado, use_container_width=True)

chart_clientes = alt.Chart(df_clientes_filtrado).mark_bar().encode(
    x="Cliente:N",
    y="Demanda Anual (Toneladas):Q",
    color="Tamaño de la Empresa:N",
    tooltip=["Cliente", "País", "Demanda Anual (Toneladas)", "Tamaño de la Empresa"]
).properties(width=700, height=400)

st.altair_chart(chart_clientes, use_container_width=True)

# ============================
# SECCIÓN 3: Exportaciones
# ============================

st.subheader("📦 Exportaciones por País")

df_exportaciones_filtrado = df_exportaciones[df_exportaciones["País"].isin(paises_seleccionados)]

chart_export = alt.Chart(df_exportaciones_filtrado).mark_bar().encode(
    x="País:N",
    y="Exportaciones (USD millones):Q",
    color=alt.value("#4CAF50"),
    tooltip=["País", "Exportaciones (USD millones)"]
).properties(width=700, height=400)

st.altair_chart(chart_export, use_container_width=True)

# ============================
# SECCIÓN 4: Tamaño de Mercado
# ============================

st.subheader("📊 Tamaño del Mercado por Segmento")

df_mercado_filtrado = df_mercado[df_mercado["País"].isin(paises_seleccionados)]

st.dataframe(df_mercado_filtrado, use_container_width=True)

chart_mercado = alt.Chart(df_mercado_filtrado).mark_bar().encode(
    x="País:N",
    y="Tamaño del Mercado (USD millones):Q",
    color="Segmento de Clientes:N",
    tooltip=["País", "Segmento de Clientes", "Tamaño del Mercado (USD millones)"]
).properties(width=700, height=400)

st.altair_chart(chart_mercado, use_container_width=True)

# ============================
# FOOTER
# ============================

st.markdown("---")
st.markdown("📈 Dashboard desarrollado con [Streamlit](https://streamlit.io) - © 2025")
