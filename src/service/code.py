from core import config
from schemas.input import InputSchema
from fastapi import UploadFile
from utils.database import db
from datetime import datetime

class Code:
    async def track(self, data: InputSchema, file: UploadFile):
        now = datetime.now()
        data.time = f"{now.year}-{now.month}-{now.day}"
        db.insert_large_object(data, file)

    async def retrieve(self, project: str):
        info = db.retrieve_info(project)
        return info
code_instance = Code()