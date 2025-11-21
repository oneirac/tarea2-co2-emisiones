import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from datetime import datetime

# Configuración de página
st.set_page_config(
    page_title="Emisiones de CO₂ Global",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar datos
@st.cache_data
def cargar_datos():
    url = "https://raw.githubusercontent.com/owid/co2-data/refs/heads/master/owid-co2-data.csv"
    df = pd.read_csv(url)
    return df

try:
    df = cargar_datos()
except:
    st.error("No se pudo cargar el dataset. Verifica tu conexión a internet.")
    st.stop()

# Título principal
st.markdown("""
# 🌎 Emisiones de CO₂ Global
**Aplicación interactiva para explorar emisiones de CO₂ a nivel mundial**
""")

# Sidebar con controles
st.sidebar.title("📊 Controles")

# Filtros
año_min = int(df['year'].min())
año_max = int(df['year'].max())
año = st.sidebar.slider("Año", año_min, año_max, año_max)

# Filtrar países válidos (excluir agregaciones globales)
paises_validos = df[(df['year'] == año) & (df['iso_code'].str.len() == 3) & (df['co2'].notna())]['country'].unique()
pais_seleccionado = st.sidebar.selectbox("Selecciona un país", sorted(paises_validos))

# Tipo de métrica
metrica = st.sidebar.radio("Métrica", ["CO₂ Total", "CO₂ per Cápita"])

# Datos para el año seleccionado
datos_año = df[df['year'] == año].copy()
datos_pais = df[df['country'] == pais_seleccionado].copy().sort_values('year')

# PESTAÑA 1: Mapa y Visualización Principal
tab1, tab2, tab3, tab4 = st.tabs(["🗺 Mapa Global", "📊 Top Emisores", "📏 Tendencias", "📝 Información"])

with tab1:
    st.subheader(f"Emisiones de CO₂ en {año}")
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Preparar datos para el mapa
        datos_mapa = datos_año[datos_año['iso_code'].str.len() == 3].copy()
        
        # Seleccionar métrica
        if metrica == "CO₂ per Cápita":
            columna = 'co2_per_capita'
            titulo_mapa = f"CO₂ per Cápita ({año})"
        else:
            columna = 'co2'
            titulo_mapa = f"Emisión Total de CO₂ ({año})"
        
        # Crear mapa interactivo
        fig_mapa = px.choropleth(
            datos_mapa,
            locations="iso_code",
            color=columna,
            hover_name="country",
            hover_data={columna: ":.2f", "iso_code": False},
            color_continuous_scale="OrRd",
            labels={columna: "CO₂ (Mt)" if columna == 'co2' else "CO₂ per cápita (t)"},
            title=titulo_mapa
        )
        fig_mapa.update_layout(height=500)
        st.plotly_chart(fig_mapa, use_container_width=True)
    
    with col2:
        st.metric("Año Seleccionado", año)
        st.metric("País Seleccionado", pais_seleccionado)
        
        # Estadísticas rápidas
        total_co2 = datos_año[datos_año['iso_code'].str.len() == 3]['co2'].sum()
        st.metric("Total CO₂ Global (Mt)", f"{total_co2:.2f}")

with tab2:
    st.subheader(f"Top 15 Emisores de CO₂ en {año}")
    
    # Top emisores
    top_emisores = datos_año[datos_año['iso_code'].str.len() == 3].nlargest(15, 'co2')[['country', 'co2', 'population']].copy()
    top_emisores = top_emisores.dropna(subset=['co2'])
    
    if not top_emisores.empty:
        fig_top = px.bar(
            top_emisores,
            y='country',
            x='co2',
            orientation='h',
            title=f"Top 15 Países Emisores ({año})",
            labels={'co2': 'Emisión (Mt)', 'country': 'País'},
            color='co2',
            color_continuous_scale='Reds'
        )
        fig_top.update_layout(height=600, showlegend=False)
        st.plotly_chart(fig_top, use_container_width=True)
    else:
        st.warning("No hay datos disponibles para este año.")

with tab3:
    st.subheader(f"Tendencia de Emisiones: {pais_seleccionado}")
    
    if not datos_pais.empty and datos_pais['co2'].notna().any():
        fig_tendencia = px.line(
            datos_pais,
            x='year',
            y='co2',
            title=f"Evolución de Emisiones CO₂ - {pais_seleccionado}",
            labels={'co2': 'Emisión (Mt)', 'year': 'Año'},
            markers=True
        )
        fig_tendencia.update_layout(height=500)
        st.plotly_chart(fig_tendencia, use_container_width=True)
        
        # Estadísticas del país
        col1, col2, col3 = st.columns(3)
        with col1:
            emision_actual = datos_pais[datos_pais['year'] == año]['co2'].values
            if len(emision_actual) > 0:
                st.metric("Emisión Actual (Mt)", f"{emision_actual[0]:.2f}")
        with col2:
            emision_1990 = datos_pais[datos_pais['year'] == 1990]['co2'].values
            if len(emision_1990) > 0:
                cambio = ((emision_actual[0] - emision_1990[0]) / emision_1990[0] * 100) if len(emision_actual) > 0 else 0
                st.metric("Cambio desde 1990 (%)", f"{cambio:.2f}%")
        with col3:
            emision_max = datos_pais['co2'].max()
            año_max = datos_pais[datos_pais['co2'] == emision_max]['year'].values[0]
            st.metric("Pico Máximo (Mt)", f"{emision_max:.2f} ({int(año_max)})")
    else:
        st.warning(f"No hay datos disponibles para {pais_seleccionado}.")

with tab4:
    st.subheader("Sobre esta Aplicación")
    
    st.markdown("""
    ### Fuente de Datos
    - **Our World in Data (OWID)**: Base de datos completa de emisiones de CO₂ a nivel mundial
    - **Repositorio**: https://github.com/owid/co2-data
    - **Última actualización**: Datos hasta 2023
    
    ### Métricas Explicadas
    - **CO₂ Total**: Emisión anual total en millones de toneladas (Mt)
    - **CO₂ per Cápita**: Emisión promedio por habitante en toneladas (t)
    
    ### Decisiones de Diseño
    1. **Paleta de Colores**: Se utilizó la escala "OrRd" para el mapa ya que representa intuitivamente
       el aumento de concentración de CO₂ (rojo indica mayor emisión)
    2. **Exclusión de Agregaciones**: Se excluyen regiones agregadas (World, Europe, Asia, etc.) del mapa
       para enfocarse en países individuales con datos comparables
    3. **Normalización Temporal**: La aplicación sincroniza todas las visualizaciones al año seleccionado,
       permitiendo comparaciones temporales consistentes
    
    ### Limitaciones Conocidas
    - Algunos países tienen datos incompletos para ciertos años
    - Las emisiones pueden incluir comercio internacional de carbono
    - Datos faltantes se muestran en gris en el mapa y se excluyen de cálculos
    - La cobertura histórica varía por país
    
    ### Tecnología
    - **Framework**: Streamlit
    - **Visualizaciones**: Plotly
    - **Procesamiento**: Pandas, NumPy
    - **Datos Geográficos**: ISO 3166-1 alpha-3 codes
    """)

# Footer
st.markdown("""
---
*Aplicación desarrollada con Streamlit, Plotly y datos de Our World in Data*
""")
