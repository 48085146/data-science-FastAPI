from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class User(BaseModel):
    name: str
    age: int


app = FastAPI()


@app.post("/users")
async def create_user(user: User):
    return user

if  __name__=='__main__':
    uvicorn.run(app="chapter3_request_body_02:app", host="127.0.0.1", port=8080, reload=True)