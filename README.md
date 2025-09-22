# Entidades y sus Métodos

## 🟡 Producto
**Atributos:**  
1. id_producto  
2. id_empresa  
3. nombre  
4. descripcion  
5. peso  
6. volumen  
7. sku  
8. precio  

**Métodos:**  
1. crearProducto()  
2. actualizarProducto()  
3. eliminarProducto()  
4. consultarProducto()  

---

## 🟡 Almacen
**Atributos:**  
1. id_almacen  
2. id_empresa  
3. id_agenteAliado  
4. nombre  
5. ubicacion  
6. capacidad  
7. tipo  

**Métodos:**  
1. registrarAlmacen()  
2. actualizarAlmacen()  
3. consultarStock()  

---

## 🟡 Inventario
**Atributos:**  
1. id_inventario  
2. id_almacen  
3. id_producto  
4. stock_disponible  
5. stock_reservado  
6. ultima_actualizacion  

**Métodos:**  
1. actualizarStock()  
2. reservarProducto()  
3. liberarReserva()  

---

## 🟠 AgenteAliado
**Atributos:**  
1. id_agente  
2. id_almacen  
3. ids_conductor  
4. nombre  
5. ruc  
6. telefono  

**Métodos:**  
1. registrarAgente()  
2. asignarAlmacen()  
3. consultarAgente()  

---

## 🟠 Vehiculo
**Atributos:**  
1. id_vehiculo  
2. id_conductor  
3. nombre  
4. tipo  
5. modelo  
6. color  
7. placa  

**Métodos:**  
1. registrarVehiculo()  
2. asignarConductor()  
3. consultarVehiculo()  

---

## 🟠 Conductor
**Atributos:**  
1. id_conductor  
2. id_agente  
3. id_vehiculo  
4. nombre  
5. dni  
6. telefono  

**Métodos:**  
1. registrarConductor()  
2. asignarVehiculo()  
3. consultarDisponibilidad()  

---

## 🟠 ClienteFinal
**Atributos:**  
1. id_cliente_final  
2. nombre  
3. correo  
4. telefono  
5. direccion_principal  

**Métodos:**  
1. registrarCliente()  
2. consultarCliente()  

---

## 🔴 Pedido
**Atributos:**  
1. id_pedido  
2. id_asignacionPedido  
3. id_empresa  
4. id_cliente_final  
5. fecha_creacion  
6. estado  
7. monto_total  
8. direccion_entrega  
9. ventana_horaria  

**Métodos:**  
1. crearPedido()  
2. actualizarEstado()  
3. consultarPedido()  

---

## 🔴 DetallePedido
**Atributos:**  
1. id_detalle  
2. id_pedido  
3. id_producto  
4. cantidad  
5. precio_unitario  

**Métodos:**  
1. agregarDetalle()  
2. consultarDetalle()  

---

## 🔴 PruebaEntrega
**Atributos:**  
1. id_prueba  
2. id_pedido  
3. foto_entrega  
4. firma_cliente  
5. otp_codigo  
6. fecha_registro  

**Métodos:**  
1. registrarEntrega()  
2. validarEntrega()  

---

# División en Microservicios

## Microservicio 1 – Gestión de Productos & Almacenes  
**Tecnología:** SQL – MySQL, Python/FastAPI  
**Entidades:** Producto, Almacen, Inventario  
**Responsable:** Julio  
**Funciones clave:**  
1. CRUD de productos  
2. Registrar almacenes  
3. Actualizar stock  

---

## Microservicio 2 – Logística y Transporte  
**Tecnología:** SQL – PostgreSQL, Java/Spring Boot  
**Entidades:** AgenteAliado, Vehiculo, Conductor  
**Responsable:** Amir  
**Funciones clave:**  
1. Registrar agentes  
2. Asignar vehículos y conductores  
3. Consultar disponibilidad  

---

## Microservicio 3 – Pedidos & Clientes  
**Tecnología:** NoSQL – MongoDB, Node.js/Express  
**Entidades:** ClienteFinal, Pedido, DetallePedido, PruebaEntrega  
**Responsable:** Ignacio  
**Funciones clave:**  
1. Crear pedidos  
2. Agregar detalles  
3. Registrar prueba de entrega  
4. Actualizar estado  

---

## Microservicio 4 – Integración  
**Tecnología:** Sin BD, Go o Python ligero  
**Entidades:** No propias (consume de los otros MS)  
**Responsable:** Frisancho  
**Funciones clave:**  
1. Endpoint `/asignarPedido`: combina Pedido (MS3) + Producto (MS1) + Conductor (MS2)  
2. Orquestación de servicios  

---

## Microservicio 5 – Analítico  
**Tecnología:** Python + Athena  
**Entidades:** No propias (consume data de S3)  
**Responsable:** Yuri  
**Funciones clave:**  
1. Consultas analíticas (ventas, stock, eficiencia de entregas)  
2. Endpoints: Reportes, etc...
