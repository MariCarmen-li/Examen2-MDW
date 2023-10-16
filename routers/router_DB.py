#Acciones
#1 cambiamos path de "usersclass" a "userdb"
#Movemos basemodel
#vaciamos user list

#-uvicorn main:app --reload-

#Path:  http://127.0.0.1:8000/userdb

#POST-body-JSON
#{"username":"Flash", "email":"Flas@buap.mx"}

#En vez de Importar el framework fastapi, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status
#Invocamos la entidad que hemos creado ****nEw
from db.models.userClass import User 
#Importamos la instancia que devolvera al usuario en formato user ***new
from db.schemas.userDICT import user_schema
#Importamos nuestro cliente para poder agregar usuarios a la db****nEw
from db.db import connection



#Creamos un objeto a partir de la clase FastAPI
router= APIRouter()

#Levantamos el server Uvicorn
#-uvicorn 4_codigos_HTTP:app --reload-
#{"id":3,"Name":"Alfredo", "LastName":"Garcia", "Age":30}
#Definimos nuestra entidad: user


#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
#users_list= []


#***Get

@router.get("/userdb/", status_code=status.HTTP_200_OK)
async def usersclass():
    users_list = []
    try:
        for userdb in connection.Computacion.user.find():
            userJSON = user_schema(userdb)
            users_list.append( User(**userJSON) )
        return users_list
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/
 


#***Get con Filtro Path
@router.get("/userdb/{username}")
async def usersclass(username:str):
    try:
        new_user=  user_schema(connection.Computacion.user.find_one({"username":username}))
        return User(**new_user)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
 
 
#***Post
@router.post("/userdb/",response_model=User, status_code=201)
async def usersclass(user:User):

    #Seconvierte de objeto User a Dict(JSON)
    user_dict= dict (user)
    #Elimino id del diccionario
    del user_dict["id"]
    #1 Creo un esquema que se llama usuarios dentro de Computacion
    #Computación= Base de datos
    #users= Colección
    id= connection.Computacion.user.insert_one(user_dict).inserted_id
    
    #Consultamos el user insertado en la bd con todo y id asignado automaticamente
    #Me devuelve un JSON hay que convertirlo a un objeto tipo User (user.py en schemas)
    new_user=  user_schema(connection.Computacion.user.find_one({"_id":id}))
    
    #La base de datos devuelve un JSON debemos transformarlo a un objeto tipo user:
    return User(**new_user)

#Put
@router.put("/userdb/{username}", response_model=User, status_code=status.HTTP_201_CREATED)
async def usersclass(user: User, username:str):
    newusername = user.username
    full_name = user.full_name
    email = user.email
    disabled = user.disabled

    filtro = {"username":username}
    newvalues = {"$set":{"email":email,
                         "full_name":full_name,
                         "disabled":disabled,
                         "username":newusername}}

    try:
        connection.Computacion.user.update_one(filtro,newvalues)
        new_user =  user_schema(connection.Computacion.user.find_one({"username":newusername}))
        return User(**new_user)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
#Delete
@router.delete("/userdb/{username}", status_code=status.HTTP_204_NO_CONTENT)
async def usersclass(username:str):
    try:
        connection.Computacion.user.delete_one({"username":username})
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


