// Dirección de la API. Por ahora, la local. En la etapa 9 la cambiás por la de Render.
// Si la página se abre en tu compu usa la API local; si no, la publicada en Render.
const ES_LOCAL = ["localhost", "127.0.0.1"].includes(location.hostname);
const API_URL = ES_LOCAL
  ? "http://127.0.0.1:8000"
  : "https://api-seguro-medico.onrender.com";

const formulario = document.getElementById("formulario");
const boton = document.getElementById("boton");
const resultado = document.getElementById("resultado");

formulario.addEventListener("submit", async (evento) => {
  evento.preventDefault(); // evita que la página se recargue

  // 1. Armar el JSON con los datos del formulario
  const datos = {
    edad: Number(document.getElementById("edad").value),
    sexo: document.getElementById("sexo").value,
    imc: Number(document.getElementById("imc").value),
    hijos: Number(document.getElementById("hijos").value),
    fumador: document.getElementById("fumador").value,
    region: document.getElementById("region").value,
  };

  boton.disabled = true;
  boton.textContent = "Calculando…";
  resultado.innerHTML = "";

  try {
    // 2. Enviarlo a la API con fetch
    const respuesta = await fetch(`${API_URL}/predecir`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(datos),
    });
    const cuerpo = await respuesta.json();

    // 3. Mostrar el resultado según el código de estado
    if (respuesta.ok) {
      const costo = cuerpo.costo_estimado.toLocaleString("es-AR", { maximumFractionDigits: 0 });
      resultado.innerHTML = `<div class="ok">Costo anual estimado<strong>US$ ${costo}</strong></div>`;
    } else if (respuesta.status === 422) {
      const problemas = cuerpo.detail.map((e) => `<li>${e.loc.at(-1)}: ${e.msg}</li>`).join("");
      resultado.innerHTML = `<div class="error"><b>Datos inválidos (422)</b><ul>${problemas}</ul></div>`;
    } else {
      resultado.innerHTML = `<div class="error"><b>Error del servidor (${respuesta.status})</b></div>`;
    }
  } catch (error) {
    // fetch falla así cuando la API está caída o el navegador bloquea la llamada (CORS)
    resultado.innerHTML = `<div class="error"><b>No se pudo conectar con la API.</b><br>
      Puede estar apagada o haber un problema de CORS.</div>`;
    console.error(error);
  } finally {
    boton.disabled = false;
    boton.textContent = "Estimar costo";
  }
});