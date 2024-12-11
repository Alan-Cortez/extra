from flask import Blueprint, render_template, request, jsonify
from apps.models.usuario import Usuario
import pusher

# Configuración de Pusher
pusher_client = pusher.Pusher(
    app_id='1767934',
    key='ffa9ea426828188c22c1',
    secret='628348e447718a9eec1f',
    cluster='us2',
    ssl=True
)

usuarios_controller = Blueprint('usuarios', __name__)

# Ruta para renderizar la página principal
@usuarios_controller.route("/")
def index():
    return render_template("index.html")

# Crear usuario
@usuarios_controller.route("/guardar", methods=["POST"])
def guardar_usuario():
    usuario = request.form["txtUsuarioFA"]
    contrasena = request.form["txtContrasenaFA"]

    # Insertar nuevo usuario
    Usuario.crear_usuario(usuario, contrasena)

    # Disparar evento Pusher para notificar la inserción
    pusher_client.trigger("registrosTiempoReal", "registroTiempoReal", {"usuario": usuario})

    return jsonify({"status": "success", "message": "Usuario creado exitosamente"})

# Leer todos los usuarios
@usuarios_controller.route("/buscar")
def buscar_usuarios():
    usuarios = Usuario.obtener_usuarios()
    return jsonify(usuarios)

# Actualizar usuario
@usuarios_controller.route("/actualizar", methods=["POST"])
def actualizar_usuario():
    id_usuario = request.form["id_usuario"]
    usuario = request.form["txtUsuarioFA"]
    contrasena = request.form["txtContrasenaFA"]

    Usuario.actualizar_usuario(id_usuario, usuario, contrasena)

    # Disparar evento Pusher para notificar la actualización
    pusher_client.trigger("registrosTiempoReal", "registroTiempoReal", {"usuario": usuario})

    return jsonify({"status": "success", "message": "Usuario actualizado exitosamente"})

# Eliminar usuario
@usuarios_controller.route("/eliminar", methods=["POST"])
def eliminar_usuario():
    id_usuario = request.form["id_usuario"]

    Usuario.eliminar_usuario(id_usuario)

    # Disparar evento Pusher para notificar la eliminación
    pusher_client.trigger("registrosTiempoReal", "registroTiempoReal", {"id_usuario": id_usuario})

    return jsonify({"status": "success", "message": "Usuario eliminado exitosamente"})
