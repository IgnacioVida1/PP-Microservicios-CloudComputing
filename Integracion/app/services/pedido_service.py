import httpx
from app.config import config

class PedidoService:
    def __init__(self):
        self.base_url = config.MS3_PEDIDOS_URL
    
    async def obtener_pedido(self, id_pedido: str):
        # TODO: Implementar llamada real cuando MS3 esté listo
        try:
            # async with httpx.AsyncClient() as client:
            #     response = await client.get(f"{self.base_url}/pedidos/{id_pedido}")
            #     return response.json()
            
            # Mock response
            return {
                "id_pedido": id_pedido,
                "id_cliente_final": "cliente_123",
                "estado": "pendiente",
                "direccion_entrega": "Av. Principal 123",
                "ventana_horaria": "09:00-12:00",
                "detalles": [
                    {"id_producto": "prod_1", "cantidad": 2},
                    {"id_producto": "prod_2", "cantidad": 1}
                ]
            }
        except Exception as e:
            print(f"Error obteniendo pedido: {e}")
            return None
    
    async def actualizar_estado_pedido(self, id_pedido: str, estado: str, conductor_id: str = None):
        # TODO: Implementar llamada real
        print(f"Actualizando pedido {id_pedido} a estado: {estado}")
        return {"success": True}