INSERT INTO agente_aliado (id_agente, id_almacen, nombre, ruc, telefono) VALUES (1, 100, 'Agente Uno', '20123456789', '999111222');
INSERT INTO vehiculo (id_vehiculo, id_conductor, nombre, tipo, modelo, color, placa) VALUES (1, NULL, 'Camion A', 'Camión', 'Volvo FH', 'Blanco', 'ABC-123');
INSERT INTO conductor (id_conductor, id_agente, id_vehiculo, nombre, dni, telefono, disponible) VALUES (1, 1, NULL, 'Juan Perez', '12345678', '999000111', true);
