"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os

def pregunta_01():
     # Cargar datos
    file_path = 'files/input/solicitudes_de_credito.csv'  # Ruta del archivo CSV original.
    data = pd.read_csv(file_path, sep=';')  # Lee el archivo CSV, usando el separador ';'.
        # Limpieza inicial del DataFrame
    data.drop(['Unnamed: 0'], axis=1, inplace=True)  # Elimina la columna no necesaria 'Unnamed: 0'.
    data.dropna(inplace=True)  # Elimina las filas con valores nulos.
    data.drop_duplicates(inplace=True)  # Elimina las filas duplicadas.

    # Arreglo de la columna 'fecha_de_beneficio'
    data[['día', 'mes', 'año']] = data['fecha_de_beneficio'].str.split('/', expand=True)  # Divide la columna 'fecha_de_beneficio' en tres nuevas columnas: 'día', 'mes', 'año'.
    data.loc[data['año'].str.len() < 4, ['día', 'año']] = data.loc[data['año'].str.len() < 4, ['año', 'día']].values  # Reordena los valores si el año tiene menos de 4 dígitos (asumiendo formato incorrecto).
    data['fecha_de_beneficio'] = data['año'] + '-' + data['mes'] + '-' + data['día']  # Reconstruye la columna 'fecha_de_beneficio' en formato 'YYYY-MM-DD'.
    data.drop(['día', 'mes', 'año'], axis=1, inplace=True)  # Elimina las columnas temporales 'día', 'mes' y 'año'.

    # Limpieza de columnas de texto
    object_columns = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito']  # Lista de columnas de tipo texto que requieren limpieza.
    data[object_columns] = data[object_columns].apply(lambda x: x.str.lower().replace(['-', '_'], ' ', regex=True).str.strip())  # Convierte a minúsculas, reemplaza caracteres específicos y elimina espacios adicionales.
    data['barrio'] = data['barrio'].str.lower().replace(['-', '_'], ' ', regex=True)  # Limpia la columna 'barrio' de manera similar.

    # Limpieza de la columna 'monto_del_credito'
    data['monto_del_credito'] = data['monto_del_credito'].str.replace("[$, ]", "", regex=True).str.strip()  # Elimina caracteres no numéricos como '$', ',' y espacios.
    data['monto_del_credito'] = pd.to_numeric(data['monto_del_credito'], errors='coerce')  # Convierte la columna a tipo numérico, manejando valores no convertibles como NaN.
    data['monto_del_credito'] = data['monto_del_credito'].fillna(0).astype(int)  # Rellena valores NaN con 0 y convierte a entero.
    data['monto_del_credito'] = data['monto_del_credito'].astype(str).str.replace('.00', '')  # Convierte de nuevo a texto y elimina '.00' de valores flotantes.

    # Elimina duplicados después de las transformaciones.
    data.drop_duplicates(inplace=True)

    # Crear directorio de salida si no existe
    output_dir = 'files/output'  # Define la carpeta de salida
    os.makedirs(output_dir, exist_ok=True)  # Crea la carpeta si no existe.

    # Guardar el DataFrame limpio en un nuevo archivo CSV
    output_path = f'{output_dir}/solicitudes_de_credito.csv'
    data.to_csv(output_path, sep=';', index=False)  # Guarda el DataFrame como CSV.

    return data.head()

# Llamar a la función



    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
