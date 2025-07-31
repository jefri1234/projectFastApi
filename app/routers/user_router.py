from fastapi import APIRouter, HTTPException
from typing import List
from app.schema.user_schema import User, UserCreate
from app.services import user_service

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=List[User],summary="lista todos los usuarios",description="obtenemos todos los usuarios registrados",response_description="lista de usuarios")
def get_users():
    return user_service.get_all_users()

@router.get("/{user_id}", response_model=User,summary="obtenemos un usuario por su id",description="buscamos un usuario por su id que el usuario nos proporciona")
def get_user(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    return user_service.create_user(user)

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate):
    updated = user_service.update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}")
def delete_user(user_id: int):
    success = user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
