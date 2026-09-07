import time

import gradio as gr
import spaces
import torch


@spaces.GPU
def saludar(nombre, historial):
    # Trabajo mínimo en GPU: valida que el entorno ZeroGPU está OK.
    # Reemplazar por la inferencia real del modelo cuando esté listo.
    _ = torch.zeros(1, device="cuda")

    nombre = (nombre or "").strip() or "desconocido/a"
    frases = [
        f"Hola {nombre}, ¿cómo estás?",
        "Soy un chatbot de ejemplo del Proyecto Integrador.",
        "Cuando conectemos el modelo real voy a poder responderte de verdad.",
    ]

    historial = historial or []
    for frase in frases:
        # cada yield actualiza el Chatbot -> efecto de "ir hablando"
        historial = historial + [{"role": "assistant", "content": frase}]
        yield historial
        time.sleep(0.6)


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages", label="Chatbot")
    nombre = gr.Textbox(label="Tu nombre")
    boton = gr.Button("Saludar")

    boton.click(fn=saludar, inputs=[nombre, chatbot], outputs=chatbot)

demo.launch()
