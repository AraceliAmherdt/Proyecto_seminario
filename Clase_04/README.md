# Clase 04 - Gradio con Blocks

Actividad: pasar de `gr.Interface` a `gr.Blocks`, sumar un componente nuevo y una función propia conectada a su propio input/output.

## Qué hace `appConBlocks.py`

La interfaz está armada con `gr.Blocks()` (en vez de `gr.Interface`) y tiene dos partes independientes:

1. **Chatbot de saludo**: un `Textbox` para el nombre y un `Button` disparan `saludar()`, que va mostrando frases de a una en un `Chatbot`, simulando que "va hablando".
2. **Calculadora de interés simple**: un `Slider` (componente nuevo, no usado antes) para elegir un monto, y un `Button` disparan `calcular_interes_simple()`, que devuelve el interés generado a una tasa fija del 5% anual. Es una función pensada como base para más adelante, cuando la app evolucione a un chatbot de consultas financieras.

## Requisitos

- Python 3.13
- Entorno virtual (`venv`) con las dependencias de `requirements.txt`

## Cómo levantar el entorno

1. Crear el entorno virtual (si no existe):
   ```powershell
   python -m venv venv
   ```
2. Activarlo:
   - **PowerShell**: `.\venv\Scripts\Activate.ps1`
   - **CMD**: `.\venv\Scripts\activate.bat`
3. Instalar las dependencias:
   ```powershell
   pip install -r requirements.txt
   ```

## Cómo correr la app

Con el entorno virtual activado:
```powershell
python appConBlocks.py
```

Como el script usa `demo.launch(share=True)`, además del link local (`http://127.0.0.1:7860`) genera un link público temporal (`https://xxxxxxxx.gradio.live`) para compartir la app corriendo desde tu compu.

> **Nota:** si usás el botón ▶️ "Run Python File" de VSCode, verificá primero que el intérprete seleccionado (`Ctrl+Shift+P` → `Python: Select Interpreter`) sea el de `Clase_04\venv\Scripts\python.exe` y no el de otra carpeta.

## Notas

- Esta app se pensó en un principio para desplegarse en Hugging Face Spaces con ZeroGPU (por eso el nombre `appConBlocks.py` venía con `@spaces.GPU` y `torch`), pero el plan cambió a Render, así que se sacaron esas dependencias: no hace falta GPU para correrla.
- Al correrla se genera una carpeta `.gradio/` local (certificado), igual que en Clase_02 — ya está en el `.gitignore` de la raíz.
