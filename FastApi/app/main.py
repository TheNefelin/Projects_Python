from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.routes import auth, public, project

app = FastAPI(title="Portafolio", description="API", version="4.0")

@app.get("/", tags=["root"])
async def root():
  return {
    "msge" : "Portafolio",
    "developer" : "https://www.francisco-dev.cl/"
  }

app.include_router(auth.router)
app.include_router(public.router)
app.include_router(project.router, dependencies=[Depends(auth.oauth2_scheme)])
