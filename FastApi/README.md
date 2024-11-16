# Python FastApi Project

### First Steps
* Install [Python 3](https://www.python.org/) < or latest
* Install [VsCode](https://code.visualstudio.com/)
* Install Python plugin (vsCode) Microsoft Version
* After deploying your app, you can use Swagger by add '/docs' on the url

## Dependency
* Virtual environment
```
pip install virtualenv
virtualenv -p python3 venv
.\venv\Scripts\activate
```
> [!CAUTION]
> if failure, open PowerShell as Admin and type 'Set-ExecutionPolicy Unrestricted'

* Install
```
pip list
pip install fastapi
pip install "uvicorn[standard]"       // server
pip install pymssql                   // SQL Server
pip install psycopg2                  // PosgreSQL (optional)
pip install python-multipart          // OAuth2
pip install python-jose[cryptography] // jwt
pip install python-dotenv             // .env
pip freeze > requirements.txt
uvicorn app.main:app --reload

pip install -r requirements.txt
```

* Server
> http://127.0.0.1:8000/

> http://127.0.0.1:8000/docs

## File .env
```
MSSQL_USER="************"
MSSQL_HOST="************"
MSSQL_PASSWORD="************"
MSSQL_DATABASE="************"

POSTGRES_USER="************"
POSTGRES_HOST="************"
POSTGRES_PASSWORD="************"
POSTGRES_DATABASE="************"
```

## Folder Structure
```
project
│
├── app/
│   ├── routes/         # Rrutas
│   │   ├── auth.py
│   │   ├── project.py
│   │   └── public.py
│   ├── tests/
│   ├── main.py
│   ├── models.py
│   └── mssql.py        # Archivo de conexión a la base de datos
├── venv/
├── .env
├── .env.local
├── .gitignore
├── README.md
├── requirements.txt
└── vercel.json
```

## Main
* Create main
  * import FastAPI
  * import routes
  * import Auth
```
from fastapi import FastAPI
from app.routes import route1, route2, ...

app = FastAPI(title="Portafolio", description="API", version="4.0")

@app.get("/", tags=["root"])
async def root():
  return {
    "msge" : "Portafolio",
    "developer" : "https://www.francisco-dev.cl/"
  }

app.include_router(route1.router)
app.include_router(route2.router)
...
```

## Auth
* Add auth on main


## Routes or Endpoint
* Create a route
  * import APIRouter
  * import DBConnection
  * import Models
```
from fastapi import APIRouter (project)
from app.mssql import execute_sp
from app.models import Model1, Model2, ...

router = APIRouter(prefix="/public", tags=["public"])

@router.get("/projects", response_model = List[Projects])
async def get_projects():
  return "projects"
```
* Add route to main
```
app.include_router(project.router)
```

### Others
```
datetime.now().astimezone() // local imezone
datetime.now(timezone.utc)  // timezone

timedelta(minutes = 15)
timedelta(seconds = 15)
timedelta(hours = 4)
timedelta(days = 7)
timedelta(weeks = 2)
```
