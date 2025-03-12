from pydantic import BaseModel

class OutputSchema(BaseModel):
    code: int
    message: str