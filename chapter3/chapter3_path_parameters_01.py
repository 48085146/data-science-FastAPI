from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/users/{id}")
async def get_user(id: int):
    return {"id": id}

if  __name__=='__main__':
    uvicorn.run(app="chapter3_path_parameters_01:app", host="127.0.0.1", port=8080, reload=True)