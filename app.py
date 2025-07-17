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
    return render_template('index.html', estudiantes=estudiantes, aprobados=aprobados, desaprobados=desaprobados)

@app.route('/registrar', methods=['POST'])
def registrar_estudiante():
    # Esta ruta registra un nuevo estudiante (la lógica viene del formulario)
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    carrera = request.form['carrera']
    notas = [float(request.form['nota1']), float(request.form['nota2']), float(request.form['nota3'])]
    beca = request.form.get('beca') == 'si'  # Verifica si tiene beca (Sí o No)
    tipo_beca = request.form.get('tipo_beca', '')
    
    # Crear un objeto Estudiante o Becado
    if beca:
        tipo_beca = request.form['tipo_beca']
        estudiante = Becado(nombre, edad, carrera, notas, beca, tipo_beca)
    else:
        estudiante = Estudiante(nombre, edad, carrera, notas, beca)
    
    estudiantes.append(estudiante)
    
    # Redirigir al inicio para ver la lista actualizada
    return redirect(url_for('index'))


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
