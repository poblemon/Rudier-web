from flask import Flask, request, jsonify, send_file
import sqlite3
import os

app = Flask(__name__)

# Crear base de datos si no existe
def crear_tabla():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            correo TEXT,
            mensaje TEXT
        )
    """)
    conn.commit()
    conn.close()

crear_tabla()

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/favicon.ico")
def favicon():
    return send_file("img/favicon.ico") if os.path.exists("img/favicon.ico") else ("", 404)

@app.route("/productos")
def productos():
    return send_file("productos.html")

@app.route("/contacto")
def contacto():
    return send_file("contacto.html")

@app.route("/nosotros")
def nosotros():
    return send_file("nosotros.html")

@app.route("/styles/<path:filename>")
def styles(filename):
    if filename in ["common.css", "style.css", "producto.css", "nosotros.css", "contacto.css", "carrusel.css"]:
        return send_file(f"styles/{filename}")
    return ("Archivo no encontrado", 404)

@app.route("/img/<path:filename>")
def img(filename):
    return send_file(f"img/{filename}")

@app.route("/enviar", methods=["POST"])
def enviar():
    nombre = request.form.get("nombre")
    correo = request.form.get("correo")
    mensaje = request.form.get("mensaje")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contactos (nombre, correo, mensaje) VALUES (?, ?, ?)", 
                   (nombre, correo, mensaje))
    conn.commit()
    conn.close()

    return jsonify({"status": "ok", "mensaje": "Mensaje recibido correctamente"}), 200

if __name__ == "__main__":
    app.run(debug=True)
