from schemas.input import InputSchema
from schemas.output import OutputSchema
from fastapi import APIRouter, HTTPException, FastAPI
from datetime import datetime
from core import config
from service.code import code_instance

router = APIRouter()
code = code_instance

@router.post("/code/track", response_model=OutputSchema)
async def process_input(data: InputSchema):
    print("initializing project tracking....")
    try:
        response = await code.track(data)
    except RuntimeError as e:
        print(f"something went wrong: {e}")
        raise HTTPException(status_code=500)
    
    return OutputSchema(
        code=200,
        message="OK"
    )

