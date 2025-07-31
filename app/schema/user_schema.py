from pydantic import BaseModel
from typing import Optional

# BaseModel viene de Pydantic y sirve para:
#Validar los datos automáticamente
#Definir los tipos
#Generar documentación en Swagger

class User(BaseModel):
    id: int
    name: str
    email: str

class UserCreate(BaseModel):
    name: str
    email: str