import gradio as gr
import spaces
import torch


@spaces.GPU
def saludar(nombre):
    # Trabajo mínimo en GPU: valida que el entorno ZeroGPU está OK.
    # Reemplazar por la inferencia real del modelo cuando esté listo.
    _ = torch.zeros(1, device="cuda")
    return f"Hola {nombre}"


with gr.Blocks() as demo:
    nombre = gr.Textbox(label="Tu nombre")
    salida = gr.Textbox(label="Respuesta")
    boton = gr.Button("Saludar")

    boton.click(fn=saludar, inputs=nombre, outputs=salida)

demo.launch()
