from fastapi import FastAPI, Header
import uvicorn

app = FastAPI()


@app.get("/")
async def get_header(hello: str = Header(...)):
    return {"hello": hello}

if  __name__=='__main__':
    uvicorn.run(app="chapter3_headers_cookies_01:app", host="127.0.0.1", port=8080, reload=True)