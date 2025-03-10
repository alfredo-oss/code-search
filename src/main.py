from fastapi import FastAPI
from api.v1.endpoints import code
from core import config

app = FastAPI()

app.include_router(code.router, prefix="/api/v1", tags=["code"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=config.settings.APP_PORT)