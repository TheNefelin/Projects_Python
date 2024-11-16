import pymssql
import os
from dotenv import load_dotenv

load_dotenv()

# importar variables de entorno
DB_DRIVER = os.getenv("BD_DRIVER")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

async def getTesting():
  try:
    version = await execute_query("SELECT SUBSTRING(@@VERSION, 1, 44)")
    return [{ 
      "msge": "Kartax API v3.0", 
      "db": f'{version[0]} ...',
      "developer": "https://www.francisco-dev.cl/"
    }]
  except Exception as ex:
    return [{"error": str(ex)}]

# funciones que ejecutan las querys y los procedimientos almacenados de SQL Server
async def execute_query(query):
  try:
    with pymssql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE) as connection:
      with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        return result
  except Exception as ex:
    return [{"estado": False, "error": str(ex)}]

async def execute_sp(sp, params):
  try:
    with pymssql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE) as connection:
      with connection.cursor(as_dict=True) as cursor:
        cursor.callproc(sp, params)
        result = cursor.fetchall()
        connection.commit()
        return result
  except Exception as ex:
    return [{"estado": False, "error": str(ex)}]