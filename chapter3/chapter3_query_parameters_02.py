from enum import Enum
from fastapi import FastAPI
import uvicorn


class UsersFormat(str, Enum):
    SHORT = "short"
    FULL = "full"


app = FastAPI()


@app.get("/users")
async def get_user(format: UsersFormat):
    return {"format": format}

if  __name__=='__main__':
    uvicorn.run(app="chapter3_query_parameters_02:app", host="127.0.0.1", port=8080, reload=True)