from flask import Flask, request, redirect, url_for, session, render_template_string

app = Flask(__name__)
app.secret_key = "clave_super_secreta_2026"

MAX_INTENTOS = 3
USUARIO_ADMIN = "admin"
CONTRASENA_ADMIN = "Admin2026"


BASE_HTML = """
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ titulo }}</title>
    <style>
        * { box-sizing: border-box; font-family: Arial, sans-serif; }
        body {
            margin: 0;
            background: #f4f6f9;
            color: #222;
        }
        .navbar {
            background: #1f2937;
            color: white;
            padding: 16px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .navbar a {
            color: white;
            text-decoration: none;
            margin-left: 16px;
            font-weight: bold;
        }
        .container {
            max-width: 1100px;
            margin: 30px auto;
            padding: 0 20px;
        }
        .card {
            background: white;
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.08);
            margin-bottom: 20px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 20px;
        }
        h1, h2, h3 { margin-top: 0; }
        input, select {
            width: 100%;
            padding: 12px;
            margin-top: 6px;
            margin-bottom: 16px;
            border: 1px solid #ccc;
            border-radius: 10px;
        }
        button, .btn {
            display: inline-block;
            background: #2563eb;
            color: white;
            border: none;
            padding: 12px 18px;
            border-radius: 10px;
            cursor: pointer;
            text-decoration: none;
            font-weight: bold;
        }
        .btn-secondary {
            background: #6b7280;
        }
        .btn-danger {
            background: #dc2626;
        }
        .msg {
            padding: 12px 14px;
            border-radius: 10px;
            margin-bottom: 16px;
        }
        .success { background: #dcfce7; color: #166534; }
        .error { background: #fee2e2; color: #991b1b; }
        .info { background: #dbeafe; color: #1d4ed8; }
        .warning { background: #fef3c7; color: #92400e; }
        ul { padding-left: 20px; }
        .actions {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        .muted {
            color: #6b7280;
        }
    </style>
</head>
<body>
    <div class="navbar">
        <div><strong>Sistema Flask</strong></div>
        <div>
            {% if session.get("auth") %}
                <a href="{{ url_for('menu') }}">Menú</a>
                <a href="{{ url_for('logout') }}">Cerrar sesión</a>
            {% endif %}
        </div>
    </div>

    <div class="container">
        {{ contenido|safe }}
    </div>
</body>
</html>
"""


def render_page(titulo: str, contenido: str):
    return render_template_string(
        BASE_HTML,
        titulo=titulo,
        contenido=contenido,
        session=session
    )


def login_requerido():
    return session.get("auth", False)


