# Seminario de Actualización - IFTS 18

Repositorio con las actividades semanales del Seminario de Actualización correspondiente al IFTS 18, organizados por clase, más el Trabajo Práctico Integrador y el Trabajo Práctico Final.

**Alumna:** Araceli Amherdt

## Estructura del repositorio

Cada carpeta tiene su propio `README.md` con el detalle de lo trabajado: qué hace el código, cómo instalar las dependencias y cómo correrlo. Esta tabla es solo un índice — la explicación completa de cada entrega está en el README de su propia carpeta.

| Carpeta | Contenido |
|---|---|
| [Clase_02](Clase_02/README.md) | Introducción a Gradio: primera interfaz web simple con Python |
| [Clase_03](Clase_03/README.md) | Conexión de un proyecto local con un repositorio en GitHub |
| [Clase_04](Clase_04/README.md) | Gradio con Blocks: componente nuevo y función propia |
| [Clase_05](Clase_05/README.md) | Deploy en Render y prueba mínima en Streamlit |
| Clase_06 | Ticket de salida de la clase (PDF) |
| [Clase_10](Clase_10/README.md) | Del dataset al modelo exportado: el camino del entrenamiento en scikit-learn, PyTorch y Keras |
| [Clase_11](Clase_11/README.md) | Publicar modelos en Hugging Face Hub con su Model Card |

## Trabajo Práctico Integrador

[**TP_Integrador**](TP_Integrador/README.md) — Clasificador de gastos con IA: una app de Gradio que clasifica gastos escritos en lenguaje natural usando un modelo zero-shot de Hugging Face, desplegada en Hugging Face Spaces. Incluye la notebook con la comparación de modelos, el informe y la presentación en PDF. El detalle completo (qué hace, cómo correrla local, cómo publicar cambios al Space, límites conocidos) está en su propio README.

**App online:** https://huggingface.co/spaces/AraceliAmherdt/Clasificador_gastos

## Trabajo Práctico Final

[**TP_Final**](TP_Final/README.md) — Estimador de costo de seguro médico: proyecto de machine learning de punta a punta. En una notebook se exploró el dataset *insurance*, se compararon varios modelos y se eligió un Random Forest de profundidad 5 (R² 0.90), exportado con `joblib`. El modelo se sirve con una API en FastAPI desplegada en Render, y una página en HTML/CSS/JavaScript publicada en GitHub Pages la consume. También está la presentación (`.pptx`). Su README tiene el detalle de cada parte y cómo correrlo local.

**App online:** https://araceliamherdt.github.io/Proyecto_seminario/TP_Final/app/frontend/

## Cómo usar este repositorio

Cada clase, el TP Integrador y el TP Final tienen su propio entorno virtual y de ser necesario (segun la actividad semanal), sus propias dependencias (`requirements.txt`) independientes entre sí. Entrá a la carpeta que te interese y seguí las instrucciones de su README para levantar el entorno correspondiente.
