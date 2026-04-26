from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Hola, Priscila! Esta es la página de inicio."

# Ruta con nombre (como la del pizarrón)
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'Hola, {nombre}!'

# Ruta para el taller devolviendo datos (JSON)
@app.route('/api/taller')
def api_data():
    data = {
        'taller': 'Mecánica Pro',
        'ubicación': 'Mendoza',
        'estado': 'Abierto'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)