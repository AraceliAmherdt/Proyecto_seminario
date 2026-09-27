# Clase 05 - Deploy

Actividad: llevar una app de Gradio a producción y probar un deploy mínimo con otra plataforma (Streamlit).

## Deploy en Render

Se desplegó la app de [Clase_04](../Clase_04) (`appConBlocks.py`) en [Render](https://render.com/).

**Link:** https://proyecto-seminario-1.onrender.com/

Configuración usada en Render:
- **Root Directory:** `Clase_04` (para que Render encuentre `requirements.txt` y `appConBlocks.py`, que no están en la raíz del repositorio)
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python appConBlocks.py`

El script detecta si está corriendo en Render (variable de entorno `PORT`) y en ese caso escucha en `0.0.0.0` en el puerto que Render asigna, en vez de usar `share=True` (que solo sirve para el link temporal en local).

## Deploy mínimo en Streamlit

Se hizo, además, una app mínima con [Streamlit](https://streamlit.io/) y se desplegó en Streamlit Community Cloud.

**Link:** https://appapp-kyse5lfheaa2dtk5japada.streamlit.app/

> Esta app se armó y desplegó por fuera de este repositorio.

## Notas

- Render tarda unos segundos en "despertar" si la app estuvo inactiva (plan gratuito) — la primera carga después de un rato sin uso puede demorar más de lo normal.

## Comparación Render vs. Streamlit

El despliegue de ambas fue muy similar, me pareció más fácil de configurar Streamlit, pero porque tenía una sola carpeta con su requirements, a diferencia del despliegue de Render que, al ser de todas las carpetas de las clases, hay que configurar bien las rutas para que tome los requirements correspondientes.

En el funcionamiento también me pareció más rápido Streamlit, tanto al deployarse como al abrir el link productivo.
