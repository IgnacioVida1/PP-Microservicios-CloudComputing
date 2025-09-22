## Entidades y sus Métodos
🟡 Producto
1. Atributos: id_producto, id_empresa, nombre, descripcion, peso, volumen, sku, precio
2. Métodos:
	a. crearProducto()  
	b. actualizarProducto()
	c. eliminarProducto()
	d. consultarProducto()

🟡 Almacen
1. Atributos: id_almacen, id_empresa, id_agenteAliado, nombre, ubicacion, capacidad, tipo
2. Métodos:
	a. registrarAlmacen()
	b. actualizarAlmacen()
	c. consultarStock()

🟡 Inventario
Atributos: id_inventario, id_almacen, id_producto, stock_disponible, stock_reservado,
ultima_actualizacion
Métodos:
actualizarStock()
reservarProducto()
liberarReserva()
🟠 AgenteAliado
Atributos: id_agente, id_almacen, ids_conductor, nombre, ruc, telefono
Métodos:
registrarAgente()
asignarAlmacen()
consultarAgente()
🟠 Vehiculo
Atributos: id_vehiculo, id_conductor, nombre, tipo, modelo, color, placa
Métodos:
registrarVehiculo()
asignarConductor()
consultarVehiculo()
🟠 Conductor
Atributos: id_conductor, id_agente, id_vehiculo, nombre, dni, telefono
Métodos:
registrarConductor()
asignarVehiculo()
consultarDisponibilidad()
🟠 ClienteFinal
Atributos: id_cliente_final, nombre, correo, telefono, direccion_principal
Métodos:
registrarCliente()
consultarCliente()
🔴 Pedido
Atributos: id_pedido, id_asignacionPedido, id_empresa, id_cliente_final, fecha_creacion, estado, monto_total, direccion_entrega, ventana_horaria
Métodos:
crearPedido()
actualizarEstado()
consultarPedido()
🔴 DetallePedido
Atributos: id_detalle, id_pedido, id_producto, cantidad, precio_unitario
Métodos:
agregarDetalle()
consultarDetalle()
🔴 PruebaEntrega
Atributos: id_prueba, id_pedido, foto_entrega, firma_cliente, otp_codigo, fecha_registro
Métodos:
registrarEntrega()
validarEntrega()

# División en Microservicios
Microservicio 1 – Gestión de Productos & Almacenes (SQL – MySQL, Python/FastAPI)
Entidades: Producto, Almacen, Inventario
Responsable: Persona 1
Funciones clave: CRUD de productos, registrar almacenes, actualizar stock.

Microservicio 2 – Logística y Transporte (SQL – PostgreSQL, Java/Spring Boot)
Entidades: AgenteAliado, Vehiculo, Conductor
Responsable: Persona 2
Funciones clave: registrar agentes, asignar vehículos y conductores, consultar disponibilidad.

Microservicio 3 – Pedidos & Clientes (NoSQL – MongoDB, Node.js/Express)
Entidades: ClienteFinal, Pedido, DetallePedido, PruebaEntrega
Responsable: Persona 3
Funciones clave: crear pedidos, agregar detalles, registrar prueba de entrega, actualizar estado.

Microservicio 4 – Integración (Sin BD, Go o Python ligero)
Entidades: No propias (consume de los otros MS).
Responsable: Persona 4
Funciones clave:
Endpoint /asignarPedido: combina Pedido (MS3) + Producto (MS1) + Conductor (MS2).
Orquestación de servicios.

Microservicio 5 – Analítico (Python + Athena)
Entidades: No propias (consume data de S3).
Responsable: Persona 5
Funciones clave:
Consultas analíticas (ventas, stock, eficiencia de entregas).


Endpoints /reportes/....
