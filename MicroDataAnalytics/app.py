# app.py

import boto3
from flask import Flask, jsonify, request

# ============================================
# Configuración de AWS
# ============================================
# Reemplaza 'tu_region_aws' con la región que estés usando (ej. 'us-east-1').
# Reemplaza 'tu-bucket-resultados-athena' con el nombre que le des a tu bucket.
REGION = 'us-east-1	'
S3_OUTPUT_BUCKET = 's3://tu-bucket-resultados-athena/results/' 
# Ojo: la ruta termina con 'results/' para organizar mejor tus resultados
DATABASE_NAME = 'ecommerce_analytics_db' # El nombre de la base de datos de Glue
ATHENA_CLIENT = boto3.client('athena', region_name=REGION)

app = Flask(__name__)

# Aquí se definirán los endpoints de tu API REST, como por ejemplo:
# @app.route('/api/ventas/top-productos', methods=['GET'])
# def get_top_products():
#     ... tu lógica de consulta a Athena ...