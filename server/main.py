from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Code(BaseModel):
    text: str

app = FastAPI()

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/interpret/")
async def interpret_code(code: Code):
    return code