from core.config import settings 
from src.schemas.input import InputSchema
from fastapi import UploadFile
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
        
    def insert_large_object(self, data: InputSchema, file: UploadFile) -> str:
            CODE_POST_QUERY = f"""
                INSERT INTO {settings.TABLE_NAME} {settings.FIELDS}
                VALUES ({data.project}, {file.filename}, {data.time}, lo_import('/tmp/{file.filename}'));
            """
            self.cursor.execute(CODE_POST_QUERY)
        
db = DataBase()