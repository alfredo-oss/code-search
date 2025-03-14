from schemas.input import InputSchema
from schemas.output import OutputSchema
from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from datetime import datetime
from core import config
from service.code import code_instance

router = APIRouter()
code = code_instance

### TODO: Both retrieval and posting in a future need to be tracked by user, if more than one person
###       wants to use the tool.

#### this endpoint allows to start tracking a project ####
@router.post("/code/track", response_model=OutputSchema)
async def process_input(
    data: InputSchema 
    ):
    print("initializing project tracking....")
    print(f"sending {data.filename} to server... ")
    try:
        response = await code.track(data)
    except RuntimeError as e:
        print(f"something went wrong: {e}")
        raise HTTPException(status_code=500)
    
    return OutputSchema(
        code=200,
        message="OK"
    )

#### this endpoint allows us to get the project status ####
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

#### this endpoint allow us to retrieve a file from a project ####
@router.get("/code/track/{filename}")
async def get_file(
    filename: str
):
    print("querying the database...")
    try:
        response = await code.retrieve_content(filename)
        print("successfully got file content")
    except RuntimeError as e:
        print(f"something went wrong: {e}")
        raise HTTPException(status_code=500)
    return response

