from pydantic import BaseModel

class OutputSchema(BaseModel):
    code: str
    message: str