# Clase 02 - Introducción a Gradio

Primer ejemplo de interfaz web simple usando la librería [Gradio](https://www.gradio.app/), que permite crear interfaces gráficas para funciones de Python sin necesidad de HTML/CSS/JS.

## Qué hace `app.py`

Define una función `greet(name, intensity)` que devuelve un saludo repitiendo signos de exclamación según la intensidad elegida, y la expone en una interfaz web con dos inputs (texto y slider) y un output de texto.

## Requisitos

- Python 3.13
- Entorno virtual (`venv`) con las dependencias listadas en `requirements.txt`

## Cómo levantar el entorno

1. Crear el entorno virtual (si no existe todavía):
   ```powershell
   python -m venv venv
   ```

2. Activarlo:
   - **PowerShell**: `.\venv\Scripts\Activate.ps1`
   - **CMD**: `.\venv\Scripts\activate.bat`
   - **Git Bash**: `source venv/Scripts/activate`

   Con el entorno activo, el prompt debería mostrar `(venv)` al inicio.

3. Instalar las dependencias:
   ```powershell
   pip install -r requirements.txt
   ```

## Cómo correr la app

Con el entorno virtual activado:
```powershell
python app.py
```

Va a mostrar algo como:
```
Running on local URL:  http://127.0.0.1:7860
```

Abrí esa URL en el navegador para probar la interfaz.

> **Nota:** en VSCode, el botón ▶️ "Run Python File" usa el intérprete seleccionado en la barra inferior derecha, no necesariamente el del venv activo en la terminal. Verificá con `Ctrl+Shift+P` → `Python: Select Interpreter` que esté seleccionado `venv\Scripts\python.exe`.

## Notas

- Al ejecutar la app se genera una carpeta `.gradio/` (con un certificado local) en el directorio desde donde se corre el script. Está ignorada en `.gitignore`, junto con `venv/`.
- `requirements.txt` no se actualiza solo al instalar paquetes nuevos — hay que agregarlos a mano, o regenerarlo completo con `pip freeze > requirements.txt`.
