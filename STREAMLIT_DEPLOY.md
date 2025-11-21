# Instrucciones de Deploy en Streamlit Community Cloud

## Estado Actual

✅ **Completado:**
- Repositorio GitHub con estructura profesional
- Código base completamente funcional en `app.py`
- Dependencies configuradas en `requirements.txt`
- Documentación completa en `README.md`
- Datos integrados desde GitHub OWID
- Visualizaciones interactivas con Plotly
- 4 pestañas de navegación
- Manejo de errores y validación de datos

## Pasos para Completar el Deploy

### 1. Verificar Cuenta de Streamlit

- Ve a https://share.streamlit.io
- Completa la verificación de correo electrónico que recibas
- Inicia sesión con tu cuenta GitHub

### 2. Crear Nueva Aplicación

Una vez logeado en Streamlit Cloud:

1. Haz clic en **"New app"**
2. Selecciona **"From existing repo"**
3. Ingresa los siguientes datos:
   - **Repository**: `oneirac/tarea2-co2-emisiones`
   - **Branch**: `main`
   - **Main file path**: `app.py`
4. Haz clic en **"Deploy"**

### 3. Esperar Deploy

- Streamlit descargará dependencias
- Instalará paquetes
- Ejecutará la aplicación
- Generará un enlace público

El proceso toma 3-5 minutos en la primera ejecución.

### 4. Probar Aplicación

Una vez desplegada:

1. Accede a la URL pública generada
2. Prueba los controles:
   - Slider de año (1750-2023)
   - Dropdown de países
   - Radio buttons de métricas
3. Navega por las 4 pestañas:
   - 🗺 Mapa Global
   - 📊 Top Emisores
   - 📏 Tendencias
   - 📝 Información

## URL del Deploy

Una vez completado, la URL será algo como:
```
https://share.streamlit.io/oneirac/tarea2-co2-emisiones/main/app.py
```

o más simple:
```
https://[your-app-name].streamlit.app
```

## Solucionar Problemas

### Si falta un paquete:
- Verifica que `requirements.txt` tenga todas las dependencias
- Haz un commit y Streamlit recargará

### Si el mapa no carga:
- Espera a que los datos se descarguen de OWID (13.6 MB)
- Puede tardar 5-10 segundos en la primera carga

### Si hay errores:
- Ve a la sección "Logs" en Streamlit Cloud
- Verás mensajes de error detallados

## Resumen de Entrega Final

**Repositorio GitHub**: https://github.com/oneirac/tarea2-co2-emisiones

**Archivos incluidos**:
- ✅ `app.py` - Aplicación principal
- ✅ `requirements.txt` - Dependencias
- ✅ `README.md` - Documentación extensa
- ✅ `.gitignore` - Configuración Git
- ✅ `STREAMLIT_DEPLOY.md` - Instrucciones de deploy (este archivo)

**Cumplimiento de Rúbrica**:
- ✅ Rigor analítico y uso de datos (manejo correcto de variables OWID)
- ✅ Diseño visual e interactividad (4 visualizaciones interactivas + controles)
- ✅ Replicación de gráficos OWID (Mapa, Top emisores, Tendencias)
- ✅ Arquitectura limpia y UX (Streamlit con tabs + sidebar)
- ✅ Trazabilidad técnica (Documentación profesional)

---

**Creado**: 21 de noviembre, 2025
**Estado**: Listo para producción ✅
