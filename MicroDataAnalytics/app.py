# app.py

import boto3
from flask import Flask, jsonify, request

# ============================================
# Configuración de AWS
# ============================================
# Reemplaza 'tu-bucket-resultados-athena' con el nombre que le des a tu bucket.
REGION = 'us-east-1	'
S3_OUTPUT_BUCKET = 's3://analytics/results/' 
# Ojo: la ruta termina con 'results/' para organizar mejor tus resultados
DATABASE_NAME = 'ecommerce_analytics_db' # El nombre de la base de datos de Glue
ATHENA_CLIENT = boto3.client('athena', region_name=REGION)

app = Flask(__name__)

# Aquí se definirán los endpoints de tu API REST, como por ejemplo:
# @app.route('/api/ventas/top-productos', methods=['GET'])
# def get_top_products():
#     ... tu lógica de consulta a Athena ...


def run_athena_query(query):
    try:
        # 1. Ejecutar la consulta en Athena
        response = ATHENA_CLIENT.start_query_execution(
            QueryString=query,
            QueryExecutionContext={
                'Database': DATABASE_NAME
            },
            ResultConfiguration={
                'OutputLocation': S3_OUTPUT_BUCKET
            }
        )
        query_execution_id = response['QueryExecutionId']

        # 2. Esperar a que la consulta termine (polling)
        while True:
            status = ATHENA_CLIENT.get_query_execution(QueryExecutionId=query_execution_id)['QueryExecution']['Status']['State']
            if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
                break
            time.sleep(1) # Espera 1 segundo antes de volver a chequear

        if status == 'SUCCEEDED':
            # 3. Obtener y procesar los resultados
            result = ATHENA_CLIENT.get_query_results(QueryExecutionId=query_execution_id)
            
            # Procesar las filas de resultados (la primera fila es la cabecera)
            columns = [col['VarCharValue'] for col in result['ResultSet']['Rows'][0]['Data']]
            data = []
            for row in result['ResultSet']['Rows'][1:]:
                # Crea un diccionario para cada fila
                item = {columns[i]: row['Data'][i]['VarCharValue'] for i in range(len(columns))}
                data.append(item)
            
            return data
        else:
            error_message = ATHENA_CLIENT.get_query_execution(QueryExecutionId=query_execution_id)['QueryExecution']['Status'].get('StateChangeReason', 'Error desconocido')
            return {"error": f"Consulta fallida: {error_message}"}, 500

    except Exception as e:
        return {"error": str(e)}, 500

# ============================================
# ENDPOINT DE API REST
# ============================================
@app.route('/api/analytics/top-productos', methods=['GET'])
def get_top_products():
    """
    Consulta a Athena para obtener los 10 productos más vendidos
    """
    # Esta es una consulta de ejemplo que une las tablas de productos y pedidos 
    # (¡Asegúrate de que los nombres de las tablas coincidan con el catálogo de Glue!)
    query = f"""
    SELECT
        T2.product_name,
        SUM(CAST(T1.quantity AS INTEGER)) AS total_sold
    FROM
        order_items_table AS T1,
        products_table AS T2
    WHERE
        T1.product_id = T2.product_id
    GROUP BY
        T2.product_name
    ORDER BY
        total_sold DESC
    LIMIT 10
    """
    
    results, status_code = run_athena_query(query)

    if status_code != 500:
        return jsonify({
            "status": "success",
            "data": results,
            "metadata": "10 productos más vendidos (datos de S3/Athena)"
        })
    else:
        # En caso de error, devuelve el error y el código HTTP 500
        return jsonify(results), status_code

if __name__ == '__main__':
    # Flask corriendo en el puerto 5000 (el puerto que expondremos en Docker)
    app.run(host='0.0.0.0', port=5000)
