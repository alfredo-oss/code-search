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
                INSERT INTO basic_track (project, filename, modification_time, file)
                VALUES (%s, %s, %s, %s);
            """
            try:
                file_data = file.file.read()
                self.cursor.execute(CODE_POST_QUERY, (data.project, file.filename, data.time, file_data))
                self.conn.commit()
            except Exception as e:
                 print(f"Database error: {e}")
                 self.conn.rollback()
                 raise
        
    def retrieve_info(self, project: str) -> str:
        CODE_GET_QUERY = """
            SELECT filename, modification_time
            FROM basic_track
            WHERE project = %s;
        """
        try:
            self.cursor.execute(CODE_GET_QUERY, (project,))
            row = self.cursor.fetchone()
            return row
        except Exception as e:
             print(f"Database error: {e}")
             self.conn.rollback()
             raise
db = DataBase()