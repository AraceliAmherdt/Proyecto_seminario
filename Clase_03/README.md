# Clase 03 - Conexión a GitHub

Cómo conectar un proyecto local con un repositorio en GitHub.

## 1. Tener un repositorio Git local

Si la carpeta del proyecto todavía no es un repositorio Git, se inicializa con:
```powershell
git init
```

Conviene tener ya un `.gitignore` armado (para excluir `venv/`, `.gradio/`, etc.) antes de empezar a agregar archivos.

## 2. Crear el repositorio en GitHub

Desde GitHub, crear un repositorio nuevo (botón "New repository"). **Importante:** si ya existe un proyecto local con contenido, conviene crear el repo **vacío**, sin tildar "Add a README" ni "Add .gitignore" — así se evita el conflicto de historias no relacionadas al hacer el primer push.

## 3. Conectar el repositorio local con el de GitHub

Se usa `git remote add` con la URL del repositorio (HTTPS o SSH):
```powershell
git remote add origin https://github.com/usuario/nombre-repo.git
```

Esto le dice a Git: "el remoto que voy a llamar `origin` es esa URL". Se puede verificar que quedó bien conectado con:
```powershell
git remote -v
```

## 4. Preparar y confirmar los cambios (add + commit)

```powershell
git add .
git commit -m "mensaje describiendo el cambio"
```

`git add` marca los archivos para el próximo commit, y `git commit` guarda ese punto en el historial local.

## 5. Subir los cambios a GitHub (push)

```powershell
git push -u origin main
```

El flag `-u` deja guardada la relación entre la rama local `main` y `origin/main`, para que en los próximos push alcance con escribir `git push` a secas.

## Notas

- Si el repo remoto ya tenía contenido/commits propios (por ejemplo, un README creado desde GitHub) y se quiere reemplazar todo por el proyecto local, el push normal es rechazado por tener historias no relacionadas. En ese caso se usa `git push --force origin main`, que sobrescribe la rama remota por completo con el historial local — acción irreversible, hay que estar seguro antes de usarla.
- `git fetch origin` sirve para traer el estado del remoto sin aplicarlo, útil para revisar qué hay antes de decidir cómo hacer el push.

## Actividad de la semana

Contá cómo resolviste cada situación de la clase de hoy.

### 1. README duplicado

Si cuando creamos un proyecto local agregamos un documento README.md, y al crear el repo que después conectaremos se crea otro README, al momento de pushear va a entrar en conflicto y no sabrá cuál elegir, teniendo que editarlo a mano y luego generar otro add y push. La manera más limpia y fácil de evitarnos esos problemas es que, al momento de crear nuestro repo, destildemos la opción de que se cree con su README, y al pushear desde nuestro local, solo tendremos el README.md creado en nuestro proyecto, sin que entre en conflicto.

### 2. Carpeta sin ignorar

El archivo `.gitignore` sirve para ignorar, en nuestros `git add .` y en los push, todo lo que se encuentre listado en ese archivo. Si el `.gitignore` no está creado, vamos a enviar a nuestro repo todo lo que se incluya en la carpeta, y no queremos eso. En este caso, en nuestro `.gitignore` se encuentra el entorno virtual y `.gradio`, porque es lo que queremos que no se suba nunca a nuestro repo.

### 3. Ramas master / main

Puede suceder que en local, al poner el comando `git branch` para verificar qué ramas tenemos, nos aparezca la rama `master`, mientras que en GitHub la rama principal se llama `main`. Si pusheamos así, van a quedar dos ramas, `master` y `main`, cuando en realidad necesitamos una sola y que no queden duplicadas. Esto se resuelve poniendo desde nuestro local el comando `git branch -M main`, que renombra esa rama `master` como `main`, y de esta forma no quedan duplicadas.
