# **API de Gestión de Tareas (To-Do)**

Este proyecto es una **API RESTful** creada con **FastAPI** que permite gestionar tareas. Incluye funcionalidades para **crear, leer, actualizar y eliminar tareas** (CRUD). A continuación, se explica cómo configurar el entorno, instalar las dependencias y ejecutar la aplicación.

---

### **Requisitos Previos**
Asegúrate de tener lo siguiente instalado en tu máquina:

- **Python** (versión 3.7 o superior) → [Descargar Python](https://www.python.org/downloads/)
- **pip** (viene con la instalación de Python)
- **Virtualenv** (opcional, pero recomendado para entornos virtuales)

---

## **1. Clonar el proyecto**

Primero, clona el proyecto desde tu repositorio (o descarga el código):

```bash
git clone https://github.com/tu-usuario/nombre-del-repositorio.git
cd nombre-del-repositorio
```

---

## **2. Crear un entorno virtual (recomendado)**

Es recomendable crear un **entorno virtual** para gestionar las dependencias sin afectar otros proyectos:

```bash
# Crear el entorno virtual (Linux/Mac)
python3 -m venv venv

# Crear el entorno virtual (Windows)
python -m venv venv

# Activar el entorno virtual (Linux/Mac)
source venv/bin/activate

# Activar el entorno virtual (Windows)
venv\Scripts\activate
```

---

## **3. Instalar las dependencias**

Dentro del entorno virtual, instala las dependencias necesarias desde el archivo **`requirements.txt`**:

```bash
pip install -r requirements.txt
```

**Nota:** Si no tienes el archivo `requirements.txt`, crea uno con el siguiente contenido:

```text
fastapi==0.95.2
uvicorn==0.22.0
```

Puedes añadir más dependencias si es necesario.

---

## **4. Ejecutar la API**

Para ejecutar la API, utiliza **uvicorn** con el siguiente comando:

```bash
uvicorn apiTest:app --reload
```

- **`apiTest`**: Nombre del archivo Python (asegúrate de que coincide con tu archivo).
- **`--reload`**: Habilita la recarga automática del servidor en modo desarrollo.

Después de ejecutar este comando, la API estará disponible en:  
**[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## **5. Probar la API**

### **Swagger UI**
FastAPI proporciona una interfaz web para probar los endpoints automáticamente:

- Ve a **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** para acceder a **Swagger UI**.
- Desde allí puedes probar todos los **endpoints** fácilmente.

### **Alternativa: Redoc**
Otra opción es la interfaz de **Redoc**, disponible en:

- **[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)**

---

## **6. Endpoints Disponibles**

| Método  | Endpoint         | Descripción                            |
|---------|------------------|----------------------------------------|
| GET     | `/tasks`         | Obtiene la lista de todas las tareas   |
| POST    | `/tasks`         | Crea una nueva tarea                   |
| GET     | `/tasks/{id}`    | Obtiene una tarea específica por su ID |
| PUT     | `/tasks/{id}`    | Actualiza una tarea existente por su ID|
| DELETE  | `/tasks/{id}`    | Elimina una tarea por su ID            |

---

## **7. Ejemplo de Uso**

Puedes probar los endpoints usando **Postman**, **curl** o directamente desde Swagger UI.

**Ejemplo de solicitud `POST` para crear una nueva tarea:**

```json
POST /tasks
{
  "titulo": "Estudiar para el examen",
  "descripcion": "Preparar temas de matemáticas",
  "realizada": false
}
```

**Ejemplo de respuesta:**

```json
{
  "mensaje": "Tarea creada exitosamente",
  "tarea": {
    "id": 11,
    "titulo": "Estudiar para el examen",
    "descripcion": "Preparar temas de matemáticas",
    "realizada": false
  }
}
```

---

## **8. Desactivar el Entorno Virtual**

Cuando hayas terminado, puedes desactivar el entorno virtual con:

```bash
# Linux/Mac
deactivate

# Windows
venv\Scripts\deactivate
```

---

## **9. Notas Finales**
- Si deseas agregar más dependencias, puedes hacerlo con:

  ```bash
  pip install <nombre-paquete>
  pip freeze > requirements.txt
  ```

- Si tienes problemas con los puertos, asegúrate de que **ningún otro servicio** esté utilizando el puerto **8000**.

---

## **10. Créditos**
Este proyecto fue desarrollado como un ejemplo educativo para gestionar tareas utilizando **FastAPI**.

---

### **Listo para Ejecutar**
Este archivo README contiene todo lo que necesitas para configurar y ejecutar la API. Si tienes preguntas adicionales, no dudes en preguntar.
