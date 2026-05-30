async function enviarReserva() {
  const msg = document.getElementById('form-msg');
  const btn = document.querySelector('.btn-book');

  const datos = {
    nombre:   document.getElementById('nombre').value.trim(),
    telefono: document.getElementById('telefono').value.trim(),
    email:    document.getElementById('email').value.trim(),
    servicio: document.getElementById('servicio').value,
    fecha:    document.getElementById('fecha').value,
    notas:    document.getElementById('notas').value.trim(),
  };

  msg.className = 'form-msg hidden';

  try {
    btn.disabled = true;
    btn.textContent = 'Enviando...';

    const res = await fetch('/reservar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(datos),
    });

    const json = await res.json();
    msg.textContent = json.mensaje;
    msg.className = 'form-msg ' + (json.ok ? 'success' : 'error');

    if (json.ok) {
      ['nombre', 'telefono', 'email', 'fecha', 'notas'].forEach(id => {
        document.getElementById(id).value = '';
      });
    }
  } catch (e) {
    msg.textContent = 'Error de conexión. Intenta de nuevo.';
    msg.className = 'form-msg error';
  } finally {
    btn.disabled = false;
    btn.innerHTML = 'Solicitar cita <i class="ti ti-arrow-right"></i>';
  }
}
