import random # Importante para generar los precios aleatorios
from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = "retail_flow_2026"

# Base de datos de productos fija
productos = {
    "127846005981": {"nombre": "Leche Entera Premium 1L", "precio": 1.80, "cat": "LÁCTEOS"},
    "456": {"nombre": "Manzana Gala Orgánica", "precio": 3.50, "cat": "FRUTAS"},
    "789": {"nombre": "Salmón Fresco Noruego", "precio": 18.90, "cat": "CARNES"},
    "101": {"nombre": "Pan Artesanal Masa Madre", "precio": 4.25, "cat": "PANADERÍA"},
    "202": {"nombre": "Detergente Líquido Bio 2L", "precio": 8.50, "cat": "LIMPIEZA"}
}

@app.route('/')
def index():
    return redirect(url_for('escaneo'))

@app.route('/escaneo')
def escaneo():
    return render_template('escaneo.html')

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html', productos=productos)

@app.route('/agregar/<codigo>')
def agregar(codigo):
    if 'carrito' not in session:
        session['carrito'] = []
    
    # LÓGICA DE DETECCIÓN E INVENCIÓN
    if codigo in productos:
        # Si el producto existe, usamos los datos reales
        producto_a_agregar = productos[codigo]
    else:
        # Si NO existe, inventamos un precio entre $10.00 y $60.00
        # Usamos los últimos 4 dígitos del código para que el nombre varíe
        precio_random = round(random.uniform(10.0, 60.0), 2)
        producto_a_agregar = {
            "nombre": f"Producto Misterioso ({codigo[-4:]})", 
            "precio": precio_random, 
            "cat": "GENÉRICO"
        }
        print(f"DEBUG: Escaneado código desconocido [{codigo}]. Generando precio: ${precio_random}")
    
    # Agregamos al carrito (sea real o inventado)
    session['carrito'].append(producto_a_agregar)
    session.modified = True
    
    return redirect(url_for('carrito'))

@app.route('/carrito')
def carrito():
    items = session.get('carrito', [])
    subtotal = sum(item['precio'] for item in items)
    
    # Cálculo de impuestos (IVA 16%)
    valor_iva = subtotal * 0.16 
    total = subtotal + valor_iva
    
    return render_template('carrito.html', 
                           items=items, 
                           subtotal=subtotal, 
                           impuestos=valor_iva, 
                           iva=valor_iva, 
                           total=total)

@app.route('/exito')
def exito():
    items = session.get('carrito', [])
    
    if not items:
        return redirect(url_for('escaneo'))
        
    subtotal = sum(item['precio'] for item in items)
    valor_iva = subtotal * 0.16
    total = subtotal + valor_iva

    # Vaciamos el carrito porque la transacción terminó
    session.pop('carrito', None)

    return render_template('exito.html', 
                           items=items, 
                           subtotal=subtotal, 
                           iva=valor_iva, 
                           total=total)

if __name__ == '__main__':
    # host='0.0.0.0' para que el iPhone pueda entrar vía Ngrok o IP local
    app.run(debug=True, host='0.0.0.0', port=5000)