# funciones.py

import pandas as pd
import numpy as np

def generar_reporte(estudiantes):
    # Crear un DataFrame con los datos de los estudiantes
    data = {
        'Carrera': [e.carrera for e in estudiantes],
        'Nombre': [e.nombre for e in estudiantes],
        'Promedio': [e.calcular_promedio() for e in estudiantes],
        'Aprobado': [e.es_aprobado() for e in estudiantes],
        'Beca': [e.beca for e in estudiantes],
        'TipodeBeca': [e.tipo_beca if hasattr(e, 'tipo_beca') else '-' for e in estudiantes]
    }
    df = pd.DataFrame(data)

    # Cálculos estadísticos
    promedio_grupal = np.mean(df['Promedio'])
    nota_maxima = np.max(df['Promedio'])
    nota_minima = np.min(df['Promedio'])
    desviacion_estandar = np.std(df['Promedio'])

    # Agregar las estadísticas como una fila adicional al DataFrame
    stats_data = {
        'Nombre': ['Promedio Grupal', 'Nota Máxima', 'Nota Mínima', 'Desviación Estándar'],
        'Promedio': [promedio_grupal, nota_maxima, nota_minima, desviacion_estandar],
        'Aprobado': ['', '', '', '']  # No es necesario calcular "Aprobado" para las estadísticas    
    }
    
    stats_df = pd.DataFrame(stats_data)
    
    # Concatenar las estadísticas al final del DataFrame original
    df = pd.concat([df, stats_df], ignore_index=True)
    
    # Exportar a CSV
    df.to_csv('estudiantes_reporte.csv', index=False)
    
    # Devolver el DataFrame y los cálculos estadísticos
    return df, promedio_grupal, nota_maxima, nota_minima, desviacion_estandar
