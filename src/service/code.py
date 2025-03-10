from core import config
from schemas.input import InputSchema
from fastapi import UploadFile
from utils.database import db
from datetime import datetime

class Code:
    async def track(self, data: InputSchema, file: UploadFile):
        data.time = str(datetime.now())
        db.insert_large_object(data, file)
code_instance = Code()