from flask import Flask, redirect, render_template, request, send_file, url_for
from clases import Estudiante, Becado
from funciones import generar_reporte

# Crear la aplicación Flask
app = Flask(__name__)

# Lista para almacenar estudiantes (en lugar de leer de un archivo CSV por ahora)
estudiantes = []

@app.route('/')
def index():
    aprobados = sum(1 for estudiante in estudiantes if estudiante.es_aprobado())
    desaprobados = len(estudiantes) - aprobados  # Los desaprobados son el total menos los aprobados
    return render_template('index.html', estudiantes=estudiantes,  estudiante=None, aprobados=aprobados, desaprobados=desaprobados)

@app.route('/registrar', methods=['POST'])
def registrar_estudiante():
    # Esta ruta registra un nuevo estudiante (la lógica viene del formulario)
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    carrera = request.form['carrera']
    notas = [float(request.form['nota1']), float(request.form['nota2']), float(request.form['nota3'])]
    beca = request.form.get('beca') == 'si'  # Verifica si tiene beca (Sí o No)
    tipo_beca = request.form.get('tipo_beca', '')
    
    if not Estudiante.validar_notas(notas):
        return redirect(url_for('index', error_notas='true'))

    # Crear un objeto Estudiante o Becado
    if beca:
        tipo_beca = request.form['tipo_beca']
        estudiante = Becado(nombre, edad, carrera, notas, beca, tipo_beca)
    else:
        estudiante = Estudiante(nombre, edad, carrera, notas, beca)
    
    estudiantes.append(estudiante)
    
    # Redirigir al inicio para ver la lista actualizada
    return redirect(url_for('index', registrar_estudiante='true'))

@app.route('/eliminar/<int:estudiante_id>')
def eliminar_estudiante(estudiante_id):
    global estudiantes
    # Filtrar la lista de estudiantes para eliminar el estudiante con el ID dado
    estudiantes = [e for e in estudiantes if e.id != estudiante_id]
    return redirect(url_for('index', eliminar_estudiante='true'))

@app.route('/editar/<int:estudiante_id>', methods=['GET', 'POST'])
def editar_estudiante(estudiante_id):
    aprobados = sum(1 for estudiante in estudiantes if estudiante.es_aprobado())
    desaprobados = len(estudiantes) - aprobados  # Los desaprobados son el total menos los aprobados
    print("Estudiantes existentes:", [e.id for e in estudiantes])
    estudiante = next((e for e in estudiantes if e.id == estudiante_id), None)
    if not estudiante:
        return "Estudiante no encontrado", 404
    
    if request.method == 'POST':
        # Actualizar los datos del estudiante
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        carrera = request.form['carrera']
        notas = [float(request.form['nota1']), float(request.form['nota2']), float(request.form['nota3'])]
        beca = request.form.get('beca') == 'si'
        tipo_beca = request.form.get('tipo_beca', '')
        
        if not Estudiante.validar_notas(notas):
            return redirect(url_for('index', estudiante_id=estudiante.id, error_notas='true'))

        estudiante.nombre = nombre
        estudiante.edad = edad
        estudiante.carrera = carrera
        estudiante.notas = notas
        estudiante.beca = beca
        if beca:
            estudiante.tipo_beca = tipo_beca
        else:
            estudiante.tipo_beca = ''
        return redirect(url_for('index', editar_estudiante='true'))
    
    return render_template('index.html', estudiantes=estudiantes, estudiante=estudiante, aprobados=aprobados, desaprobados=desaprobados)

@app.route('/descargar_reporte')
def descargar_reporte():
    # Generar el reporte utilizando la función de funciones.py
    df, _, _, _, _ = generar_reporte(estudiantes)
    
    # Guardar el reporte como un archivo CSV
    file_path = 'estudiantes_reporte.csv'
    df.to_csv(file_path, index=False)
    
    # Enviar el archivo CSV al usuario para que lo descargue
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
