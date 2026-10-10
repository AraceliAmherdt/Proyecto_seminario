import gradio as gr


def saludar(texto):
    return f"Recibí: {texto}"


demo = gr.Interface(
    fn=saludar,
    inputs=gr.Textbox(label="Escribí un gasto"),
    outputs=gr.Textbox(label="Respuesta"),
    title="Clasificador de gastos",
)

demo.launch()