from flask import Flask, request, jsonify, send_file
import os
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializar Firebase
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": os.environ.get('FIREBASE_PROJECT_ID'),
    "private_key_id": os.environ.get('FIREBASE_PRIVATE_KEY_ID'),
    "private_key": os.environ.get('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
    "client_email": os.environ.get('FIREBASE_CLIENT_EMAIL'),
    "client_id": os.environ.get('FIREBASE_CLIENT_ID'),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": os.environ.get('FIREBASE_CLIENT_X509_CERT_URL')
})
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("../index.html")

@app.route("/productos")
def productos():
    return send_file("../productos.html")

@app.route("/contacto")
def contacto():
    return send_file("../contacto.html")

@app.route("/nosotros")
def nosotros():
    return send_file("../nosotros.html")

@app.route("/styles/<path:filename>")
def styles(filename):
    if filename in ["common.css", "style.css", "producto.css", "nosotros.css", "contacto.css", "carrusel.css"]:
        return send_file(f"../styles/{filename}")
    return ("Archivo no encontrado", 404)

@app.route("/img/<path:filename>")
def img(filename):
    return send_file(f"../img/{filename}")

@app.route("/enviar", methods=["POST"])
def enviar():
    nombre = request.form.get("nombre")
    correo = request.form.get("correo")
    mensaje = request.form.get("mensaje")

    # Guardar en Firebase Firestore
    doc_ref = db.collection('contactos').document()
    doc_ref.set({
        'nombre': nombre,
        'correo': correo,
        'mensaje': mensaje,
        'timestamp': firestore.SERVER_TIMESTAMP
    })

    return jsonify({"status": "ok", "mensaje": "Mensaje recibido correctamente"}), 200

# Exportar la app para Vercel
application = app
