from pydantic import BaseModel
from typing import Optional

class InputSchema(BaseModel):
    user: str
    project: str
    filename: str
    time: Optional[str]
    content: str