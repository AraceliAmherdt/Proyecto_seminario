import time

import gradio as gr


def saludar(nombre, historial):
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


def calcular_interes_simple(capital):
    # Placeholder para futuras consultas financieras: tasa fija por ahora.
    tasa_anual = 0.05
    interes = capital * tasa_anual
    total = capital + interes
    return (
        f"Con un capital de ${capital:,.2f} al {tasa_anual * 100:.0f}% anual, "
        f"generarías ${interes:,.2f} de interés (total: ${total:,.2f})."
    )


with gr.Blocks() as demo:
    gr.Markdown("## Chatbot de saludo")
    chatbot = gr.Chatbot(label="Chatbot")
    nombre = gr.Textbox(label="Tu nombre")
    boton = gr.Button("Saludar")
    boton.click(fn=saludar, inputs=[nombre, chatbot], outputs=chatbot)

    gr.Markdown("## Calculadora de interés simple")
    capital = gr.Slider(minimum=0, maximum=1_000_000, step=1000, label="Monto a invertir ($)")
    resultado = gr.Textbox(label="Resultado")
    boton_calcular = gr.Button("Calcular")
    boton_calcular.click(fn=calcular_interes_simple, inputs=capital, outputs=resultado)

demo.launch(share=True)
