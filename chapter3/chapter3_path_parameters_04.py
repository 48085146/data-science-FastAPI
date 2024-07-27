from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()


@app.get("/users/{id}")
async def get_user(id: int = Path(..., ge=1)):
    return {"id": id}

if  __name__=='__main__':
    uvicorn.run(app="chapter3_path_parameters_04:app", host="127.0.0.1", port=8080, reload=True)