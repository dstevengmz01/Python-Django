function generoagregar() {
  document.addEventListener('DOMContentLoaded', function () {
  const formularioGenero = document.getElementById('form-genero');
  if (formularioGenero) {
    formularioGenero.addEventListener('submit', function () {
      alert('¡Género agregado con éxito!');
    });
  }
});
}
generoagregar();

function peliculaagregar() {
 document.addEventListener('DOMContentLoaded', function () {
  const formularioPelicula = document.getElementById('agregar_pelicula');
  if (formularioPelicula) {
    formularioPelicula.addEventListener('submit', function () {
      alert('Pelicula agregada con éxito!');
    });
  }
});
}
peliculaagregar();