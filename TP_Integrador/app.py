import gradio as gr
import spaces
from transformers import pipeline

# --- Configuración (decidida en la notebook) ---
MODELO = "MoritzLaurer/mDeBERTa-v3-base-mnli-xnli"
CATEGORIAS = ["comida", "transporte", "servicios", "salud", "ocio", "educación"]
PLANTILLA = "Este gasto es de {}."

# --- Se carga UNA vez, al arrancar la app (fuera de la función con GPU) ---
clasificador = pipeline("zero-shot-classification", model=MODELO, device="cuda")


# --- Se ejecuta en CADA consulta, con GPU prestada por ZeroGPU ---
@spaces.GPU
def clasificar(texto):
    if not texto or not texto.strip():
        return {}
    resultado = clasificador(
        texto,
        candidate_labels=CATEGORIAS,
        hypothesis_template=PLANTILLA,
    )
    return dict(zip(resultado["labels"], resultado["scores"]))


demo = gr.Interface(
    fn=clasificar,
    inputs=gr.Textbox(label="Escribí un gasto", placeholder="Ej.: cargué la SUBE"),
    outputs=gr.Label(label="Categoría", num_top_classes=3),
    title="Clasificador de gastos",
    description=(
        "Escribí un gasto como lo anotarías en el celular y la app lo clasifica en "
        "comida, transporte, servicios, salud, ocio o educación. "
        "Usa un modelo zero-shot de Hugging Face: no fue entrenado con estas categorías."
    ),
    examples=["cargué la SUBE", "pagué la factura de luz", "5 lucas a Juan por el asado"],
)

demo.launch()