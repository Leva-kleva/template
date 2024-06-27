import os

app_name = "main"

debug = os.environ.get('DEBUG') if os.environ.get('DEBUG') else True
if debug == "False": debug = False

host = os.environ.get('HOST_SERVICE') if os.environ.get('HOST_SERVICE') else "0.0.0.0"
port = os.environ.get('PORT_SERVICE') if os.environ.get('PORT_SERVICE') else 8015

secret_key = os.environ.get('SECRET_KEY') if os.environ.get('SECRET_KEY') else "secret"

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}

db_user = os.environ.get('DB_USER') if os.environ.get('DB_USER') else ""
db_password = os.environ.get('DB_PASSWORD') if os.environ.get('DB_PASSWORD') else ""
db_host = os.environ.get('DB_HOST') if os.environ.get('DB_HOST') else ""
db_port = os.environ.get('DB_PORT') if os.environ.get('DB_PORT') else ""
db_name = os.environ.get('DB_NAME') if os.environ.get('DB_NAME') else ""

postgresql_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
