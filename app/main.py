from fastapi import FastAPI
from app.db_settings import returnAllUsers

app = FastAPI()

@app.get("/")
async def index():
    user_dict = {}
    for user in returnAllUsers():
        user_dict[str(user['_id'])] = user['username']
    return (str(user_dict))
