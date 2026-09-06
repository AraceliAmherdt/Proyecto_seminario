---
title: ProyectoSeminario
emoji: 🏆
colorFrom: gray
colorTo: pink
sdk: gradio
sdk_version: 6.26.0
python_version: '3.12'
app_file: app.py
pinned: false
license: mit
short_description: gradio
---

# Proyecto Integrador - IFST 18

App de ejemplo con Gradio. Deploy en Hugging Face Spaces:
https://huggingface.co/spaces/AraceliAmherdt/proyectoSeminario

## Requisitos

- Python 3.10 o superior

## Instalación

1. Crear y activar un entorno virtual (Windows):

   ```
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. Instalar las dependencias:

   ```
   pip install -r requirements.txt
   ```

## Uso local

```
python app.py
```

## Deploy a Hugging Face Spaces

```
git add -A
git commit -m "Actualizar app"
git push space main
```
