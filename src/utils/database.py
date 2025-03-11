from core.config import settings 
from schemas.input import InputSchema
from fastapi import UploadFile
import psycopg2


class DataBase:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(f"dbname={settings.DATABASE_NAME} user={settings.DATABASE_USER}")
            self.cursor = self.conn.cursor()
        except:
            raise RuntimeError("database failed to connect")
        
    def insert_large_object(self, data: InputSchema, file: UploadFile) -> str:
            CODE_POST_QUERY = """
                INSERT INTO basic_track (project, filename, modification, file)
                VALUES (%s, %s, %s, lo_import(%s));
            """
            try:
                self.cursor.execute(CODE_POST_QUERY, (data.project, file.filename, data.time, f"/tmp/{file.filename}"))
                self.conn.commit()
            except Exception as e:
                 print(f"Database error: {e}")
                 self.conn.rollback()
                 raise
        
db = DataBase()