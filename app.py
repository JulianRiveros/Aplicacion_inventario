import Base_datos_usuarios
import getpass
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'la_grieta'  # Clave secreta para sesiones


# Ruta para el formulario de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    mensaje = session.pop('mensaje_registro', None)  # Obtener el mensaje de la sesión
    ##mensaje = ''
    if request.method == 'POST':
        nombre_usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        inicio_sesion = Base_datos_usuarios.iniciar_sesion(nombre_usuario, contraseña, usuarios)
        if inicio_sesion:
            return f'Bienvenido, {nombre_usuario}!'
            
        ##if usuario in USUARIOS and USUARIOS[usuario] == contraseña:
            ##return f'Bienvenido, {usuario}!'
        else:
            mensaje = 'Credenciales incorrectas. Inténtalo de nuevo.'
    return render_template('login.html', mensaje=mensaje)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    mensaje = ''
    if request.method == 'POST':
        nombre_usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        # Verificar si el usuario ya existe
        validacion_registro = Base_datos_usuarios.registrar_usuario(nombre_usuario, contraseña, usuarios)
        if validacion_registro:
            ##return f'Usuario registrado correctamente. Puedes iniciar sesión ahora, {nombre_usuario}!'
            ##mensaje = 'Usuario registrado exitosamente.'
            session['mensaje_registro'] = 'Usuario registrado exitosamente.'
            return redirect(url_for('login', mensaje=mensaje))  # Pasar el mensaje como argumento a la URL
        ##if usuario in USUARIOS:
        ##    
        else:
            mensaje = 'El usuario ya existe. Por favor, elige otro nombre de usuario.'
            ##return f'Usuario registrado correctamente. Puedes iniciar sesión ahora, {usuario}!'
    return render_template('registro.html', mensaje=mensaje)


if __name__ == '__main__':
    Base_datos_usuarios.crear_conexion_base_datos()
    usuarios = Base_datos_usuarios.coleccion_usuarios()
    
    app.run(debug=True)
