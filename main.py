from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from api.v1.api import api_router

app  = FastAPI(title="API de países com banco de dados")

@app.get("/", tags=["API"])
async def start_api():
    return {"message": "API de países funcionando normalmente!"}

origins = [
    'http://localhost',
    'http://localhost:8080', # XAMP
    'http://localhost:5500',
    'http://localhost:5173',
    'http://127.0.0.1:5500'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(api_router, prefix=settings.API_V1)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8002, log_level="info", reload=True)
