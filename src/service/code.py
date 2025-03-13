from schemas.input import InputSchema
from utils.database import db
from datetime import datetime

class Code:
    async def track(self, data: InputSchema):
        now = datetime.now()
        data.time = f"{now.year}-{now.month}-{now.day}"
        # encoding data for byte-like insertion to database
        file = (data.content).encode("utf-8")
        db.insert_byte_like_object(data, file)

    async def retrieve(self, project: str):
        info = db.retrieve_info(project)
        return info
    
    async def retrieve_content(self, project: str):
        info = db.retrieve_binary_content(project)
        return info
code_instance = Code()