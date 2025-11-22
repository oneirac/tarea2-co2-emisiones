# Tarea 2: Emisiones de CO₂ Global - Visualización Interactiva con Streamlit

## 🎯 Descripción

Aplicación web interactiva desarrollada en **Streamlit** para explorar y analizar datos de emisiones de CO₂ a nivel mundial. La aplicación utiliza datos de **Our World in Data (OWID)**, visualizaciones interactivas con **Plotly**, y un flujo de trabajo versionado en **GitHub**.

La aplicación permite:
- Visualizar emisiones de CO₂ por país en un mapa interactivo
- Explorar tendencias temporales de emisiones
- Comparar emisores globales
- Analizar métricas por país seleccionado

## 🌐 Links de Entrega

- **Repositorio GitHub**: https://github.com/oneirac/tarea2-co2-emisiones
- **Aplicación Streamlit Cloud**: [Será actualizado después del deploy]

## 📋 Requisitos Mínimos

- Python >= 3.8
- Streamlit >= 1.28.0
- Pandas >= 2.0.0
- Plotly >= 5.17.0
- GeoPandas >= 0.13.0

## 🚀 Instalación y Ejecución Local

### 1. Clonar el repositorio

```bash
git clone https://github.com/oneirac/tarea2-co2-emisiones.git
cd tarea2-co2-emisiones
```

### 2. Crear ambiente virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
streamlit run app.py
```

La aplicación se abrirá en `http://localhost:8501`

## 📊 Estructura del Repositorio

```
tarea2-co2-emisiones/
├── app.py                 # Código principal de la aplicación Streamlit
├── requirements.txt       # Dependencias del proyecto
├── .gitignore            # Archivos a ignorar en Git
├── README.md             # Este archivo
└── utils/                # (Futura) Funciones auxiliares
```

## 📈 Visualizaciones Implementadas

### 1. **Mapa Global (Choropleth)**
- Visualiza emisiones de CO₂ por país para un año seleccionado
- Paleta de colores OrRd (Orange-Red) para representar intensidad de emisiones
- Interactividad: hover para ver detalles de cada país
- Sincroniza con selector de año y métrica

### 2. **Top 15 Emisores (Gráfico de Barras)**
- Muestra los 15 países con mayores emisiones en el año seleccionado
- Ordenamiento descendente por volumen de CO₂
- Colores escalonados para visualizar jerarquía

### 3. **Tendencias Temporales (Gráfico de Línea)**
- Evolución de emisiones del país seleccionado desde 1750 a presente
- Permite identificar picos y cambios significativos
- Incluye métricas: emisión actual, cambio desde 1990, pico histórico

## 🎨 Decisiones de Diseño

### Decisión 1: Paleta de Colores OrRd
**Justificación**: La escala Orange-Red es intuitiva para datos de contaminación. El naranja representa niveles bajos de emisión, transitando al rojo intenso para altos niveles. Esta progresión refleja visualmente el concepto de "urgencia ambiental".

### Decisión 2: Exclusión de Agregaciones Globales
**Justificación**: Se excluyen entidades como "World", "Europe", "Asia" del mapa principal para enfocarse en países individuales (códigos ISO3). Esto permite:
- Comparaciones más rigurosas entre territorios equivalentes
- Evitar doble conteo en análisis globales
- Mayor claridad en la navegación

### Decisión 3: Layout con Pestañas (Tabs)
**Justificación**: Organiza información diversa sin sobrecargar la interfaz:
- Mapa global (pestaña 1): exploración geográfica
- Top emisores (pestaña 2): análisis comparativo
- Tendencias (pestaña 3): análisis temporal
- Información (pestaña 4): documentación y metodología

## 📊 Fuente de Datos

- **Proveedor**: Our World in Data (OWID)
- **Dataset**: Annual CO₂ emissions per country
- **URL**: https://github.com/owid/co2-data
- **Cobertura**: 1750-2023 (según disponibilidad por país)
- **Formato**: CSV descargado automáticamente desde GitHub raw
- **Actualización**: Los datos se cargan en tiempo real desde el repositorio de OWID

### Variables Principales
- `country`: Nombre del país o región
- `year`: Año del registro
- `iso_code`: Código ISO3 para mapeo geográfico
- `co2`: Emisión total en millones de toneladas (Mt)
- `co2_per_capita`: Emisión per cápita en toneladas (t)
- `population`: Población del país

## ⚠️ Limitaciones y Consideraciones

### Datos Faltantes
- Algunos países no tienen datos para todos los años
- Países sin datos en un año específico aparecen en gris en el mapa
- Se excluyen automáticamente de cálculos de totales

### Cobertura Histórica Variable
- Datos de países desarrollados: generalmente desde 1800-1900
- Datos de países en desarrollo: frecuentemente desde 1950-1990
- Datos recientes: hasta 2023 (con lag de 1-2 años)

### Metodología de Emisiones
- Incluye emisiones de combustibles fósiles e industria
- No incluye todas las fuentes de GEI (ej: agricultura, ganadería)
- Puede incluir comercio internacional de carbono según metodología OWID

### Limitaciones Técnicas
- Cargar dataset completo (13.6 MB) puede tomar 5-10 segundos la primera vez
- Interactividad del mapa depende de la velocidad de conexión
- Algunos navegadores antiguos pueden tener limitaciones

## 🔧 Tecnología

- **Framework Web**: Streamlit (Python)
- **Visualización**: Plotly (gráficos interactivos)
- **Procesamiento de Datos**: Pandas, NumPy
- **Datos Geográficos**: ISO 3166-1 alpha-3 codes
- **Control de Versiones**: Git + GitHub
- **Despliegue**: Streamlit Community Cloud

## 📝 Uso de IA

[Completar con disclosure si corresponde: "Esta aplicación fue desarrollada con asistencia de IA para: generación de template, optimización de código, etc."]

## 👥 Equipo

- **Nombre de integrantes**:  jasandovalv, sofialaniss, danteaguirreb, oneirac
- **Correos**: jaisandovalv@udd.cl, S.alanisalvarez@gmail.com , d.aguirreb@udd.cl, osvaldoneira@gmail.com
- **Fecha de entrega**: 23 de noviembre, 2025

## 📚 Referencias

- [Our World in Data - CO₂ Emissions](https://ourworldindata.org/co2-emissions)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Python](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/)

## 📄 Licencia

Este proyecto está disponible bajo licencia MIT.

---

**Última actualización**: 21 de noviembre, 2025
