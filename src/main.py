import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api_v1 import router

app = FastAPI()

origins = ["*"]

# app.mount("/static", StaticFiles(directory="frontend"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)

@app.get("/")
async def root():
    return {"name": "autoservice"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

