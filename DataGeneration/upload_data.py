import boto3
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# Cliente S3
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
    region_name=AWS_REGION
)

# Carpeta local donde tienes los CSV
carpeta_local = "data"

# Nombre del bucket
nombreBucket = "analytics-proy-parcial"

# Carpeta local donde tienes los CSV
carpeta_local = "data"

# Archivos locales y su carpeta destino en el bucket
archivos = {
    "inventarios_20k.csv": "data/inventarios/",
    "productos_2k.csv":   "data/productos/",
    "almacenes_10.csv":   "data/almacenes/"
}

# Subir cada archivo
for archivo_local, carpeta_destino in archivos.items():
    ruta_local = os.path.join(carpeta_local, archivo_local)  # ej: data/Inventarios.csv
    ruta_s3 = carpeta_destino + archivo_local                # ej: data/inventarios/Inventarios.csv
    try:
        s3.upload_file(ruta_local, nombreBucket, ruta_s3)
        print(f"✅ Subido {ruta_local} → s3://{nombreBucket}/{ruta_s3}")
    except Exception as e:
        print(f"❌ Error subiendo {ruta_local}: {e}")

print("🚀 Ingesta completada")
