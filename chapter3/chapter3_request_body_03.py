pyfrom fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class User(BaseModel):
    name: str
    age: int


class Company(BaseModel):
    name: str


app = FastAPI()


@app.post("/users")
async def create_user(user: User, company: Company):
    return {"user": user, "company": company}


if  __name__=='__main__':
    uvicorn.run(app="chapter3_request_body_03:app", host="127.0.0.1", port=8080, reload=True)