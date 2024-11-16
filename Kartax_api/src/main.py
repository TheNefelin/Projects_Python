from sql.sql_server import getTesting, execute_sp
from pydantic import BaseModel
from datetime import datetime
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware #cors handler class
from fastapi.staticfiles import StaticFiles #img handler class
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from routers import negocios, clientes, item_grp, item_categ, item, usuarios

app = FastAPI(title="Kartax", description="API", version="3.0")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="usuario-logearse")

# origins = [
#     "http://localhost",
#     "http://localhost:8000",
#     "http://localhost:3000",
# ]
# fechaql = datetime.strptime("20230725 15:42:00", "%Y%m%d %H:%M:%S")

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# modelo ------------------------------------------------------------------
class Registrarse(BaseModel):
  nombres: str
  apellidos: str
  usuario: str
  correo: str
  clave: str

class Logearse(BaseModel):
  usuario: str
  clave: str

# root --------------------------------------------------------------------
@app.get("/", tags=["root"])
async def root():
  return await getTesting()

@app.post("/usuario-registrarse", tags=["root"])
async def registrarse(obj: Registrarse):
  result = await execute_sp("pa_usuario_registrarse", (obj.nombres, obj.apellidos, obj.usuario, obj.correo, obj.clave,))
  estado, msge = result[0]['estado'], result[0]['msge']

  if not estado:
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail = msge,
      headers={"WWW-Authenticate": "Bearer"},
    )

  return result

@app.post("/usuario-logearse", tags=["root"])
async def iniciar_sesion(form: OAuth2PasswordRequestForm = Depends()):
  result = await execute_sp("pa_usuario_logearse", (form.username, form.password,))
  estado, msge = result[0]['estado'], result[0]['msge']

  if not estado:
    raise HTTPException(
      status_code = status.HTTP_401_UNAUTHORIZED, 
      detail = msge,
      headers={"WWW-Authenticate": "Bearer"},
    )
  
  sql_token, nombres, apellidos, correo, rol = result[0]['sql_token'], result[0]['nombres'], result[0]['apellidos'], result[0]['correo'], result[0]['rol']

  return {"access_token": sql_token, "token_type": "bearer", "msge": msge, "nombres": nombres, "apellidos": apellidos, "correo": correo, "rol": rol }

@app.get("/token", tags=["root"])
async def get_token(token: str = Depends(oauth2_scheme)):
   print(token)
   return {"token": token}

# routers -----------------------------------------------------------------
app.include_router(clientes.router)
app.include_router(negocios.router)
app.include_router(item_grp.router)
app.include_router(item_categ.router)
app.include_router(item.router)
app.include_router(usuarios.router, dependencies=[Depends(oauth2_scheme)])
app.mount("/static", StaticFiles(directory="static"), name="static")
