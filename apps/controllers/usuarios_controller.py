from flask import Blueprint, render_template, request, redirect, url_for
from apps.models.usuario import Usuario

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/')
def index():
    # Lógica para obtener y mostrar los usuarios desde la base de datos
    usuarios = Usuario.obtener_todos()
    return render_template('index.html', usuarios=usuarios)

@usuarios_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        Usuario.crear(nombre, email)
        return redirect(url_for('usuarios.index'))
    return render_template('crear.html')

# Agrega más rutas según sea necesario
