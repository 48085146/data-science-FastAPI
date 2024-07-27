from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def hello_world():
    return {"hello": "world"}


if  __name__=='__main__':
    uvicorn.run(app="chapter3_first_endpoint_01:app", host="127.0.0.1", port=8080, reload=True)