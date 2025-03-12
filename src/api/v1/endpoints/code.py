from schemas.input import InputSchema
from schemas.output import OutputSchema
from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from datetime import datetime
from core import config
from service.code import code_instance
from utils.async_parsers import parse_form_data

router = APIRouter()
code = code_instance


@router.post("/code/track", response_model=OutputSchema)
async def process_input(
    data: InputSchema = Depends(parse_form_data), 
    file: UploadFile = None
    ):
    print("initializing project tracking....")
    print(f"sending {file.filename} to server... ")
    try:
        response = await code.track(data, file)
    except RuntimeError as e:
        print(f"something went wrong: {e}")
        raise HTTPException(status_code=500)
    
    return OutputSchema(
        code=200,
        message="OK"
    )

@router.get("/code/{project_name}")
async def get_project_status(
    project_name: str
    ):
    print("querying the database...")
    try:
        response = await code.retrieve(project_name)
        print(f"got response: {response}")
    except RuntimeError as e:
        print(f"something went wrong: {e}")
        raise HTTPException(status_code=500)
    return response


