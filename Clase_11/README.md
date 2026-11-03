# Clase 11 - Publicar un modelo con su Model Card

Actividad: publicar en Hugging Face Hub cuatro modelos ya entrenados, cada uno con su Model Card (`README.md`), y responder preguntas sobre qué se sube, qué hace falta para usar cada modelo y en qué se diferencian las bibliotecas.

## Qué hay en la carpeta

| Archivo / carpeta | Contenido |
|---|---|
| [ifts18-practica-model-cards](ifts18-practica-model-cards/README.md) | Repositorio de la práctica, clonado del repo de la docente. Tiene los cuatro modelos listos para publicar y su propio README con todas las instrucciones. |
| `Respuestas actividad clase 11.pdf` | Mis respuestas a las 9 preguntas de la actividad. |

### Los cuatro modelos

| Carpeta | Biblioteca | Problema | Modelo entrenado | En Hugging Face |
|---|---|---|---|---|
| `01-sklearn-regresion` | scikit-learn | precio de una casa (regresión) | `model.joblib` | [ver modelo](https://huggingface.co/AraceliAmherdt/01-sklearn-regresion) |
| `02-pytorch-regresion` | PyTorch | precio de una casa (regresión) | `model.safetensors` + `config.json` + `modelo.py` | [ver modelo](https://huggingface.co/AraceliAmherdt/02-pytorch-regresion) |
| `03-keras-regresion` | Keras | precio de una casa (regresión) | `model.keras` | [ver modelo](https://huggingface.co/AraceliAmherdt/03-keras-regresion) |
| `04-transformers-clasificacion-texto` | Transformers | comentario positivo o negativo | `model.safetensors` + `config.json` + tokenizer | [ver modelo](https://huggingface.co/AraceliAmherdt/04-transformers-clasificacion-texto) |

Los tres de regresión usan los mismos datos de la [Clase 10](../Clase_10/README.md). La carpeta `00-formatos-exportacion` tiene ejemplos de otros formatos de exportación (pickle, skops, ONNX, TorchScript, `torch.export`, SavedModel, TFLite, `.weights.h5`).

## Qué hice

1. Publiqué cada una de las cuatro carpetas como un repositorio de modelo distinto en Hugging Face Hub, desde la web (*Files and versions → Add file → Upload files*). Los links a cada uno están en la tabla de arriba.
2. Revisé en cada repo la pestaña **Model card**, las etiquetas que genera el encabezado YAML y el botón **Use this model**.
3. Respondí las preguntas en el PDF. Entre otras cosas:
   - qué archivo es el modelo entrenado en cada repo y cuáles hacen falta para **usarlo** o para **reproducirlo**;
   - por qué PyTorch necesita `modelo.py` y la normalización aparte, y Keras no;
   - por qué estos modelos no se pueden usar con `InferenceClient` como el modelo de cardiffnlp del TP (ningún Inference Provider los tiene desplegados);
   - en qué repos funciona el código de **Use this model** (en el 01 falla porque busca `sklearn_model.joblib` en vez de `model.joblib`).

## Cómo correr los ejemplos

Todo se corre desde la carpeta `ifts18-practica-model-cards`, que tiene su propio `requirements.txt`:

```powershell
cd ifts18-practica-model-cards
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

python 01-sklearn-regresion/predict.py                                          # usa el modelo local
python 01-sklearn-regresion/predict_hub.py AraceliAmherdt/01-sklearn-regresion  # baja el modelo del Hub
```

Cambiando `01-sklearn-regresion` por otra carpeta se prueba cada ejemplo. El detalle está en el [README de la práctica](ifts18-practica-model-cards/README.md).

## Notas

- `ifts18-practica-model-cards` es un clon con su propia carpeta `.git` (remoto: `cynthiavillagra/ifts18-practica-model-cards`). Si se agrega así a este repositorio, Git la guarda como una referencia a otro repo y no sube sus archivos. Para que los archivos queden acá, hay que borrar esa carpeta `.git` interna antes de hacer `git add`.
- Al subir al Hub no hay que arrastrar las carpetas `.venv` ni `__pycache__`.
