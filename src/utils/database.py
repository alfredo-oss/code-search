from core.config import settings 
from schemas.input import In
import psycopg2

# connect to postgreSQL
conn = psycopg2.connect("dbname=postgres user=postgres")
cur = conn.cursor()

class DataBase:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(f"dbname={settings.DATABASE_NAME} user={settings.DATABASE_USER}")
            self.cursor = conn.cursor()
        except:
            raise RuntimeError("database failed to connect")
        
    def insert_large_object(self, **kwargs) -> str:
            CODE_POST_QUERY = f"""
                INSERT INTO {settings.TABLE_NAME} ({kwargs.get("project")}, {kwargs.get("filename")}, {kwargs.get("modification")}, {kwargs.get("file")})
                VALUES ({kwargs.get("filename")}, lo_import('{kwargs.get("path_to_file")}'));
            """

        
db = DataBase()