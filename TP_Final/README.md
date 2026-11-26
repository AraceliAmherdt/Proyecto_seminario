# TP Final - Estimador de costo de seguro médico

Proyecto completo de machine learning de punta a punta: entrenar un modelo de regresión, exportarlo, servirlo con una API en **FastAPI** y consumirlo desde una página web en HTML/CSS/JavaScript.

La app estima el **costo anual de un seguro médico** (en dólares) a partir de seis datos de una persona: edad, sexo, índice de masa corporal (IMC), hijos a cargo, si fuma y región de EE. UU.

**App online:** https://araceliamherdt.github.io/Proyecto_seminario/TP_Final/app/frontend/

**API online (Render):** https://api-seguro-medico.onrender.com

> La API está en el plan gratuito de Render: si estuvo un rato sin uso, la primera consulta puede tardar unos segundos mientras el servidor se despierta.

## Qué hay en la carpeta

```
TP_Final/
├── notebook/
│   ├── entrenamiento.ipynb     # exploración, comparación de modelos y exportación
│   └── datos/insurance.csv     # dataset descargado por la notebook
├── app/
│   ├── modelo/modelo.joblib    # pipeline entrenado (preprocesamiento + modelo)
│   ├── backend/
│   │   ├── main.py             # API en FastAPI
│   │   └── requirements.txt
│   └── frontend/
│       ├── index.html          # formulario
│       ├── style.css
│       └── app.js              # llama a la API con fetch y muestra el resultado
└── TPF_Amherdt_Araceli.pptx    # presentación del trabajo
```

## 1. Entrenamiento del modelo (`notebook/entrenamiento.ipynb`)

**Dataset:** *Medical Cost Personal* (`insurance.csv`) del libro *Machine Learning with R*, con datos simulados. Tiene 1338 filas; se eliminó 1 duplicada y quedaron 1337. Las columnas se renombraron al español.

- **Features numéricas:** `edad`, `imc`, `hijos`
- **Features categóricas:** `sexo`, `fumador`, `region`
- **Target:** `costo`

**Exploración:** la mediana del costo (9382) es bastante menor que la media (13270), y la variable que más pesa es ser fumador: en promedio un fumador paga unos US$ 32 050 y un no fumador unos US$ 8441, es decir, cerca de 3,8 veces más.

**Preparación:** separación 80/20 en entrenamiento y prueba (`random_state=42`) y un `ColumnTransformer` con `StandardScaler` para las numéricas y `OneHotEncoder` para las categóricas, todo dentro de un `Pipeline`. Así el archivo exportado incluye también la transformación de las entradas.

**Comparación de modelos** (sobre el conjunto de prueba):

| Modelo | MAE | RMSE | R² | Peso del `.joblib` |
|---|---|---|---|---|
| Línea base (`DummyRegressor`) | 9862 | 13 612 | -0.008 | — |
| Regresión lineal | 4177 | 5956 | 0.807 | 0.004 MB |
| Random Forest (sin límite) | 2583 | 4673 | 0.881 | 9.7 MB |
| **Random Forest, profundidad 5, 200 árboles** | **2419** | **4245** | **0.902** | **0.95 MB** |

Con validación cruzada de 5 particiones se confirmó el resultado (MAE promedio: lineal 4200, RF completo 2671, RF profundidad 5 2513).

**Modelo elegido:** el Random Forest limitado a 5 niveles. Tiene el mejor error, generaliza mejor porque aprende patrones generales en lugar de memorizar, y pesa diez veces menos que el bosque sin límite, algo importante para subirlo a un servidor gratuito. Se exportó con `joblib` a `app/modelo/modelo.joblib` (scikit-learn 1.9.1) y se probó cargándolo de nuevo.

## 2. API (`app/backend/main.py`)

API hecha con **FastAPI**:

- Carga el modelo **una sola vez** al iniciar (con `lifespan`), no en cada consulta.
- Valida la entrada con **Pydantic**: edad de 18 a 64, IMC de 10 a 60, hijos de 0 a 5, y valores fijos para `sexo` (`female`/`male`), `fumador` (`yes`/`no`) y `region` (`northeast`, `northwest`, `southeast`, `southwest`). Si algo no cumple, responde **422** con el detalle.
- Configura **CORS** para aceptar llamadas solo desde `localhost:5500` y desde GitHub Pages.

Endpoints:

| Método | Ruta | Qué hace |
|---|---|---|
| GET | `/health` | Verifica que la API está viva |
| POST | `/predecir` | Recibe los datos de una persona y devuelve `costo_estimado` |
| GET | `/docs` | Documentación interactiva generada por FastAPI |

Ejemplo de consulta:

```json
POST /predecir
{ "edad": 35, "sexo": "male", "imc": 28.5, "hijos": 2, "fumador": "no", "region": "northwest" }
```

Respuesta:

```json
{ "costo_estimado": 6792.2 }
```

## 3. Frontend (`app/frontend/`)

Página estática con un formulario de los seis datos. `app.js` arma el JSON, lo manda a `/predecir` con `fetch` y muestra:

- el costo estimado, formateado en dólares;
- la lista de campos inválidos si la API responde 422;
- un aviso si no se pudo conectar (API apagada o bloqueo por CORS).

Detecta sola a qué API llamar: si la página se abre en `localhost` usa la API local (`http://127.0.0.1:8000`); si no, la de Render.

## 4. Deploy

- **Backend:** en **Render**, como servicio web con Uvicorn.
- **Frontend:** en **GitHub Pages**, servido desde este mismo repositorio.

## Cómo correrlo localmente

Desde la carpeta `TP_Final`:

```bash
# 1. Crear y activar el entorno virtual
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux / Mac

# 2. Instalar dependencias
pip install -r app/backend/requirements.txt

# 3. Levantar la API
cd app/backend
uvicorn main:app --reload
```

La API queda en http://127.0.0.1:8000 y la documentación en http://127.0.0.1:8000/docs.

Para el frontend, servir la carpeta `app/frontend` en el puerto 5500 (por ejemplo con la extensión *Live Server* de VS Code, o con `python -m http.server 5500` desde esa carpeta) y abrir http://localhost:5500.

Para volver a entrenar el modelo, abrir `notebook/entrenamiento.ipynb` con el mismo entorno (además hace falta `ipykernel` para correrla en Jupyter o VS Code) y ejecutar todas las celdas.

> El modelo se guardó con scikit-learn 1.9.1. Conviene usar esa misma versión (la de `requirements.txt`) para cargarlo sin advertencias ni errores.

## Límites

- Los datos son simulados y de EE. UU.: el modelo sirve como ejercicio, no para estimar el costo real de un seguro.
- Solo acepta los rangos con los que se entrenó (por ejemplo, edades de 18 a 64).
