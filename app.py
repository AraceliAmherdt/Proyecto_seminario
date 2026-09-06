import gradio as gr
import spaces
import torch


@spaces.GPU
def saludar(nombre):
    # Trabajo mínimo en GPU: valida que el entorno ZeroGPU está OK.
    # Reemplazar por la inferencia real del modelo cuando esté listo.
    _ = torch.zeros(1, device="cuda")
    return f"Hola {nombre}"


demo = gr.Interface(fn=saludar, inputs="text", outputs="text")
demo.launch()
