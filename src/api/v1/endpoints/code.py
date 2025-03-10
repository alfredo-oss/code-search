from schemas.input import InputSchema
from schemas.output import OutputSchema
from fastapi import APIRouter, HTTPException, UploadFile
from datetime import datetime
from core import config
from service.code import code_instance

router = APIRouter()
code = code_instance

@router.post("/code/track", response_model=OutputSchema)
async def process_input(data: InputSchema, file: UploadFile):
    print("initializing project tracking....")
    print(f"sending {file.filename} to server... ")
    try:
        response = await code.track(data)
    except RuntimeError as e:
        print(f"something went wrong: {e}")
        raise HTTPException(status_code=500)
    
    return OutputSchema(
        code=200,
        message="OK"
    )

