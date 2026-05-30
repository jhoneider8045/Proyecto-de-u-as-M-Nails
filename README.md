# M & Nails — Sitio web con Flask

## Estructura del proyecto

```
M &_nails/
├── app.py                  ← Servidor Flask (lógica principal)
├── requirements.txt        ← Dependencias Python
├── templates/
│   └── index.html          ← Plantilla HTML (Jinja2)
└── static/
    ├── css/
    │   └── style.css       ← Estilos
    └── js/
        └── main.js         ← Lógica del formulario
```

## Cómo ejecutar

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecutar el servidor
```bash
python app.py
```

### 3. Abrir en el navegador
```
http://localhost:5000
```

## Personalizar

### Cambiar servicios y precios
Edita la lista `SERVICIOS` en `app.py`.

### Cambiar datos de contacto
Edita el diccionario `CONTACTO` en `app.py`.

### Guardar reservas en base de datos
Reemplaza la lista `reservas = []` por una conexión a SQLite, PostgreSQL, etc.
Ejemplo con SQLite:
```python
import sqlite3

def guardar_reserva(datos):
    con = sqlite3.connect("reservas.db")
    con.execute(
        "INSERT INTO reservas VALUES (?,?,?,?,?,?)",
        (datos['nombre'], datos['telefono'], datos['email'],
         datos['servicio'], datos['fecha'], datos['notas'])
    )
    con.commit()
    con.close()
```
