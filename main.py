#########################################Primera Parte################################################
# Instalación del framwork fastApi, código:
# -pip install fastapi-

#Instalación del Servidor Uvicorn, código:
#-pip install "uvicorn[standard]"-

# Instalación del framwork fastApi y el servidor todo en una sola instrucción, código:
# -pip install fastapi[all]-

#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI

from routers import router_DB
#Creamos un objeto a partir de la clase FastAPI, propio del archivo main
app= FastAPI()

app.include_router(router_DB.router)

#Utilizamos la (instancia) función get del framework FastAPI
@app.get("/")
async def imprimir():
    return "Hola estudiantes"
