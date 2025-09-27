import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Inicializar Faker
fake = Faker('es_ES')

# --- CONFIGURACIÓN DE VOLÚMENES ---
NUM_PRODUCTOS = 100
NUM_ALMACENES = 2
# Inventario = 2000 productos * 10 almacenes = 20,000 registros (¡Mínimo cumplido!)
NUM_INVENTARIO = NUM_PRODUCTOS * NUM_ALMACENES 

print(f"Generando {NUM_PRODUCTOS} Productos, {NUM_ALMACENES} Almacenes y {NUM_INVENTARIO} registros de Inventario...")

# =======================================================
# 1. ENTIDAD ALMACEN (10 Registros)
# =======================================================
almacenes_data = []
for i in range(1, NUM_ALMACENES + 1):
    almacenes_data.append({
        'id_almacen': i,
        'id_agenteAliado': random.randint(100, 999),
        'nombre': f"Almacén {i} - {fake.city()}",
        'ubicacion': fake.address().replace('\n', ', '),
        'capacidad': random.randint(50000, 500000),
        'tipo': random.choice(['General', 'Refrigerado', 'Peligroso', 'Zona Franca'])
    })
df_almacen = pd.DataFrame(almacenes_data)

# =======================================================
# 2. ENTIDAD PRODUCTO (2,000 Registros)
# =======================================================
productos_data = []
for i in range(1, NUM_PRODUCTOS + 1):
    precio = round(random.uniform(10.0, 500.0), 2)
    productos_data.append({
        'id_producto': i,
        'nombre': fake.word().capitalize() + " " + fake.word().capitalize(),
        'descripcion': fake.paragraph(nb_sentences=2),
        'peso': round(random.uniform(0.1, 50.0), 2),
        'volumen': round(random.uniform(0.01, 1.0), 2),
        'sku': f"SKU-{random.randint(100000, 999999)}",
        'precio': precio
    })
df_producto = pd.DataFrame(productos_data)

# =======================================================
# 3. ENTIDAD INVENTARIO (20,000 Registros)
# =======================================================
inventario_data = []
inventario_id = 1
start_date = datetime.now() - timedelta(days=90)

# Iterar sobre todos los productos y todos los almacenes para generar el Inventario
for prod_id in df_producto['id_producto']:
    for almacen_id in df_almacen['id_almacen']:
        
        # Generar stock realista
        stock_disp = random.randint(50, 5000)
        stock_res = random.randint(0, int(stock_disp * 0.1)) # 0 a 10% del disponible
        
        # Generar fecha aleatoria dentro de los últimos 90 días
        random_days = random.randint(1, 90)
        ultima_act = start_date + timedelta(days=random_days, hours=random.randint(0, 23), minutes=random.randint(0, 59))
        
        inventario_data.append({
            'id_inventario': inventario_id,
            'id_almacen': almacen_id,
            'id_producto': prod_id,
            'stock_disponible': stock_disp,
            'stock_reservado': stock_res,
            'ultima_actualizacion': ultima_act.strftime('%Y-%m-%d %H:%M:%S')
        })
        inventario_id += 1

df_inventario = pd.DataFrame(inventario_data)


# =======================================================
# 4. GUARDAR EN ARCHIVOS CSV
# =======================================================
print("\nGuardando archivos CSV...")

# Crear el directorio 'data' si no existe
import os
os.makedirs('data', exist_ok=True)

df_producto.to_csv('data/productos_2k.csv', index=False, encoding='utf-8')
print(" - data/productos_2k.csv: ¡Generado!")

df_almacen.to_csv('data/almacenes_10.csv', index=False, encoding='utf-8')
print(" - data/almacenes_10.csv: ¡Generado!")

df_inventario.to_csv('data/inventarios_20k.csv', index=False, encoding='utf-8')
print(" - data/inventarios_20k.csv: ¡Generado!")

print(f"\n¡Generación de data completada! Total de registros de inventario: {len(df_inventario)}")