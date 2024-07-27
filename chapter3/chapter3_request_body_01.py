from fastapi import FastAPI, Body
import uvicorn

app = FastAPI()


@app.post("/users")
async def create_user(name: str = Body(...), age: int = Body(...)):
    return {"name": name, "age": age}

if  __name__=='__main__':
    uvicorn.run(app="chapter3_request_body_01:app", host="127.0.0.1", port=8080, reload=True)