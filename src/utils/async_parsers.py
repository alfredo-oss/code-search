from fastapi import Form
from typing import Optional
from schemas.input import InputSchema

# convert form-data into a Pydantic model
async def parse_form_data(
        user: str = Form(...),
        project: str = Form(...),
        time: Optional[str] = Form(None)
 ) -> InputSchema:
    return InputSchema(user=user, project=project, time=time)
