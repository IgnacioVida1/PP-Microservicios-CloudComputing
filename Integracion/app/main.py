from fastapi import FastAPI, HTTPException
from app.services.asignacion_service import AsignacionService
from app.models.asignacion_models import AsignacionPedidoRequest, AsignacionPedidoResponse, ReporteEficiencia

app = FastAPI(
    title="Microservicio 4 - Integración",
    description="Orquestador de servicios para asignación de pedidos",
    version="1.0.0"
)

asignacion_service = AsignacionService()

@app.get("/")
async def root():
    return {"message": "Microservicio 4 - Integración funcionando"}

@app.post("/asignarPedido/{id_pedido}", response_model=dict)
async def asignar_pedido(id_pedido: str):
    """
    Endpoint principal para asignar un pedido
    Combina: Pedido (MS3) + Producto (MS1) + Conductor (MS2)
    """
    try:
        resultado = await asignacion_service.asignar_pedido(id_pedido)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/reportes/eficiencia/{periodo}", response_model=ReporteEficiencia)
async def obtener_reporte_eficiencia(periodo: str):
    """
    Endpoint para reportes analíticos combinados
    """
    try:
        reporte = await asignacion_service.generar_reporte_eficiencia(periodo)
        return reporte
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """
    Endpoint de health check para verificar estado del servicio
    """
    return {"status": "healthy", "service": "ms4-integracion"}

if __name__ == "__main__":
    import uvicorn
    from app.config import config
    uvicorn.run(app, host=config.HOST, port=config.PORT)