# Clase 10 - Del dataset al modelo exportado

Actividad: recorrer el camino completo del entrenamiento de un modelo de regresión lineal (datos → predicción → pérdida → optimizador) y exportar el modelo entrenado a un archivo que se pueda usar en otra app sin volver a entrenar.

## Qué hay en la carpeta

- `Clase_10_Modelo_Completo_PyTorch (1).ipynb`: notebook de la clase (material de la docente, Cynthia M. Villagra), ya ejecutado y con mi actividad resuelta al final.

## Qué se trabaja en el notebook

El problema: predecir el precio de una casa (en miles de US$) a partir de tres características: `m2`, `balcon` y `ascensor`. Los datos son 200 casas generadas con `numpy` y una semilla fija, así que siempre salen iguales.

1. **El problema**: se plantea la fórmula `precio = w1·m2 + w2·balcon + w3·ascensor + b` y se estiman los pesos "a ojo" mirando los datos, antes de entrenar.
2. **Una vuelta del camino, a mano**: una iteración del entrenamiento con los números a la vista, caja por caja: entran los datos, el modelo predice, la pérdida mide el error y el optimizador corrige `w` y `b`. Después, filas, vueltas y épocas.
3. **scikit-learn**: `LinearRegression`, `SGDRegressor` (el mismo modelo recorriendo el camino) y la importancia de escalar las entradas con `StandardScaler`.
4. **PyTorch**: el mismo ciclo escrito explícitamente (tensores, `nn.Linear`, pérdida, optimizador).
5. **Keras**: el mismo ciclo, pero escondido adentro de `fit`.
6. **Evaluación**: medir el modelo con casas que no vio (`r2_score`, error cuadrático medio).
7. **¿Qué es un modelo?**: los parámetros aprendidos más la transformación de las entradas (`make_pipeline`).
8. **Exportar el modelo**: `joblib` en scikit-learn, `state_dict` en PyTorch y `.keras` en Keras. Se ve qué guarda cada formato y qué hay que guardar aparte, por ejemplo el scaler.

Al final hay una **actividad**, un resumen y un glosario.

## Mi actividad: formato "modelo completo" (PyTorch)

La actividad pide elegir un formato de exportación, exportar el modelo con ese formato y responder cuatro preguntas. Yo elegí el **modelo completo** de PyTorch:

```python
torch.save(modelo_pt, CARPETA / "casas_completo.pt")
joblib.dump(scaler, CARPETA / "casas_completo_scaler.joblib")   # el scaler viaja aparte
```

A diferencia del `state_dict` (sección 8.2), que guarda solo el diccionario de parámetros, este formato guarda el **objeto entero**. Resumen de mis respuestas:

1. **¿Qué guarda? ¿Dónde están w y b?** Guarda el objeto Python completo usando pickle: los parámetros (w y b como tensores, dentro de cada capa), los buffers, la estructura de capas y una *referencia* a la clase (solo su nombre y su módulo, no el código).
2. **¿Hace falta la misma librería? ¿Hay que volver a escribir la fórmula?** Sí a las dos. Hace falta PyTorch (`torch.load`), mejor en una versión igual o parecida. La clase también tiene que estar definida en el código, porque la fórmula vive en `forward` y eso no se guarda en el archivo.
3. **¿Es seguro abrir un archivo de un desconocido?** **No.** Para cargarlo hay que usar `weights_only=False`, y la documentación de `torch.load` advierte que un pickle malicioso puede ejecutar código arbitrario.
4. **¿Para qué caso lo elegiría?** Para seguir entrenando, sí. Para una app de Gradio puede servir, aunque el `state_dict` es más robusto. Para un celular, no (para eso está `torch.export`). Para compartirlo en Hugging Face Hub, tampoco: ahí conviene `safetensors`.

## Cómo correrlo

El notebook está pensado para **Google Colab**: abrirlo ahí y ejecutar las celdas **de a una, en orden**. La primera celda instala lo que no viene en Colab (`skops`, `skl2onnx`, `onnx`, `onnxscript`, `onnxruntime`).

Para correrlo local en VS Code hace falta un entorno con Jupyter y estas librerías:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install jupyter numpy pandas matplotlib scikit-learn torch keras tensorflow joblib skops skl2onnx onnx onnxscript onnxruntime
```

## Notas

- Las celdas marcadas como **PREDICCIÓN** piden escribir una estimación en la celda de texto **antes** de ejecutar el código que da la respuesta.
- Al ejecutar la sección 8 y la actividad se crea una carpeta `modelos_exportados/` con los archivos exportados (`casas.joblib`, `casas_pt.pt`, `casas.keras`, `casas_completo.pt` y los scalers). Esa carpeta no está en el repo: se genera al correr el notebook.
- Los mismos datos y el mismo problema se retoman en la [Clase 11](../Clase_11/README.md) para publicar los modelos en Hugging Face Hub.
