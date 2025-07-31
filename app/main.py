from fastapi import FastAPI
from app.routers import user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Mi Api rest de prueba",
    description="esta api es una prueba para aprender el uso de fastApi",
    version="0.1",
    contact={
        "name":"Max obregon",
        "phone":"900 713 005"
    }
)

# CORS por si accedes desde frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Registrar el router
app.include_router(user_router.router)
