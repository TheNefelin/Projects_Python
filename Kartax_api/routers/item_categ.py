from sql.sql_server import execute_sp
from fastapi import APIRouter

router = APIRouter(prefix="/item-categ", tags=["items-categ"])

@router.get("/{id}")
async def get_negocio_byid(id: int):
  result = await execute_sp("pa_item_categ_get_byid", (id,))
  return result

@router.get("/por-categ/{id}")
async def get_negocio_byid(id: int):
  result = await execute_sp("pa_item_categ_get_byid_grp", (id,))
  return result

@router.get("/por-negocio/{id}")
async def get_negocio_byid(id: int):
  result = await execute_sp("pa_item_categ_get_byid_negocio", (id,))
  return result