@app.route("/", methods=["GET"])
def inicio():
    if login_requerido():
        return redirect(url_for("menu"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if "intentos" not in session:
        session["intentos"] = 0

    mensaje = ""
    clase = ""

    if request.method == "POST":
        if session["intentos"] >= MAX_INTENTOS:
            mensaje = "Intentos caducados, vuelve a intentarlo más tarde."
            clase = "error"
        else:
            usuario_ing = request.form.get("usuario", "").strip()
            contrasena_ing = request.form.get("contrasena", "").strip()

            sin_espacios = (" " not in usuario_ing) and (" " not in contrasena_ing)
            usuario_alnum = usuario_ing.isalnum()
            contrasena_alnum = contrasena_ing.isalnum()
            largo_ok = len(contrasena_ing) >= 8
            numero_ok = any(c.isdigit() for c in contrasena_ing)
            letra_ok = any(c.isalpha() for c in contrasena_ing)

            errores = []
            if not sin_espacios:
                errores.append("No se permiten espacios.")
            if not usuario_alnum:
                errores.append("Usuario: solo se permite alfanumérico.")
            if not contrasena_alnum:
                errores.append("Contraseña: solo se permite alfanumérico.")
            if not largo_ok:
                errores.append("La contraseña debe tener mínimo 8 caracteres.")
            if not numero_ok:
                errores.append("La contraseña debe tener al menos un número.")
            if not letra_ok:
                errores.append("La contraseña debe contener al menos una letra.")

            if errores:
                session["intentos"] += 1
                mensaje = "<br>".join(errores) + f"<br><br>Intento {session['intentos']}/{MAX_INTENTOS}"
                clase = "error"
            else:
                if usuario_ing == USUARIO_ADMIN and contrasena_ing == CONTRASENA_ADMIN:
                    session["auth"] = True
                    session["intentos"] = 0
                    return redirect(url_for("menu"))
                else:
                    session["intentos"] += 1
                    if usuario_ing != USUARIO_ADMIN:
                        mensaje = "El usuario es incorrecto."
                    else:
                        mensaje = "La contraseña es incorrecta."
                    mensaje += f"<br><br>Intento {session['intentos']}/{MAX_INTENTOS}"
                    clase = "error"

    bloqueado = session.get("intentos", 0) >= MAX_INTENTOS

    contenido = f"""
    <div class="card" style="max-width:520px; margin:auto;">
        <h2>Acceso al sistema</h2>
        <p class="muted">Usuario: <strong>admin</strong> | Contraseña: <strong>Admin2026</strong></p>
        {"<div class='msg " + clase + "'>" + mensaje + "</div>" if mensaje else ""}
        <form method="post">
            <label>Usuario</label>
            <input type="text" name="usuario" placeholder="Ingresa tu usuario" {"disabled" if bloqueado else ""}>

            <label>Contraseña</label>
            <input type="password" name="contrasena" placeholder="Ingresa tu contraseña" {"disabled" if bloqueado else ""}>

            <button type="submit" {"disabled" if bloqueado else ""}>Ingresar</button>
        </form>
    </div>
    """
    return render_page("Login", contenido)


@app.route("/menu")
def menu():
    if not login_requerido():
        return redirect(url_for("login"))

    contenido = """
    <div class="card">
        <h2>Panel principal</h2>
        <p>Selecciona una opción.</p>
    </div>

    <div class="grid">
        <div class="card">
            <h3>🔢 Clasificar número</h3>
            <p>Determina si un número es positivo, negativo o cero, y si es par o impar.</p>
            <a class="btn" href="/clasificar">Entrar</a>
        </div>

        <div class="card">
            <h3>👤 Categoría de edad y permisos</h3>
            <p>Evalúa etapa de vida, acceso premium y permiso para conducir.</p>
            <a class="btn" href="/categoria">Entrar</a>
        </div>

        <div class="card">
            <h3>💰 Calcular tarifa final</h3>
            <p>Aplica recargos y descuentos según edad, día, membresía y método de pago.</p>
            <a class="btn" href="/tarifa">Entrar</a>
        </div>

    </div>
    """
    return render_page("Menú", contenido)


@app.route("/clasificar", methods=["GET", "POST"])
def clasificar():
    if not login_requerido():
        return redirect(url_for("login"))

    resultado = ""

    if request.method == "POST":
        entrada = request.form.get("numero", "").strip()

        try:
            n = int(entrada)
            mensajes = []

            if n > 0:
                mensajes.append("El número es positivo.")
            elif n < 0:
                mensajes.append("El número es negativo.")
            else:
                mensajes.append("El número es 0.")

            if n != 0:
                if n % 2 == 0:
                    mensajes.append("El número es par.")
                else:
                    mensajes.append("El número es impar.")

            resultado = "<div class='msg success'><ul>" + "".join(f"<li>{m}</li>" for m in mensajes) + "</ul></div>"
        except ValueError:
            resultado = "<div class='msg error'>Entrada inválida. Ingresa un número entero.</div>"

    contenido = f"""
    <div class="card">
        <h2>Clasificar número</h2>
        <form method="post">
            <label>Ingresa un número entero</label>
            <input type="text" name="numero" placeholder="Ejemplo: -7">
            <div class="actions">
                <button type="submit">Clasificar</button>
                <a class="btn btn-secondary" href="/menu">Volver</a>
            </div>
        </form>
        <br>
        {resultado}
    </div>
    """
    return render_page("Clasificar número", contenido)


@app.route("/categoria", methods=["GET", "POST"])
def categoria():
    if not login_requerido():
        return redirect(url_for("login"))

    resultado = ""

    if request.method == "POST":
        edad_txt = request.form.get("edad", "").strip()
        ine = request.form.get("ine", "").strip().lower()
        licencia = request.form.get("licencia", "").strip().lower()

        errores = []

        try:
            edad = int(edad_txt)
            if not (0 <= edad <= 120):
                errores.append("Ingresa una edad válida entre 0 y 120.")
        except ValueError:
            errores.append("Ingresa una edad válida.")

        if ine not in ("s", "n"):
            errores.append("Ingresa una opción válida en INE.")
        if licencia not in ("s", "n"):
            errores.append("Ingresa una opción válida en Licencia.")

        if errores:
            resultado = "<div class='msg error'><ul>" + "".join(f"<li>{e}</li>" for e in errores) + "</ul></div>"
        else:
            mensajes = ["Datos correctos ✅"]

            if edad <= 12:
                mensajes.append("Estás en una etapa de niñez, no puedes ingresar.")
            elif edad <= 17:
                mensajes.append("Estás en adolescencia: puedes registrarte, pero no comprar sin tutor.")
            elif edad <= 64:
                mensajes.append("Estás en adultez: puedes comprar sin tutor.")
            else:
                mensajes.append("Estás en adulto mayor: tienes derecho a tu compra legal.")

            if ine == "s" and edad >= 21:
                mensajes.append("Acceso al servicio premium.")
            else:
                mensajes.append("No puedes realizar la compra.")

            if licencia == "s" and edad >= 18:
                mensajes.append("Sí puedes conducir.")
            else:
                mensajes.append("No puedes conducir (sin licencia).")

            resultado = "<div class='msg success'><ul>" + "".join(f"<li>{m}</li>" for m in mensajes) + "</ul></div>"

    contenido = f"""
    <div class="card">
        <h2>Categoría de edad y permisos</h2>
        <form method="post">
            <label>Edad</label>
            <input type="number" name="edad" min="0" max="120" placeholder="Ejemplo: 25">

            <label>¿Cuentas con identificación oficial?</label>
            <select name="ine">
                <option value="">Selecciona</option>
                <option value="s">Sí</option>
                <option value="n">No</option>
            </select>

            <label>¿Cuentas con licencia de conducir?</label>
            <select name="licencia">
                <option value="">Selecciona</option>
                <option value="s">Sí</option>
                <option value="n">No</option>
            </select>

            <div class="actions">
                <button type="submit">Evaluar</button>
                <a class="btn btn-secondary" href="/menu">Volver</a>
            </div>
        </form>
        <br>
        {resultado}
    </div>
    """
    return render_page("Categoría", contenido)


@app.route("/tarifa", methods=["GET", "POST"])
def tarifa():
    if not login_requerido():
        return redirect(url_for("login"))

    resultado = ""

    if request.method == "POST":
        servicio = 200.0

        edad_txt = request.form.get("edad", "").strip()
        dia = request.form.get("dia", "").strip()
        estudiante = request.form.get("estudiante", "").strip().lower()
        miembro = request.form.get("miembro", "").strip().lower()
        metodo = request.form.get("metodo", "").strip().lower()

        errores = []

        try:
            edad = int(edad_txt)
            if not (0 <= edad <= 120):
                errores.append("Ingresa una edad válida entre 0 y 120.")
        except ValueError:
            errores.append("Ingresa una edad válida.")

        if dia not in ("1", "2", "3", "4", "5", "6", "7"):
            errores.append("Ingresa una opción válida en día.")
        if estudiante not in ("s", "n"):
            errores.append("Ingresa una opción válida en estudiante.")
        if miembro not in ("s", "n"):
            errores.append("Ingresa una opción válida en miembro.")
        if metodo not in ("e", "t"):
            errores.append("Ingresa un método de pago válido.")

        if errores:
            resultado = "<div class='msg error'><ul>" + "".join(f"<li>{e}</li>" for e in errores) + "</ul></div>"
        else:
            mensajes = []

            if dia in ("6", "7"):
                servicio *= 1.10
                mensajes.append("Se aplicó un recargo del 10% por fin de semana.")

            servicio_base = servicio
            porcentaje = 0

            if edad <= 12:
                porcentaje += 50
            elif edad <= 17:
                porcentaje += 20
            elif edad <= 64:
                porcentaje += 0
            else:
                porcentaje += 30

            if estudiante == "s" and edad >= 13:
                porcentaje += 15

            if miembro == "s":
                porcentaje += 10

            if metodo == "e":
                porcentaje += 5

            if porcentaje > 60:
                mensajes.append(f"Tu descuento era de {porcentaje}% pero el máximo es 60%.")
                porcentaje = 60

            descuento = servicio_base * (porcentaje / 100)
            total = servicio_base - descuento

            mensajes.append(f"Servicio base (con recargo si aplica): {servicio_base:.2f}")
            mensajes.append(f"Descuento aplicado: {porcentaje}%")
            mensajes.append(f"Monto de descuento: {descuento:.2f}")
            mensajes.append(f"TOTAL A PAGAR: {total:.2f}")

            resultado = "<div class='msg success'><ul>" + "".join(f"<li>{m}</li>" for m in mensajes) + "</ul></div>"

    contenido = f"""
    <div class="card">
        <h2>Calcular tarifa final</h2>
        <form method="post">
            <label>Edad</label>
            <input type="number" name="edad" min="0" max="120" placeholder="Ejemplo: 30">

            <label>Día de la semana</label>
            <select name="dia">
                <option value="">Selecciona</option>
                <option value="1">1 - Lunes</option>
                <option value="2">2 - Martes</option>
                <option value="3">3 - Miércoles</option>
                <option value="4">4 - Jueves</option>
                <option value="5">5 - Viernes</option>
                <option value="6">6 - Sábado</option>
                <option value="7">7 - Domingo</option>
            </select>

            <label>¿Eres estudiante?</label>
            <select name="estudiante">
                <option value="">Selecciona</option>
                <option value="s">Sí</option>
                <option value="n">No</option>
            </select>

            <label>¿Eres miembro?</label>
            <select name="miembro">
                <option value="">Selecciona</option>
                <option value="s">Sí</option>
                <option value="n">No</option>
            </select>

            <label>Método de pago</label>
            <select name="metodo">
                <option value="">Selecciona</option>
                <option value="e">Efectivo</option>
                <option value="t">Tarjeta</option>
            </select>

            <div class="actions">
                <button type="submit">Calcular</button>
                <a class="btn btn-secondary" href="/menu">Volver</a>
            </div>
        </form>
        <br>
        {resultado}
    </div>
    """
    return render_page("Tarifa final", contenido)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
