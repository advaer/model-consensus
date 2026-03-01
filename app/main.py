from fastapi import FastAPI
from jsonframe import ok

app = FastAPI()


@app.get("/")
async def root():
    return ok({"message": "Hello World"})
