from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="API de Gestión de Tareas",
    description="Una API sencilla para gestionar tareas",
    version="1.0.0"
)

# Modelos de datos
class TareaBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=50, description="El título de la tarea")
    descripcion: Optional[str] = Field(None, max_length=200, description="Descripción detallada de la tarea")
    realizada: bool = Field(False, description="Indica si la tarea está realizada o no")

class CrearTarea(TareaBase):
    pass

class Tarea(TareaBase):
    id: int = Field(..., description="El identificador único de la tarea")

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "titulo": "Comprar víveres",
                "descripcion": "Leche, huevos, pan",
                "realizada": False
            }
        }

class RespuestaTarea(BaseModel):
    mensaje: str
    tarea: Tarea

# Simulación de base de datos en memoria
tareas: List[Tarea] = [
    Tarea(id=1, titulo="Comprar leche", descripcion="Comprar leche en el supermercado", realizada=False),
    Tarea(id=2, titulo="Leer libro", descripcion="Leer el libro de Python", realizada=False),
    Tarea(id=3, titulo="Hacer ejercicio", descripcion="Hacer 30 minutos de cardio", realizada=True),
    Tarea(id=4, titulo="Llamar al banco", descripcion="Solicitar información sobre la tarjeta de crédito", realizada=False),
    Tarea(id=5, titulo="Limpiar la casa", descripcion="Barrer, trapear y limpiar el baño", realizada=False),
    Tarea(id=6, titulo="Preparar la cena", descripcion="Cocinar pasta con salsa de tomate", realizada=False),
    Tarea(id=7, titulo="Enviar correo", descripcion="Enviar el informe semanal al equipo de trabajo", realizada=True),
    Tarea(id=8, titulo="Pagar servicios", descripcion="Pagar la factura del agua y la luz", realizada=False),
    Tarea(id=9, titulo="Organizar escritorio", descripcion="Ordenar los documentos y papeles acumulados", realizada=True),
    Tarea(id=10, titulo="Visitar al médico", descripcion="Consultar resultados del análisis", realizada=False)
]

# Rutas de la API
@app.get("/", response_model=dict)
async def inicio():
    return {"mensaje": "Bienvenido a la API de Gestión de Tareas"}

@app.get("/tasks", response_model=List[Tarea], status_code=status.HTTP_200_OK)
async def obtener_tareas():
    if not tareas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay tareas disponibles")
    return tareas

@app.post("/tasks", response_model=RespuestaTarea, status_code=status.HTTP_201_CREATED)
async def crear_tarea(tarea: CrearTarea):
    existe_tarea = any(t.titulo == tarea.titulo for t in tareas)
    if existe_tarea:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe una tarea con este título."
        )
    
    nueva_tarea = Tarea(id=len(tareas) + 1, **tarea.dict())
    tareas.append(nueva_tarea)
    return RespuestaTarea(
        mensaje="Tarea creada exitosamente",
        tarea=nueva_tarea
    )

@app.get("/tasks/{task_id}", response_model=RespuestaTarea, status_code=status.HTTP_200_OK)
async def obtener_tarea(task_id: int):
    tarea = next((t for t in tareas if t.id == task_id), None)
    if tarea is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada")
    return RespuestaTarea(
        mensaje="Tarea encontrada",
        tarea=tarea
    )

@app.put("/tasks/{task_id}", response_model=RespuestaTarea, status_code=status.HTTP_200_OK)
async def actualizar_tarea(task_id: int, tarea_actualizada: CrearTarea):
    tarea = next((t for t in tareas if t.id == task_id), None)
    if tarea is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada")
    
    tarea.titulo = tarea_actualizada.titulo
    tarea.descripcion = tarea_actualizada.descripcion
    tarea.realizada = tarea_actualizada.realizada
    
    return RespuestaTarea(
        mensaje="Tarea actualizada exitosamente",
        tarea=tarea
    )

@app.delete("/tasks/{task_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def eliminar_tarea(task_id: int):
    tarea = next((t for t in tareas if t.id == task_id), None)
    if tarea is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada")
    
    tareas.remove(tarea)
    return {"mensaje": "Tarea eliminada exitosamente"}

# Inicio de la aplicación
if __name__ == "__main__":
    uvicorn.run("apiTest:app", host="0.0.0.0", port=8000, reload=True)
