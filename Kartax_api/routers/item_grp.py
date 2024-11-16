from sql.sql_server import execute_sp
from fastapi import APIRouter

router = APIRouter(prefix="/item-grp", tags=["items-grp"])

@router.get("/{id}")
async def get_negocio_byid(id: int):
  result = await execute_sp("pa_item_grp_get_byid", (id,))
  return result

@router.get("/por-negocio/{id}")
async def get_negocio_byid(id: int):
  result = await execute_sp("pa_item_grp_get_byid_negocio", (id,))
  return result
