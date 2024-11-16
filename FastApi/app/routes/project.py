from fastapi import APIRouter
from typing import List
from app.mssql import execute_sp
from app.models import Project

router = APIRouter(prefix="/project", tags=["project"])

@router.get("/", response_model=List[Project])
async def get_all():
  return await execute_sp("PF_Proyecto_GetAll", ())

