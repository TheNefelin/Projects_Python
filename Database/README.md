# Testing Python with Database
* install Python 3.11.4 (PC) [doc](https://www.python.org)
* install Python plugin (vsCode) Microsoft Version

### Virtual Environment
* install virtual env
* be sure its activate
```
pip install virtualenv
virtualenv -p python3 venv
.\venv\Scripts\activate
```
> :warning: if failure open PowerShell as Admin and type 'Set-ExecutionPolicy Unrestricted'

### Dependency
* python-dotenv [doc](https://pypi.org/project/python-dotenv)
* flask-marshmallow [doc](https://flask-marshmallow.readthedocs.io/en/latest)
* create requirements file
```
pip install flask-marshmallow
pip install flask-sqlalchemy 
pip install marshmallow-sqlalchemy
pip install python-dotenv
pip install mysqlclient

pip freeze > requirements.txt
```

### Create .env file
```
BD_CONN="conntection_string"
```

### Run server or deploy api
```
python src/app.py
// OR
(... nothing yet)
```

### Other Commands
* get list of all dependency
* install all dependency from requirements file
```
pip list
pip install -r requirements.txt
```

### Connection
```
BD_CONN_MYSQL=mysql//user:pass@host:port/db
```