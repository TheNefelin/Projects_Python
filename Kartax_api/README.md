# Kartax API v3.0

> [Deployed API](https://kartax-api-py.vercel.app/docs)

* install Python 3.11.4 (PC) [page & doc](https://www.python.org/)
* install Python plugin (vsCode) Microsoft Version
* after deploying your app, you can use Swagger by add '/docs' on the url

### installing dependency 
```
//for create virtual environment
pip install virtualenv
virtualenv -p python3 env (if failure open PowerShell as Admin and type 'Set-ExecutionPolicy Unrestricted')
.\env\Scripts\activate

//this install FastApi
pip install fastapi

//this install Uvicorn as Server
pip install "uvicorn[standard]"

//package for managing SQL Server
pip install pymssql

//for creating .env file for secret data
pip install python-dotenv 

//for form data sending user password on OAuth2
pip install python-multipart 

//create the requirements file
pip freeze > requirements.txt 
```

### create .env file
```
BD_DRIVER="SQL Server"
DB_HOST="host path"
DB_DATABASE="database name"
DB_USER="user name"
DB_PASSWORD="password"
```

### Deploy and run API
```
//run server
.\env\Scripts\activate
uvicorn src.main:app --reload
```

### Other commands
```
//list of all dependency
pip list

//install all dependency from requirements.txt
pip install -r requirements.txt
```
