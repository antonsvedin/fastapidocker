from fastapi import FastAPI
from functions import calculate

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello world"}

@app.get("/test")
async def test():
    return {"message": "testing"}

@app.get("/calc/{num}")
async def calc(num):
    return calculate(num)