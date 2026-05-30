from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- Datos del estudio ---
SERVICIOS = [
    {
        "icono": "ti-sparkles",
        "nombre": "Manicure clásico",
        "descripcion": "Limpieza, corte, limado, Uña decorada y esmaltado tradicional con los mejores productos.",
        "precio": "$50.000",
        "duracion": "50 min",
    },
    {
        "icono": "ti-diamond",
        "nombre": "Semipermanente",
        "descripcion": "Esmalte de larga duración con acabado profesional. Dura hasta 3 semanas.",
        "precio": "$65.000",
        "duracion": "60 min",
    },
    {
        "icono": "ti-wand",
        "nombre": "Manicura de Lujo",
        "descripcion": "Diseños personalizados con decoraciones, foils, piedras y técnicas especiales.",
        "precio": "$80.000",
        "duracion": "90 min",
    },
    {
        "icono": "ti-snowflake",
        "nombre": "Acrílico / Gel",
        "descripcion": "Extensión de uñas con acrílico o gel para mayor longitud y resistencia.",
        "precio": "$120.000",
        "duracion": "120 min",
    },
    {
        "icono": "ti-heart",
        "nombre": "Manicure + Pedicure",
        "descripcion": "Paquete completo para manos y pies con exfoliación e hidratación.",
        "precio": "$80.000",
        "duracion": "100 min",
    },
    {
        "icono": "ti-star",
        "nombre": "Retiro y esmaltado",
        "descripcion": "Retiro seguro del esmalte anterior y aplicación de nuevo color a elección.",
        "precio": "$30.000",
        "duracion": "30 min",
    },
]

GALERIA = [
    {"nombre": "French Rose - Rosa Frances",   "clase": "g1", "size": "tall"},
    {"nombre": "Golden Designs - Diseños dorados",   "clase": "g2", "size": "normal"},
    {"nombre": "Effects And Encapsulation - Efectos y Encapsulados", "clase": "g3", "size": "normal"},
    {"nombre": "Chrome Night - Noche Cromo",  "clase": "g4", "size": "normal"},
    {"nombre": "French Manicure With Blush - Manicura Francesa Con Rubor",  "clase": "g5", "size": "normal"},
]

CONTACTO = {
    "direccion": ", Soacha, Cundinamarca",
    "horario": "Lun–Vie 9:00am–7:00pm · Sáb 9:00am–5:00pm · Disponibilidad segun la Agenda",  
    "whatsapp": "",
    "instagram": "@",
    "tiktok": "@",
}

# Reservas guardadas en memoria (en producción usarías una base de datos)
reservas = []


@app.route("/")
def index():
    return render_template(
        "index.html",
        servicios=SERVICIOS,
        galeria=GALERIA,
        contacto=CONTACTO,
    )


@app.route("/reservar", methods=["POST"])
def reservar():
    datos = request.get_json()
    campos = ["nombre", "telefono", "email", "servicio", "fecha"]
    for campo in campos:
        if not datos.get(campo):
            return jsonify({"ok": False, "mensaje": f"El campo '{campo}' es obligatorio."}), 400

    reservas.append(datos)
    print(f"[Nueva reserva] {datos['nombre']} — {datos['servicio']} el {datos['fecha']}")
    return jsonify({"ok": True, "mensaje": f"¡Cita solicitada, {datos['nombre']}! Te contactaremos pronto."})


if __name__ == "__main__":
    app.run(debug=True)
