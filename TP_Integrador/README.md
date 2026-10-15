---
title: Clasificador de gastos
emoji: 💸
colorFrom: green
colorTo: blue
sdk: gradio
sdk_version: 6.28.0
app_file: app.py
pinned: false
---

# Clasificador de gastos con IA

Trabajo Práctico Integrador · Seminario de Actualización · Tec. Sup. en Cs. de Datos e IA · IFTS N.º 18
**Autora:** Araceli Amherdt · 2026

**👉 App online:** https://huggingface.co/spaces/AraceliAmherdt/Clasificador_gastos

## Qué hace

Escribís un gasto como lo anotarías en el celular y la app lo clasifica en una de seis categorías:
**comida, transporte, servicios, salud, ocio o educación**.

| Escribís | La app responde |
|---|---|
| `cargué la SUBE` | transporte |
| `pagué la factura de luz` | servicios |

Muestra las tres categorías más probables con su puntaje, así se ve cuándo el modelo duda.

**¿Por qué IA y no palabras clave?** Un mismo gasto se escribe de infinitas maneras ("cargué la SUBE", "el bondi",
"5 lucas a Juan por el asado"). Una lista de palabras clave nunca termina de cubrirlas; el modelo interpreta el significado.

## Cómo funciona

- **Modelo:** [`MoritzLaurer/mDeBERTa-v3-base-mnli-xnli`](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli),
  multilingüe, 0,3B parámetros, 558 MB.
- **Técnica:** clasificación *zero-shot*. El modelo no fue entrenado con estas categorías: cada una se convierte en una
  hipótesis (`"Este gasto es de transporte."`) y el modelo calcula qué tan probable es. La app **infiere**, no entrena.
- **Cómo se ejecuta:** con `pipeline` de `transformers`. El modelo se descarga y corre dentro del servidor de la app,
  sin depender de créditos de Hugging Face.
- **Dónde corre:** Hugging Face Spaces con hardware ZeroGPU (plan gratuito).

La elección del modelo y de `pipeline` está justificada en la notebook `TP_Amherdt_Araceli.ipynb`.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `app.py` | La app: carga el modelo y arma la interfaz con Gradio |
| `requirements.txt` | Librerías que necesita la app, con la versión de Gradio fijada |
| `README.md` | Este archivo. El bloque entre `---` del principio es la configuración del Space |
| `TP_Amherdt_Araceli.ipynb` | Notebook con la comparación de modelos, tiempos y pruebas |

## Cómo correrla en tu compu

Requisitos: Python 3.10 o superior y unos 3 GB libres (librerías y modelo).
No hace falta GPU: si no hay, el modelo corre en CPU, más lento.

```bash
# 1. Clonar el repo y entrar a la carpeta del TP
git clone https://github.com/AraceliAmherdt/Proyecto_seminario/tree/main
cd Proyecto_seminario/TP_Integrador

# 2. (Recomendado) crear un entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux / Mac

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Correr la app
python app.py
```

Abrí en el navegador la dirección que aparece en la terminal (normalmente `http://127.0.0.1:7860`).
La primera vez tarda unos minutos porque descarga el modelo (558 MB); las siguientes, no.

No hace falta token de Hugging Face: el modelo es público.

## Cómo publicar cambios en el Space

El código vive en GitHub, dentro de `TP_Integrador/`. El Space es un segundo repositorio (*remote*) que recibe
solo esta carpeta, usando `git subtree`.

Una sola vez, desde la raíz del repo:

```bash
git remote add space https://huggingface.co/spaces/AraceliAmherdt/Clasificador_gastos
```

Cada vez que se quiera publicar:

```bash
git add .
git commit -m "Descripción del cambio"
git push                                            # sube a GitHub
git subtree push --prefix TP_Integrador space main  # publica en el Space
```

Git pide usuario de Hugging Face y, como contraseña, un **token con permiso de escritura**.

## Límites conocidos

- **Siempre elige una categoría**, aunque lo escrito no sea un gasto: los puntajes suman 100 %.
- **El Space se duerme** si nadie lo usa. La primera consulta después de eso tarda *[20.2 s, medido]* porque vuelve a cargar el modelo.
- **ZeroGPU usa la cuota diaria de GPU de cada visitante.** Con uso muy intenso, una persona podría agotarla.
- Hugging Face puede cambiar las condiciones del plan gratuito, como ya pasó en julio de 2026, cuando dejó de ofrecer
  CPU Basic gratis.