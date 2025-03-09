from core import config
from schemas.input import InputSchema
from utils.database import db

class Code:
    async def track(self, data: InputSchema):
        db.insert_large_object(data)
code_instance = Code()