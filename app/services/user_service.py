import json
from typing import List, Optional
from app.schema.user_schema import User, UserCreate
from pathlib import Path

DB_FILE = Path(__file__).resolve().parent.parent / "db" / "fake_db.json"

# Cargar datos
def load_users() -> List[User]:
    try:
        with open(DB_FILE, "r") as f:
            return [User(**user) for user in json.load(f)]
    except FileNotFoundError:
        return []

# Guardar datos
def save_users(users: List[User]):
    with open(DB_FILE, "w") as f:
        json.dump([user.dict() for user in users], f, indent=4)

# Obtener todos
def get_all_users() -> List[User]:
    return load_users()

# Obtener por ID
def get_user_by_id(user_id: int) -> Optional[User]:
    users = load_users()
    return next((user for user in users if user.id == user_id), None)

# Crear
def create_user(user_data: UserCreate) -> User:
    users = load_users()
    new_id = max([user.id for user in users], default=0) + 1
    new_user = User(id=new_id, **user_data.dict())
    users.append(new_user)
    save_users(users)
    return new_user

# Actualizar
def update_user(user_id: int, user_data: UserCreate) -> Optional[User]:
    users = load_users()
    for i, user in enumerate(users):
        if user.id == user_id:
            updated = User(id=user_id, **user_data.dict())
            users[i] = updated
            save_users(users)
            return updated
    return None

# Eliminar
def delete_user(user_id: int) -> bool:
    users = load_users()
    updated_users = [user for user in users if user.id != user_id]
    if len(updated_users) == len(users):
        return False
    save_users(updated_users)
    return True
