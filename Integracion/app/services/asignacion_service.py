from app.services.producto_service import ProductoService
from app.services.pedido_service import PedidoService
from app.services.logistica_service import LogisticaService
from datetime import datetime
import uuid

class AsignacionService:
    def __init__(self):
        self.producto_service = ProductoService()
        self.pedido_service = PedidoService()
        self.logistica_service = LogisticaService()
    
    async def asignar_pedido(self, id_pedido: str):
        # 1. Obtener información del pedido
        pedido = await self.pedido_service.obtener_pedido(id_pedido)
        if not pedido:
            return {"error": "Pedido no encontrado"}
        
        # 2. Verificar stock de productos
        for detalle in pedido.get("detalles", []):
            stock_ok = await self.producto_service.verificar_stock(
                detalle["id_producto"], 
                detalle["cantidad"]
            )
            if not stock_ok:
                return {"error": f"Stock insuficiente para producto {detalle['id_producto']}"}
        
        # 3. Buscar conductor disponible
        conductor = await self.logistica_service.buscar_conductor_disponible(
            pedido["direccion_entrega"],
            pedido["ventana_horaria"]
        )
        
        if not conductor:
            return {"error": "No hay conductores disponibles"}
        
        # 4. Asignar conductor al pedido
        await self.logistica_service.asignar_conductor_pedido(id_pedido, conductor["id_conductor"])
        
        # 5. Actualizar estado del pedido
        await self.pedido_service.actualizar_estado_pedido(
            id_pedido, 
            "asignado", 
            conductor["id_conductor"]
        )
        
        # 6. Retornar respuesta de asignación
        return {
            "id_asignacion": str(uuid.uuid4()),
            "id_pedido": id_pedido,
            "id_conductor": conductor["id_conductor"],
            "id_vehiculo": conductor["id_vehiculo"],
            "conductor": conductor["nombre"],
            "vehiculo": conductor["vehiculo"],
            "estado": "asignado",
            "fecha_asignacion": datetime.now().isoformat(),
            "mensaje": "Pedido asignado exitosamente"
        }
    
    async def generar_reporte_eficiencia(self, periodo: str):
        # TODO: Implementar lógica de reportes combinando datos de todos los MS
        return {
            "periodo": periodo,
            "total_pedidos": 150,
            "pedidos_entregados": 142,
            "tasa_exito": 94.67,
            "tiempo_promedio_entrega": 2.5,
            "conductores_activos": 8
        }