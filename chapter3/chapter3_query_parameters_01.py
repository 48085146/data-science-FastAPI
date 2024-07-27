from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/users")
async def get_user(page: int = 1, size: int = 10):
    return {"page": page, "size": size}

if  __name__=='__main__':
    uvicorn.run(app="chapter3_query_parameters_01:app", host="127.0.0.1", port=8080, reload=True)