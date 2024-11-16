from sql.sql_server import execute_sp
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/usuario", tags=["usuarios"])

# modelo ------------------------------------------------------------------
class Usuario(BaseModel):
  id: int
  nombres: str
  apellidos: str
  usuario: str
  correo: str
  fecha: datetime
  is_active: bool

# crud --------------------------------------------------------------------
@router.get("/")
async def get_usuario_all():
 return "developing"

@router.get("/{id}")
async def get_usuario_byid(id: int):
 return "developing"

@router.post("/")
async def post_usuario_byid(props: Usuario):
 return "developing"

@router.put("/")
async def put_usuario_byid(props: Usuario):
 return "developing"

@router.delete("/{id}")
async def del_usuario_byid(id: int):
 return "developing"
