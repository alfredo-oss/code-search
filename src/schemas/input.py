from pydantic import BaseModel
from typing import Optional

class InputSchema(BaseModel):
    user: str
    project: str
    file: Optional[str]
    time: Optional[str]