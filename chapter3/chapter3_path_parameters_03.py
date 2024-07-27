from enum import Enum
from fastapi import FastAPI
import uvicorn

class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"


app = FastAPI()


@app.get("/users/{type}/{id}/")
async def get_user(type: UserType, id: int):
    return {"type": type, "id": id}

if  __name__=='__main__':
    uvicorn.run(app="chapter3_path_parameters_03:app", host="127.0.0.1", port=8080, reload=True)