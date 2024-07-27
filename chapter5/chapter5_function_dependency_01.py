from typing import Tuple

from fastapi import FastAPI, Depends
import uvicorn

app = FastAPI()


async def pagination(skip: int = 0, limit: int = 10) -> Tuple[int, int]:
    return (skip, limit)


@app.get("/items")
async def list_items(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}


@app.get("/things")
async def list_things(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}

if  __name__=='__main__':
    uvicorn.run(app="chapter5_function_dependency_01:app", host="127.0.0.1", port=8080, reload=True)